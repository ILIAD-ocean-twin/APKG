"""Convert APKG registry records (v1 JSON) to RDF (Turtle and/or JSON-LD) following the APKG-LDAP v2 profile,
then validate the result with validate.py.

Instructions (requirements, how to run, mapping): see README.md in this folder.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PREFIXES = {
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "adms": "http://www.w3.org/ns/adms#",
    "apkg-rec": "http://w3id.org/apkg/v2/records#",
    "apkg-pro": "http://w3id.org/apkg/v2/process#",
    "bf": "http://id.loc.gov/ontologies/bibframe/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "geo": "http://www.opengis.net/ont/geosparql#",
    "pav": "http://purl.org/pav/",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
}

# Keys of the v1 JSON that are mapped (or deliberately ignored) by this script.
TOP_KEYS = {"id", "type", "geometry", "properties", "links", "conformsTo", "time", "linkTemplates"}
PROP_KEYS = {
    # Record (tables A.1.1 / A.1.2)
    "type", "title", "name", "description", "keywords", "created", "updated", "license", "rights",
    "themes", "formats", "contacts",
    # Process (table C14)
    "identifier", "family", "software_version", "date_created", "sdDatePublished", "latest", "url",
    "citation", "author", "contributor", "maintainer", "sdPublisher", "source_organization",
    "provider", "producer", "spatial_coverage", "temporal_coverage", "code_repository",
    "programming_language", "original_url", "class", "inputs", "outputs", "cwl",
}
IGNORED_PROP_KEYS = {"id"}  # short CWL id: not mapped in v2 (to be decided)


# ------------------------------------------------------------------ small RDF model
class Lit:
    def __init__(self, value, datatype=None):
        self.value, self.datatype = str(value), datatype


class Node:
    def __init__(self, types, iri=None):
        self.iri, self.types, self.props = iri, list(types), []

    def add(self, prop, value):
        if value is None or value == "" or value == []:
            return self
        if isinstance(value, (str, int, float)) and not isinstance(value, bool):
            value = Lit(value)
        self.props.append((prop, value))
        return self


def empty(v):
    return v is None or v == "" or v == [] or v == {}


def as_list(v):
    if empty(v):
        return []
    return v if isinstance(v, list) else [v]


def uri(v):
    return None if empty(v) else Lit(v, "xsd:anyURI")


def date_literal(v):
    if empty(v):
        return None
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
        return Lit(v, "xsd:date")
    return Lit(v, "xsd:dateTimeStamp")


# ------------------------------------------------------------------ mapping helpers
def email(value):
    return Node(["apkg-rec:Email"]).add("vcard:value", value)


def person(p):
    n = Node(["apkg-pro:Person"]).add("foaf:name", p.get("name"))
    if not empty(p.get("email")):
        n.add("vcard:hasEmail", email(p["email"]))
    return n


def address(a):
    n = Node(["apkg-rec:Address"])
    for key, prop in (("street_address", "vcard:street-address"), ("address_locality", "vcard:locality"),
                      ("administrative_area", "vcard:region"), ("postal_code", "vcard:postal-code"),
                      ("address_country", "vcard:country-name")):
        for v in as_list(a.get(key)):
            n.add(prop, v)
    for r in as_list(a.get("roles")):
        n.add("apkg-rec:contactPointType", r)
    return n


def organisation(o):
    n = Node(["apkg-pro:Organisation"]).add("skos:prefLabel", o.get("name")).add("apkg-pro:homepage", uri(o.get("url")))
    if not empty(o.get("address")):
        n.add("vcard:hasAddress", address(o["address"]))
    return n


def link(l):
    n = Node(["apkg-rec:Link"]).add("apkg-rec:href", uri(l.get("href"))).add("apkg-rec:rel", l.get("rel"))
    n.add("apkg-rec:mediaType", l.get("type")).add("dct:title", l.get("title"))
    if not empty(l.get("length")):
        n.add("apkg-rec:length", Lit(l["length"], "xsd:nonNegativeInteger"))
    for p in as_list(l.get("profile")):
        n.add("apkg-rec:profile", uri(p))
    n.add("dct:created", date_literal(l.get("created"))).add("dct:modified", date_literal(l.get("updated")))
    return n


def parameter(p):
    n = Node(["apkg-pro:Parameter"]).add("dct:identifier", p.get("id")).add("apkg-pro:parameterType", p.get("type"))
    n.add("dct:description", p.get("doc"))
    if "default" in p and p["default"] is not None:
        d = p["default"]
        n.add("apkg-pro:defaultValue", d if isinstance(d, str) else json.dumps(d))
    n.add("apkg-pro:format", p.get("format"))
    return n


def contact(c):
    n = Node(["apkg-rec:Contact"]).add("dct:identifier", c.get("identifier")).add("vcard:fn", c.get("name"))
    n.add("vcard:title", c.get("position")).add("vcard:organization-name", c.get("organization"))
    if not empty(c.get("logo")):
        n.add("vcard:hasLogo", link(c["logo"]))
    for ph in as_list(c.get("phones")):
        m = Node(["apkg-rec:Phone"]).add("vcard:value", ph.get("value"))
        for r in as_list(ph.get("roles")):
            m.add("apkg-rec:contactPointType", r)
        n.add("vcard:hasTelephone", m)
    for em in as_list(c.get("emails")):
        m = email(em.get("value"))
        for r in as_list(em.get("roles")):
            m.add("apkg-rec:contactPointType", r)
        n.add("vcard:hasEmail", m)
    for a in as_list(c.get("addresses")):
        n.add("vcard:hasAddress", address(a))
    for l in as_list(c.get("links")):
        n.add("apkg-rec:hasLink", link(l))
    n.add("apkg-rec:hoursOfService", c.get("hoursOfService")).add("apkg-rec:contactInstructions", c.get("contactInstructions"))
    for r in as_list(c.get("roles")):
        n.add("vcard:role", r)
    return n


def secrets_from_cwl(cwl_text):
    """Return one list of input ids per cwltool:Secrets hint found in the CWL (YAML) text."""
    if empty(cwl_text):
        return []
    lines = cwl_text.splitlines()
    found = []
    for i, line in enumerate(lines):
        if not re.search(r"cwltool:Secrets", line):
            continue
        base = len(line) - len(line.lstrip())
        ids = None
        for j in range(i, min(i + 50, len(lines))):
            l2 = lines[j]
            if j > i and l2.strip() and (len(l2) - len(l2.lstrip())) <= base and not l2.lstrip().startswith("secrets"):
                break
            m = re.search(r"secrets:\s*\[(.*)\]", l2)
            if m:
                ids = [x.strip().strip("'\"") for x in m.group(1).split(",") if x.strip()]
                break
            if re.search(r"secrets:\s*$", l2):
                ind = len(l2) - len(l2.lstrip())
                ids = []
                for k in range(j + 1, len(lines)):
                    l3 = lines[k]
                    m2 = re.match(r"\s*-\s*(.+?)\s*$", l3)
                    if m2 and (len(l3) - len(l3.lstrip())) >= ind:
                        ids.append(m2.group(1).strip("'\""))
                    elif l3.strip():
                        break
                break
        if ids:
            found.append(ids)
    return found


# ------------------------------------------------------------------ record
def convert(record, warnings):
    props = record.get("properties") or {}
    rid = record.get("id") or props.get("identifier")
    if empty(rid):
        raise ValueError("record without id")
    is_process = not empty(props.get("class"))
    main = Node(["apkg-pro:Process", "apkg-rec:Record"] if is_process else ["apkg-rec:Record"], iri=f"<{rid}>")

    for k in record:
        if k not in TOP_KEYS:
            warnings.append(f"top-level field '{k}' not mapped")
    for k in props:
        if k not in PROP_KEYS and k not in IGNORED_PROP_KEYS:
            warnings.append(f"field 'properties.{k}' not mapped")
    for k in ("time", "linkTemplates"):
        if not empty(record.get(k)):
            warnings.append(f"field '{k}' present but not mapped by this script")
    for k in ("language", "languages", "resourceLanguages", "externalIds"):
        if not empty(props.get(k)):
            warnings.append(f"field 'properties.{k}' present but not mapped by this script")

    # --- Record (A.1.1 / A.1.2)
    main.add("dct:identifier", rid)
    main.add("dct:created", date_literal(props.get("created")))
    main.add("dct:modified", date_literal(props.get("updated")))
    for c in as_list(record.get("conformsTo")):
        main.add("apkg-rec:conformsTo", uri(c))
    for l in as_list(record.get("links")):
        main.add("dcat:qualifiedRelation", link(l))
    main.add("apkg-rec:resourceType", props.get("type"))
    main.add("dct:title", props.get("title") or props.get("name"))
    main.add("dct:description", props.get("description"))
    g = record.get("geometry")
    if not empty(g):
        main.add("geo:hasGeometry", Node(["apkg-rec:Geometry"]).add("apkg-rec:geometryType", g.get("type"))
                 .add("apkg-rec:coordinates", json.dumps(g.get("coordinates"), separators=(",", ":"))))
    for kw in as_list(props.get("keywords")):
        main.add("dcat:keyword", kw)
    for t in as_list(props.get("themes")):
        th = Node(["apkg-rec:Theme"]).add("apkg-rec:scheme", uri(t.get("scheme")))
        for c in as_list(t.get("concepts")):
            c = c if isinstance(c, dict) else {"id": c}
            cn = Node(["apkg-rec:Concept"], iri=f"<{c['url']}>" if not empty(c.get("url")) else None)
            th.add("apkg-rec:hasConcept", cn.add("skos:notation", c.get("id")))
        main.add("apkg-rec:hasTheme", th)
    for f in as_list(props.get("formats")):
        main.add("dct:format", Node(["apkg-rec:Format"]).add("dct:title", f.get("name")).add("apkg-rec:mediaType", f.get("mediaType")))
    for c in as_list(props.get("contacts")):
        main.add("dcat:contactPoint", contact(c))
    main.add("apkg-rec:license", uri(props.get("license")))
    if not empty(props.get("rights")):
        main.add("dct:rights", Node(["dct:RightsStatement"]).add("rdfs:label", props["rights"]))

    if not is_process:
        return main

    # --- Process (C14)
    main.add("apkg-pro:processID", props.get("identifier") or rid)
    main.add("apkg-pro:familyID", props.get("family"))
    main.add("pav:version", props.get("software_version"))
    main.add("apkg-pro:dateCreated", date_literal(props.get("date_created")))
    main.add("apkg-pro:registrationDate", date_literal(props.get("sdDatePublished")))
    if props.get("latest") is not None:
        main.add("apkg-pro:isLatestVersion", Lit(str(props["latest"]).lower(), "xsd:boolean"))
    if not empty(props.get("url")):
        main.add("apkg-pro:cwlDescriptor", Node(["apkg-pro:CWLDescriptor"])
                 .add("apkg-pro:descriptorURL", uri(props["url"])).add("apkg-rec:mediaType", "application/cwl+yaml"))
    for c in as_list(props.get("citation")):
        main.add("apkg-pro:citation", c)
    for p in as_list(props.get("author")):
        main.add("dct:creator", person(p))
    for p in as_list(props.get("contributor")):
        main.add("dct:contributor", person(p))
    for p in as_list(props.get("maintainer")):
        main.add("apkg-pro:hasMaintainer", person(p))
    for o in as_list(props.get("sdPublisher"))[:1]:
        main.add("dct:publisher", organisation(o))
    for o in as_list(props.get("source_organization")):
        main.add("apkg-pro:hasSourceOrganisation", organisation(o))
    for o in as_list(props.get("provider")):
        main.add("apkg-pro:hasProviderOrganisation", organisation(o))
    for o in as_list(props.get("producer")):
        main.add("apkg-pro:hasProducerOrganisation", organisation(o))
    sc = props.get("spatial_coverage")
    if not empty(sc):
        node = Node(["apkg-pro:SpatialCoverage"])
        if not empty((sc.get("geo") or {}).get("box")):
            node.add("geo:hasGeometry", Node(["apkg-pro:Geo"]).add("apkg-pro:box", sc["geo"]["box"]))
        node.add("apkg-pro:geoClass", sc.get("class"))
        main.add("bf:geographicCoverage", node)
    main.add("apkg-pro:temporalCoverage", props.get("temporal_coverage"))
    main.add("apkg-pro:codeRepository", uri(props.get("code_repository")))
    for pl in as_list(props.get("programming_language")):
        main.add("apkg-pro:programmingLanguage", pl)
    main.add("apkg-pro:originalURL", uri(props.get("original_url")))
    main.add("apkg-pro:processClass", props.get("class"))
    for p in as_list(props.get("inputs")):
        main.add("apkg-pro:hasInput", parameter(p))
    for p in as_list(props.get("outputs")):
        main.add("apkg-pro:hasOutput", parameter(p))
    for ids in secrets_from_cwl(props.get("cwl")):
        s = Node(["apkg-pro:Secret"])
        for i in ids:
            s.add("apkg-pro:secretInputID", i)
        main.add("apkg-pro:hasSecret", s)
    return main


# ------------------------------------------------------------------ Turtle output
def lit_ttl(l):
    s = l.value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r")
    return f'"{s}"' if l.datatype in (None, "xsd:string") else f'"{s}"^^{l.datatype}'


def value_ttl(v, indent):
    if isinstance(v, Lit):
        return lit_ttl(v)
    if v.iri:
        # named node (e.g. a concept with an url): write inline with its description
        return v.iri if not v.props else node_ttl(v, indent, inline=True)
    return node_ttl(v, indent)


def grouped(props):
    order, groups = [], {}
    for p, v in props:
        if p not in groups:
            order.append(p)
            groups[p] = []
        groups[p].append(v)
    return [(p, groups[p]) for p in order]


def node_ttl(n, indent, inline=False):
    pad = " " * (indent + 4)
    parts = [f"a {', '.join(n.types)}"] + [f"{p} " + ", ".join(value_ttl(v, indent + 4) for v in vs) for p, vs in grouped(n.props)]
    if inline and n.iri:
        # A named node (e.g. a concept with an url) cannot be nested in Turtle:
        # it is referenced by its IRI here and described in its own block at the end.
        EXTRA.append(n)
        return n.iri
    return "[\n" + pad + (" ;\n" + pad).join(parts) + "\n" + " " * indent + "]"


EXTRA = []


def to_turtle(main, source):
    EXTRA.clear()
    out_head = "".join(f"@prefix {p}: <{u}> .\n" for p, u in PREFIXES.items())
    body = f"\n# Converted from {source}\n# following the APKG-LDAP v2 application profile (SCRIPTS/json2rdf.py).\n\n"
    parts = [f"a {', '.join(main.types)}"] + [f"{p} " + ", ".join(value_ttl(v, 4) for v in vs) for p, vs in grouped(main.props)]
    body += main.iri + " " + " ;\n    ".join(parts) + " .\n"
    while EXTRA:
        n = EXTRA.pop(0)
        parts = [f"a {', '.join(n.types)}"] + [f"{p} " + ", ".join(value_ttl(v, 4) for v in vs) for p, vs in grouped(n.props)]
        body += "\n" + n.iri + " " + " ;\n    ".join(parts) + " .\n"
    return out_head + body


# ------------------------------------------------------------------ main
def jsonld_value(v):
    if isinstance(v, Lit):
        if v.datatype in (None, "xsd:string"):
            return v.value
        return {"@value": v.value, "@type": v.datatype}
    return jsonld_node(v)


def jsonld_node(n):
    obj = {}
    if n.iri:
        obj["@id"] = n.iri.strip("<>")
    obj["@type"] = n.types if len(n.types) > 1 else n.types[0]
    for p, vs in grouped(n.props):
        values = [jsonld_value(v) for v in vs]
        obj[p] = values if len(values) > 1 else values[0]
    return obj


def to_jsonld(main, source):
    doc = {"@context": dict(PREFIXES)}
    doc.update(jsonld_node(main))
    return json.dumps(doc, ensure_ascii=False, indent=2) + "\n"


def records_in(data):
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and isinstance(data.get("features"), list):
        return data["features"]
    return [data]


def safe_name(rid):
    name = re.sub(r"^urn:apkg:", "", rid)
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name)


def main():
    ap = argparse.ArgumentParser(description="Convert APKG v1 JSON records to APKG-LDAP v2 Turtle and validate them.")
    ap.add_argument("inputs", nargs="+", help="JSON files or folders with JSON files")
    ap.add_argument("-o", "--output", default=str(ROOT / "examples"), help="output folder (default: examples/)")
    ap.add_argument("--no-validate", action="store_true", help="do not run the SHACL validation at the end")
    ap.add_argument("-f", "--format", choices=["ttl", "jsonld", "both"], default="ttl",
                    help="output format: ttl (Turtle, default), jsonld (JSON-LD) or both")
    args = ap.parse_args()

    files = []
    for i in args.inputs:
        p = Path(i)
        files += sorted(p.glob("*.json")) if p.is_dir() else [p]
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    written, ok = [], True
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"ERROR reading {f}: {e}")
            ok = False
            continue
        for rec in records_in(data):
            warnings = []
            try:
                node = convert(rec, warnings)
            except Exception as e:
                print(f"ERROR converting a record of {f}: {e}")
                ok = False
                continue
            rid = rec.get("id") or rec["properties"]["identifier"]
            outputs = []
            if args.format in ("ttl", "both"):
                target = out_dir / f"{safe_name(rid)}.ttl"
                target.write_text(to_turtle(node, rid), encoding="utf-8")
                outputs.append(target)
            if args.format in ("jsonld", "both"):
                target = out_dir / f"{safe_name(rid)}.jsonld"
                target.write_text(to_jsonld(node, rid), encoding="utf-8")
                outputs.append(target)
            written += outputs
            print(f"{f.name} -> " + ", ".join(str(t) for t in outputs))
            for w in warnings:
                print(f"   warning: {w}")

    if not written:
        return 1
    if args.no_validate:
        return 0 if ok else 1

    print("\nSHACL validation\n----------------")
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from validate import validate_files
    except ImportError:
        print("validate.py not found next to this script; validation skipped.")
        return 0 if ok else 1
    try:
        valid = validate_files(written)
    except ImportError:
        print("pyshacl is not installed (pip install pyshacl); validation skipped.")
        return 0 if ok else 1
    return 0 if ok and valid else 1


if __name__ == "__main__":
    sys.exit(main())
