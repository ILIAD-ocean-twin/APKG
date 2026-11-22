"""Validate APKG-LDAP v2 data (Turtle .ttl or JSON-LD .jsonld) against the SHACL shapes with pyshacl.

Instructions (requirements, how to run, mapping): see README.md in this folder.
"""
import sys
from pathlib import Path

# The APKG folder is the parent of SCRIPTS/.
ROOT = Path(__file__).resolve().parent.parent

ONTOLOGY = ["terms/apkg-declarations-v2.ttl", "terms/apkg-rec-v2.ttl", "terms/apkg-pro-v2.ttl"]
SHAPES = ["SHACL/apkg-rec-shapes-v2.ttl", "SHACL/apkg-pro-shapes-v2.ttl"]


def _load(paths):
    from rdflib import Graph
    g = Graph()
    for p in paths:
        p = Path(p)
        g.parse(p if p.is_absolute() else ROOT / p, format="turtle")
    return g


def validate_files(data_files):
    """Validate the given Turtle files. Returns True if all of them conform."""
    from rdflib import Graph
    from pyshacl import validate

    ont = _load(ONTOLOGY)
    shapes = _load(SHAPES)
    print(f"Ontology: {len(ont)} triples. Shapes: {len(shapes)} triples.\n")

    all_ok = True
    for f in data_files:
        data = Graph()
        fmt = "json-ld" if Path(f).suffix.lower() in (".jsonld", ".json") else "turtle"
        data.parse(str(f), format=fmt)
        conforms, _, report = validate(
            data,
            shacl_graph=shapes,
            ont_graph=ont,        # lets sh:class see rdfs:subClassOf from the ontology
            inference="none",     # the shapes are designed to work without inference
            abort_on_first=False,
        )
        print(f"{Path(f).name}: {len(data)} triples -> {'CONFORMS' if conforms else 'DOES NOT CONFORM'}")
        if not conforms:
            all_ok = False
            print(report)
    return all_ok


def main():
    data_files = [Path(a).resolve() for a in sys.argv[1:]] or sorted([*(ROOT / "examples").glob("*.ttl"), *(ROOT / "examples").glob("*.jsonld")])
    if not data_files:
        print("No data files found.")
        return 1
    return 0 if validate_files(data_files) else 1


if __name__ == "__main__":
    sys.exit(main())
