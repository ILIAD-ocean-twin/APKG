# APKG-LDAP v2 scripts

[<- main](../README.md)

Three scripts for the APKG Linked Data Application Profile v2:

| Script | What it does |
|--------|--------------|
| `json2rdf.py` | Converts APKG registry records (v1 JSON) to RDF following the profile, as Turtle (`.ttl`), JSON-LD (`.jsonld`) or both, and validates the result at the end. |
| `validate.py` | Validates RDF data (`.ttl` or `.jsonld`) against the SHACL shapes of the profile. |
| `download_registry.py` | Downloads every record of the APKG registry as JSON (optionally with its CWL) and can convert them all with `json2rdf.py`. |

The `RFC5646` folder holds a separate script (`registry_to_skos.py`) for the language subtag registry.

## Requirements

- Python 3.9 or later. Check with:

  ```
  python --version
  ```

- `pyshacl`, which also installs `rdflib`. Install it once with:

  ```
  pip install pyshacl
  ```

  If `pip` is not found, use `python -m pip install pyshacl`.

The conversion itself (`json2rdf.py`) needs nothing besides Python. Without `pyshacl` the files are still converted, and the validation at the end is skipped with a message.

## How to run

Open a terminal (Command Prompt, PowerShell or the VS Code terminal) and position yourself in the root folder of the repository, that is, the folder that contains `SCRIPTS`, `SHACL`, `terms` and `examples`:

```
cd <path-to-the-repository>
```

All the commands below are run from that folder. On macOS or Linux, use `/` instead of `\` in the paths (e.g. `python SCRIPTS/json2rdf.py`).

### json2rdf.py: convert JSON to RDF

| Command | Result |
|---------|--------|
| `python SCRIPTS\json2rdf.py record.json` | Converts one record and writes `examples\<name>.ttl` |
| `python SCRIPTS\json2rdf.py rec1.json rec2.json` | Converts several records |
| `python SCRIPTS\json2rdf.py some\folder` | Converts every `.json` file in the folder |
| `python SCRIPTS\json2rdf.py record.json --format jsonld` | Writes JSON-LD (`examples\<name>.jsonld`) instead of Turtle |
| `python SCRIPTS\json2rdf.py record.json --format both` | Writes both `<name>.ttl` and `<name>.jsonld` |
| `python SCRIPTS\json2rdf.py record.json -o out` | Writes the files to the folder `out` instead of `examples\` |
| `python SCRIPTS\json2rdf.py record.json --no-validate` | Converts only, without the SHACL validation |

The options can be combined, for example:

```
python SCRIPTS\json2rdf.py some\folder --format both -o out
```

**Input.** A record as returned by the registry with `?f=json`, for example
`https://iliad-registry.inesctec.pt/collections/apkg/items/<id>?f=json`.
A file may also hold a list of records, or a FeatureCollection (`{"features": [...]}`, as returned by `.../items?f=json`).

**Output file names.** Built from the record id (URN) without the `urn:apkg:` prefix, e.g. `workflow_forth_gr_oilspill_pipeline_medslik_146_1.0.0.ttl`. A record with the same id overwrites the previous file.

At the end, `json2rdf.py` calls `validate.py` on the files it has just written.

### validate.py: SHACL validation

| Command | Result |
|---------|--------|
| `python SCRIPTS\validate.py` | Validates every `.ttl` and `.jsonld` file in the `examples\` folder |
| `python SCRIPTS\validate.py examples\my-record.ttl` | Validates one file (`.ttl` or `.jsonld`) |
| `python SCRIPTS\validate.py file1.ttl file2.jsonld` | Validates several files |

What it does:

1. Reads the ontology (`terms/apkg-declarations-v2.ttl`, `terms/apkg-rec-v2.ttl`, `terms/apkg-pro-v2.ttl`) and the shapes (`SHACL/apkg-rec-shapes-v2.ttl`, `SHACL/apkg-pro-shapes-v2.ttl`). A syntax error in any of them stops the script with the file and line of the error.
2. Validates each data file without inference (the shapes are designed for that), passing the ontology so that `sh:class` sees `rdfs:subClassOf`.
3. Prints `CONFORMS` or `DOES NOT CONFORM` for each file, and the SHACL report with the violations when a file does not conform.

### download_registry.py: download all records of the registry

| Command | Result |
|---------|--------|
| `python SCRIPTS\download_registry.py` | Downloads every record as JSON into `examples\json\` (one file per record) |
| `python SCRIPTS\download_registry.py --with-cwl` | Also downloads each record's CWL (`?f=cwl`) and stores it in the field `cwl`, so that `json2rdf.py` can extract the secrets |
| `python SCRIPTS\download_registry.py --with-cwl --convert` | Downloads, then converts every record to Turtle and JSON-LD in `examples\` and validates them |
| `python SCRIPTS\download_registry.py -o some\folder` | Saves the JSON files in another folder |
| `python SCRIPTS\download_registry.py --fast` | Keeps the records as given in the listing pages, without downloading each record (faster, but without the records' links) |
| `python SCRIPTS\download_registry.py --rdf-output out --convert` | Writes the converted files to `out` instead of `examples\` |

By default it reads `https://iliad-registry.inesctec.pt/collections/apkg/items`; another collection can be given with `--url`. Each record is downloaded from its own URL (`.../items/<id>?f=json`), because the listing pages do not include the records' `links`; this takes one request per record (use `--fast` to skip it). It pages through the collection (following the `next` links, or by offset) until it has read the number of records the registry reports (`numberMatched`), and warns if the counts differ. It needs nothing besides Python; `--convert` uses `pyshacl` for the validation, as above.

### Exit code

`json2rdf.py` and `validate.py` return `0` when everything was converted and conforms, and `1` otherwise (useful in other scripts or CI). `download_registry.py --convert` returns the result of the conversion.

## Mapping (json2rdf.py)

The mapping follows the tables of the profile (see the [main README](../README.md)).

- The record id (URN) is the IRI of the main node, typed `apkg-rec:Record` and, when `properties.class` is present, also `apkg-pro:Process`.
- All other nodes (links, persons, organisations, parameters, ...) are blank nodes.
- Secrets are taken from the field `Secrets` (`{"secrets": [...]}`) when present, otherwise from the `cwltool:Secrets` hints of the embedded CWL (field `cwl`, added by `download_registry.py --with-cwl`).
- `registration_url` is mapped to `apkg-pro:originalURL`.
- CWL parameter types are written as one string: `File?` (optional), `File[]` (array), and union types (a JSON list such as `["string?", "File?"]`) joined with `|` (`string?|File?`).
- Empty values (`null`, `""`, `[]`) are not mapped.
- The short CWL id (`properties.id`) is not mapped in v2.
- Fields that the script does not map are listed as warnings, so that nothing is lost silently. This includes the parameter fields `label` and `keywords`, which the profile does not cover yet. The OGC fields `time`, `language`, `languages`, `resourceLanguages`, `externalIds` and `linkTemplates` are reported as warnings when present.

## JSON-LD output

Turtle and JSON-LD hold exactly the same RDF graph.

The JSON-LD is self-contained: its `@context` only declares the namespace prefixes of the profile, and properties are written as compact IRIs (e.g. `"dct:title"`, `"apkg-pro:processClass"`), so no remote context has to be fetched to read it. Typed values (dates, URLs, booleans) use `{"@value": ..., "@type": "xsd:..."}`, and related nodes are nested objects.
