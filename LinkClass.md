# APKG Linked Data Application Profile

[<- main](README.md)

## Core properties related to the Link Class

- Table A.2.1

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| href         | A URL related to this record | 🟢  foaf:page | apkg-rec:Link | foaf:Document | 0-M | 0-M |  |   |
| rel          | The type of relation of this record | 🟢  dct:relation | apkg-rec:Link | xsd:anyURI | 1 | 1 | ianaRelation |  |
| type | Media type of the relation of this record | 🟢 dct:format | apkg-rec:Link | dct:MediaType| 0-1  | 0-1  | ianaMediaType | |
| hreflang     | A hint indicating what the language of the result of dereferencing the link should be. | 🔴 apkg-rec:hasLanguage  | apkg-rec:Link | apkg-rec:Language | 0-1 | 0-1 | ISO639-2 |   rdfs:subPropertyOf dct:language; It migth require to match with https://schemas.opengis.net/ogcapi/records/part1/1.0/openapi/schemas/language.yaml in Version 2 (TODO) |
| title        | A title of the related link | 🟢  dct:title | apkg-rec:Link | xsd:string | 0-1 | 0-1 |     |    |
| length     |  | 🟢   | apkg-rec:Link |  | 0-1 | 0-1 |  |  |
| profile     | One or more identifiers that provide information about additional semantics (constraints, conventions, extensions), in addition to those defined by the media type, that are associated with the target resource. | 🟢   | apkg-rec:Link | xsd:string | 0-1 | 0-1 |  |  |
| created     | Date of creation of the resource pointed to by the link. | 🟢   | apkg-rec:Link |  | 0-1 | 0-1 |  | date-time |
| updated     | Most recent date on which the resource pointed to by the link was changed. | 🟢   | apkg-rec:Link |  | 0-1 | 0-1 |  | date-time |
