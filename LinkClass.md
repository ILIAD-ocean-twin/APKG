# APKG Linked Data Application Profile

[<- main](README.md)

## Core properties related to the Link Class

- Table A.2.1

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| href         | A URL related to this record | 🟢  foaf:page | 🔴apkg-rec:Link |🟢 foaf:Document | 1|1 |  |   |
| rel          | The type of relation of this record | 🟢  dct:type | 🔴apkg-rec:Link | IRI | 1 | 1 | ianaRelation |  |
| type | Media type of the relation of this record | 🟢 dct:format | 🔴apkg-rec:Link | 🟢 dct:MediaType| 0-1  | 0-1  | ianaMediaType | |
| hreflang     | A hint indicating what the language of the result of dereferencing the link should be. | 🟢 dct:language |🔴 apkg-rec:Link | 🔴 apkg-rec:Language | 0-1 | 0-1 | ISO639-2 |    It migth require to match with https://schemas.opengis.net/ogcapi/records/part1/1.0/openapi/schemas/language.yaml in Version 2 (TODO) |
| title        | A title of the related link | 🟢  dct:title |🔴 apkg-rec:Link | rdf:langString | 0-1 | 0-1 |     |    |
| length     | The size in bytes of the target resource | 🟢 dcat:byteSize  | 🔴apkg-rec:Link | xsd:nonNegativeInteger | 0-1 | 0-1 |  | DCAT domain of dcat:byteSize is dcat:Distribution: apkg-rec:Link is inferred as dcat:Distribution.” |
| profile     | One or more identifiers that provide information about additional semantics (constraints, conventions, extensions), in addition to those defined by the media type, that are associated with the target resource. | 🟢 dct:conformsTo |🔴 apkg-rec:Link | IRI| 0-M | 0-M | QUAL PODIA SER prof:Profile? | 
| created     | Date of creation of the resource pointed to by the link. | 🟢 dct:created     |🔴 apkg-rec:Link | xsd:dateTime | 0-1 | 0-1 |  | |
| updated     | Most recent date on which the resource pointed to by the link was changed. | 🟢 dct:modified  | 🔴 apkg-rec:Link | xsd:dateTime  | 0-1 | 0-1 |  | |

[<- main](README.md)