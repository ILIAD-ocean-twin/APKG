"""Validate APKG-LDAP v2 data (Turtle) against the SHACL shapes with pyshacl.

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
          python SCRIPTS\\validate.py
              -> validates every .ttl file in the examples\\ folder
          python SCRIPTS\\validate.py examples\\my-record.ttl
              -> validates one file
          python SCRIPTS\\validate.py file1.ttl file2.ttl
              -> validates several files

    json2ttl.py (in this folder) calls this script automatically at the end
    of each conversion.

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
        data.parse(str(f), format="turtle")
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
    data_files = [Path(a).resolve() for a in sys.argv[1:]] or sorted((ROOT / "examples").glob("*.ttl"))
    if not data_files:
        print("No data files found.")
        return 1
    return 0 if validate_files(data_files) else 1


if __name__ == "__main__":
    sys.exit(main())
