# The __Application Package__ Application Profile V2.0 - Examples

[<- main](../README.md)

This folder contains records of the [APKG registry](https://iliad-registry.inesctec.pt/collections/apkg/items?f=html) converted to RDF following the APKG Linked Data Application Profile v2 (APKG-LDAP v2). Each record is available in two serialisations that hold exactly the same RDF graph:

- Turtle (`.ttl`)
- JSON-LD (`.jsonld`)

All files conform to the SHACL shapes of the profile (folder `shacl/`), except one record with an error in its source data (see [Known issues](#known-issues)).

## Contents

The folder holds every record of the registry. Two of them are described below as reference examples.

| File | Record | Kind |
|------|--------|------|
| `tool_inesctec_pt_virtual-choreographies-transformer-plugin-unity_0.2.1.ttl` / `.jsonld` | `urn:apkg:tool:inesctec:pt:virtual-choreographies-transformer-plugin-unity:0.2.1` | CommandLineTool |
| `workflow_forth_gr_oilspill_pipeline_medslik_146_1.0.0.ttl` / `.jsonld` | `urn:apkg:workflow:forth:gr:oilspill_pipeline_medslik_146:1.0.0` | Workflow (with secrets) |
| `json/` | the source records in JSON, as returned by the registry (`?f=json`), when downloaded with `scripts/download_registry.py` | |

**File names** are built from the record id without the `urn:apkg:` prefix, with `:` replaced by `_`. The record id (URN) is also the IRI of the main node in each file.

## What each example shows

- **Tool** (`virtual-choreographies-transformer-plugin-unity`): a CommandLineTool with optional parameters (`File?`, `string?`), an output with an EDAM format, maintainers, contributors and authors (`apkg-pro:Person`), and source and producer organisations with an address.
- **Workflow** (`oilspill_pipeline_medslik_146`): a Workflow with parameters that have default values and descriptions, a licence, an open-ended temporal coverage (`2014-01-01T00:00:00Z/`), a creation date without time (`xsd:date`), and secrets taken from the `cwltool:Secrets` hint of its CWL.

Both records have the Record part (identifier, title, description, keywords, GeoJSON geometry, links) and the Process part (version, family, class, CWL descriptor, spatial coverage, organisations, inputs and outputs).

## How to regenerate the examples

Open a terminal and position yourself in the root folder of the repository (the folder that contains `examples`, `scripts`, `shacl` and `terms`). See [scripts/README.md](../scripts/README.md) for the requirements.

**All records of the registry**, downloaded, converted to Turtle and JSON-LD, and validated:

```
python scripts\download_registry.py --with-cwl --convert
```

This saves the JSON files in `examples\json\` and the `.ttl` and `.jsonld` files in `examples\`. The option `--with-cwl` also downloads the CWL of each record, so that the secrets can be extracted.

**One record**, from a JSON file:

```
python scripts\json2rdf.py examples\json\<file>.json --format both
```

**Validate** every file in this folder:

```
python scripts\validate.py
```

## Notes

- Nodes other than the main record (links, persons, organisations, parameters, ...) are blank nodes, so the same organisation appears as separate nodes when it is cited more than once (e.g. as source and as producer).
- Empty values in the JSON (`null`, `""`, `[]`) are not converted.
- The short CWL id (`properties.id`) is not converted in v2.
- On macOS or Linux, use `/` instead of `\` in the paths.

## Known issues

- **`tool_inesctec_pt_2stac_simulation_0.2.0.ttl` / `.jsonld`** (`urn:apkg:tool:inesctec:pt:2stac_simulation:0.2.0`) does **not** conform to the shapes. The error is in the record's CWL in the registry, not in the profile or in the conversion: `InitialWorkDirRequirement` is indented under `outputs`, so it is read as an output parameter without a type, and the shapes report the missing `apkg-pro:parameterType` (`sh:minCount 1`). The file is kept as a real example of what the validation catches. It will conform once the CWL is corrected in the registry and the record is downloaded and converted again.
