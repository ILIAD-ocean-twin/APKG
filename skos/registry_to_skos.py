import sys
recs = []
for block in open(sys.argv[1], encoding='utf-8').read().split('\n%%\n')[1:]:
    d = {}
    key = None
    for line in block.splitlines():
        if line.startswith('  ') and key:
            d[key][-1] += ' ' + line.strip(); continue
        key, _, val = line.partition(': ')
        d.setdefault(key, []).append(val)
    if d['Type'][0] == 'language':
        recs.append(d)
date = open(sys.argv[1], encoding='utf-8').readline().split(': ')[1].strip()
subtags = {r['Subtag'][0] for r in recs}

def lit(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

out = [f"""@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dct:  <http://purl.org/dc/terms/> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix lang: <http://example.org/bcp47/language/> .
@prefix scope: <http://example.org/bcp47/scope/> .

# SKOS rendering of the "Type: language" records of the IANA Language Subtag
# Registry (RFC 5646 / BCP 47), registry File-Date {date}.
# Change the "lang:" and "scope:" namespaces to your own base URIs before publishing.

lang: a skos:ConceptScheme ;
    skos:prefLabel "IANA Language Subtag Registry — primary language subtags"@en ;
    dct:source <https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry> ;
    dct:conformsTo <https://www.rfc-editor.org/info/rfc5646> ;
    dct:issued "{date}"^^xsd:date .
"""]

scopes = {}
for r in recs:
    st = r['Subtag'][0]
    desc = r['Description']
    p = [f"lang:{st} a skos:Concept",
         "    skos:inScheme lang:",
         f"    skos:notation {lit(st)}",
         f"    skos:prefLabel {lit(desc[0])}@en"]
    for a in desc[1:]:
        p.append(f"    skos:altLabel {lit(a)}@en")
    p.append(f"    dct:created \"{r['Added'][0]}\"^^xsd:date")
    if 'Macrolanguage' in r:
        m = r['Macrolanguage'][0]
        assert m in subtags, m
        p.append(f"    skos:broader lang:{m}")
    else:
        p.append("    skos:topConceptOf lang:")
    if 'Scope' in r:
        scopes.setdefault(r['Scope'][0], []).append(st)
    if 'Deprecated' in r:
        p.append("    owl:deprecated true")
        p.append(f"    dct:modified \"{r['Deprecated'][0]}\"^^xsd:date")
    if 'Preferred-Value' in r:
        pv = r['Preferred-Value'][0]
        assert pv in subtags, pv
        p.append(f"    dct:isReplacedBy lang:{pv}")
    if 'Suppress-Script' in r:
        p.append(f"    skos:note {lit('Suppress-Script: ' + r['Suppress-Script'][0])}")
    for c in r.get('Comments', []):
        p.append(f"    skos:scopeNote {lit(c)}@en")
    out.append(' ;\n'.join(p) + ' .\n')

for sc, members in sorted(scopes.items()):
    out.append(f"scope:{sc} a skos:Collection ;\n    skos:prefLabel {lit('Scope: ' + sc)}@en ;\n    skos:member "
               + ', '.join(f'lang:{m}' for m in members) + ' .\n')

# narrower inverses
narrow = {}
for r in recs:
    if 'Macrolanguage' in r:
        narrow.setdefault(r['Macrolanguage'][0], []).append(r['Subtag'][0])
out.append("# Macrolanguage → encompassed languages")
for m, kids in sorted(narrow.items()):
    out.append(f"lang:{m} skos:narrower " + ', '.join(f'lang:{k}' for k in kids) + ' .')
out.append("\n# Top concepts")
tops = [r['Subtag'][0] for r in recs if 'Macrolanguage' not in r]
out.append("lang: skos:hasTopConcept " + ', '.join(f'lang:{t}' for t in tops) + ' .')

open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(recs), 'concepts;', len(tops), 'top;', sum(map(len, narrow.values())), 'with broader;', {k: len(v) for k, v in scopes.items()})
