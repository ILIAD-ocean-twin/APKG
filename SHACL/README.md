# The __Application Package__ Application Profile V2.0 - APKG SHACL shapes

[<- main](../README.md)

This folder contains the SHACL shapes of the APKG Linked Data Application Profile v2 (APKG-LDAP v2). They check that an RDF description of a catalogue Record or of a Process (an application package) conforms to the profile: which properties each class may or must have, how many values, and of which datatype, class or value list.

## Files

| File | Module | Shapes for | Shapes graph IRI |
|------|--------|-----------|------------------|
| `apkg-rec-shapes-v2.ttl` | Record (Core), prefix `apkg-rec:` | Tables A.1.1, A.1.2 and B2-B13 | `http://w3id.org/apkg/v2/records/shapes` |
| `apkg-pro-shapes-v2.ttl` | Process, prefix `apkg-pro:` | Tables C14 and D15-D21 | `http://w3id.org/apkg/v2/process/shapes` |

The two files follow the two modules of the ontology (folder `terms/`):

- `apkg-rec-shapes-v2.ttl` imports the Record ontology (`terms/apkg-rec-v2.ttl`) and does not depend on the Process module.
- `apkg-pro-shapes-v2.ttl` imports the Process ontology (`terms/apkg-pro-v2.ttl`) and the Record shapes, because a Process is also a Record.

To validate data, load **both** files as one shapes graph. The script `SCRIPTS/validate.py` does this for you.

## How to validate

The easiest way is the validation script (see [SCRIPTS/README.md](../SCRIPTS/README.md)). Open a terminal and position yourself in the root folder of the repository (the folder that contains `SHACL`, `terms`, `examples` and `SCRIPTS`), then run:

```
python SCRIPTS\validate.py                      (every .ttl and .jsonld in examples\)
python SCRIPTS\validate.py examples\my-record.ttl
```

It loads the two shapes files and the ontology, validates without inference, and prints `CONFORMS` or the SHACL report for each file.

Any other SHACL processor can be used, as long as it supports SHACL Core and SHACL-SPARQL (needed by the Language shape), and both shapes files are given together.

## Shapes

### Record module (`apkg-rec-shapes-v2.ttl`)

| Shape | Target class | Table | Main constraints |
|-------|--------------|-------|------------------|
| `apkg-rec:RecordShape` | `apkg-rec:Record` | A.1.1, A.1.2 | `dct:identifier` and `dct:title` exactly 1; dates as `xsd:dateTimeStamp`; `conformsTo`, `license` as `xsd:anyURI`; `geo:hasGeometry` to a Geometry; `time:hasTime` to a `time:Interval` or `time:Instant`; links, themes, formats, contacts typed with their classes |
| `apkg-rec:ExternalIdentifierShape` | (used by RecordShape) | A.1.2 | `adms:Identifier` node: `skos:notation` exactly 1, `adms:schemaAgency` at most 1 |
| `apkg-rec:RightsStatementShape` | (used by RecordShape) | A.1.2 | `dct:RightsStatement` node: at least one `rdfs:label` |
| `apkg-rec:AddressShape` | `apkg-rec:Address` | B2 | country as a two-letter code (`^[A-Z]{2}$`); `contactPointType` in private, work, billing, delivery |
| `apkg-rec:ConceptShape` | `apkg-rec:Concept` | B3 | `skos:notation` exactly 1 |
| `apkg-rec:ContactShape` | `apkg-rec:Contact` | B4 | at least a name (`vcard:fn`) or an organisation (`vcard:organization-name`); `vcard:role` in the ISO 19115 CI_RoleCode list; logo, phones, emails, addresses, links typed with their classes |
| `apkg-rec:LogoLinkShape` | (used by ContactShape) | B4 | a logo Link has `rel` = "icon" and a media type |
| `apkg-rec:EmailShape` | `apkg-rec:Email` | B5 | `vcard:value` exactly 1, email syntax; `contactPointType` in private, work |
| `apkg-rec:FormatShape` | `apkg-rec:Format` | B6 | `dct:title` and `mediaType` (type/subtype syntax) at most 1 |
| `apkg-rec:GeometryShape` | `apkg-rec:Geometry` | B7 | `geometryType` in the GeoJSON types (RFC 7946); `coordinates` as one JSON array string |
| `apkg-rec:IriTemplateMappingShape` | `apkg-rec:IriTemplateMapping` | B8 | `hydra:variable` exactly 1 |
| `apkg-rec:LanguageShape` | `apkg-rec:Language` | B9 | `skos:notation` exactly 1 as `xsd:language`; `textDirection` in ltr, rtl, ttb, btt; SHACL-SPARQL: the language tag of `skos:prefLabel` must equal the code |
| `apkg-rec:LinkShape` | `apkg-rec:Link` | B10 | `href` (`xsd:anyURI`) and `rel` exactly 1; `rel` from the IANA registry, "root", or a URI; `mediaType` type/subtype syntax; `length` as `xsd:nonNegativeInteger` |
| `apkg-rec:LinkTemplateShape` | `apkg-rec:LinkTemplate` | B11 | `hydra:template` exactly 1 (`hydra:Rfc6570Template`); `rel` as in LinkShape; mappings typed as IriTemplateMapping |
| `apkg-rec:PhoneShape` | `apkg-rec:Phone` | B12 | `vcard:value` exactly 1 in E.164 (`^\+[1-9][0-9]{3,14}$`); `contactPointType` in private, work |
| `apkg-rec:ThemeShape` | `apkg-rec:Theme` | B13 | at least one concept; `scheme` exactly 1 as `xsd:anyURI` |

### Process module (`apkg-pro-shapes-v2.ttl`)

| Shape | Target class | Table | Main constraints |
|-------|--------------|-------|------------------|
| `apkg-pro:ProcessShape` | `apkg-pro:Process` | C14 | also applies `apkg-rec:RecordShape`; `processID`, `pav:version`, `processClass` (CommandLineTool or Workflow) exactly 1; at least one author (`dct:creator`); exactly one producer; at least one source organisation (the producer counts); `dateCreated` as `xsd:date` or `xsd:dateTimeStamp`; `registrationDate` as `xsd:dateTimeStamp`; inputs, outputs, secrets typed with their classes |
| `apkg-pro:CWLDescriptorShape` | `apkg-pro:CWLDescriptor` | D15 | `descriptorURL` exactly 1; `mediaType` fixed to "application/cwl+yaml" |
| `apkg-pro:GeoShape` | `apkg-pro:Geo` | D16 | `box` exactly 1, four numbers (schema.org box syntax) |
| `apkg-pro:OrganisationShape` | `apkg-pro:Organisation` | D17 | name (`skos:prefLabel`) and `homepage` exactly 1; address at most 1 |
| `apkg-pro:ParameterShape` | `apkg-pro:Parameter` | D18 | `dct:identifier` and `parameterType` exactly 1; type in the CWL types, optionally followed by "?" |
| `apkg-pro:PersonShape` | `apkg-pro:Person` | D19 | `foaf:name` and one Email exactly 1 |
| `apkg-pro:SpatialCoverageShape` | `apkg-pro:SpatialCoverage` | D20 | one Geo (`geo:hasGeometry`); `geoClass` fixed to "schema:GeoShape" |
| `apkg-pro:SecretShape` | `apkg-pro:Secret` | D21 | at least one `secretInputID` |

## Design choices

- **Open shapes.** No shape is `sh:closed`: a node may carry properties that the profile does not mention, and only the declared ones are checked. This is the usual choice for application profiles, and it lets a Process pass the Record shape although it has extra properties.
- **No inference needed.** The shapes are meant to be run without a reasoner:
  - `apkg-pro:ProcessShape` applies `apkg-rec:RecordShape` with `sh:node`, so a Process is checked as a Record even if the data does not state `rdf:type apkg-rec:Record`.
  - The producer of a Process counts as a source organisation through `sh:alternativePath` (`hasSourceOrganisation` or `hasProducerOrganisation`), instead of relying on `rdfs:subPropertyOf`.
- **Node types must be explicit.** `sh:class` checks the `rdf:type` of related nodes (for example a link must be typed `apkg-rec:Link`). `SCRIPTS/json2rdf.py` writes these types.
- **v1 data as literals.** Following the profile, values that v1 data holds as strings stay literals (`xsd:string` or `xsd:anyURI`), and value lists are checked with `sh:in`, `sh:pattern` or `sh:hasValue`. The notes "In v3 it becomes ..." in the tables say how each one will change.
- **Link relations.** `rel` accepts the 134 relation types of the IANA Link Relation Types registry (last updated 2026-06-12), plus "root" (used by OGC API - Records, not registered at IANA), or any URI (extension relation types, RFC 8288).
- **Fixed values.** Two constants that are not in the v1 JSON are enforced with `sh:hasValue`: the CWL media type ("application/cwl+yaml") and the legacy geo class ("schema:GeoShape").

## Known limits

- The SHACL-SPARQL constraint of the Language shape needs a processor with SHACL-SPARQL support (pyshacl has it).
- `xsd:anyURI` and the patterns check the syntax only: they do not check that a URL resolves or that a code exists in its registry (e.g. an ISO 3166 country code or an EDAM format).
- Link templates, themes, contacts, languages and external identifiers are not used in v1 data; their shapes are kept for conformance with OGC API - Records and have only been tested with synthetic data.

## Related folders

- `terms/`: the ontology modules (`apkg-rec-v2.ttl`, `apkg-pro-v2.ttl`) and the declarations module (`apkg-declarations-v2.ttl`).
- `examples/`: example records (Turtle, and JSON-LD when generated with `--format jsonld` or `both`), valid against these shapes.
- `SCRIPTS/`: conversion from JSON (`json2rdf.py`) and validation (`validate.py`).
