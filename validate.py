"""Validate APKG-LDAP v2 example data against the SHACL shapes with pyshacl.

Usage (from the APKG folder):
    pip install pyshacl
    python validate.py                      # validates every .ttl in examples/
    python validate.py path/to/data.ttl     # validates one or more given files
"""
import sys
from pathlib import Path

from rdflib import Graph
from pyshacl import validate

ROOT = Path(__file__).resolve().parent

ONTOLOGY = ["terms/apkg-declarations-v2.ttl", "terms/apkg-rec-v2.ttl", "terms/apkg-pro-v2.ttl"]
SHAPES = ["SHACL/apkg-rec-shapes-v2.ttl", "SHACL/apkg-pro-shapes-v2.ttl"]


def load(paths):
    g = Graph()
    for p in paths:
        g.parse(ROOT / p if not Path(p).is_absolute() else p, format="turtle")
    return g


def main():
    data_files = sys.argv[1:] or sorted(str(p) for p in (ROOT / "examples").glob("*.ttl"))
    if not data_files:
        print("No data files found.")
        return 1

    # Parsing the ontology and shapes also checks that their Turtle syntax is valid.
    ont = load(ONTOLOGY)
    shapes = load(SHAPES)
    print(f"Ontology: {len(ont)} triples. Shapes: {len(shapes)} triples.\n")

    all_ok = True
    for f in data_files:
        data = load([f])
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
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
