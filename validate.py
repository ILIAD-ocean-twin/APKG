"""Validate APKG-LDAP v2 example data against the SHACL shapes with pyshacl.

REQUIREMENTS
    - Python 3.9 or later (check with:  python --version)
    - pyshacl, which also installs rdflib. Install it once with:
          pip install pyshacl
      If "pip" is not found, use:
          python -m pip install pyshacl

HOW TO RUN
    Open a terminal (Command Prompt, PowerShell or the VS Code terminal)
    in the APKG folder, for example:
          cd C:\\Users\\dei\\GitHub\\APKG

    Then run one of:
          python validate.py
              -> validates every .ttl file in the examples/ folder
          python validate.py examples\\my-record.ttl
              -> validates one file
          python validate.py file1.ttl file2.ttl
              -> validates several files

WHAT IT DOES
    1. Reads the ontology (terms/apkg-declarations-v2.ttl, terms/apkg-rec-v2.ttl,
       terms/apkg-pro-v2.ttl) and the shapes (SHACL/apkg-rec-shapes-v2.ttl,
       SHACL/apkg-pro-shapes-v2.ttl). A Turtle syntax error in any of them
       stops the script with the file and line of the error.
    2. Validates each data file without inference (the shapes are designed
       for that), passing the ontology so that sh:class sees rdfs:subClassOf.
    3. Prints CONFORMS or DOES NOT CONFORM for each file, and the SHACL
       report with the violations when a file does not conform.

EXIT CODE
    0 if every file conforms, 1 otherwise (useful in scripts or CI).
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
