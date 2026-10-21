[<- main](README.md)

## Core properties related to the Link Class

- Table 2.1

| OGC Property   | Description                                                                              | Vocabulary Term                          | Domain                                   | Range                             | Cardinality OGC | Cardinality APKG | VES | Note |
|----------------|------------------------------------------------------------------------------------------|-------------------------|------------------------------------------|-----------------------------------|-------------|-----|------|--|
| title          | A title of the related link   |          🟢  dct:title             | apkg-rec:Link                            | xsd:string                     | 0-1        | 0-1        |     | |
| href          | A URL related to this record    |          🟢  foaf:page            | apkg-rec:Link        |                      | 0-M         | 0-M         |     |    |
| rel          | The type of relation of this record    |          🟢  dct:relation            | apkg-rec:Link                            | xsd:anyURI | 1 | 1 | ianaRelation    |    |
| type | Media type of the relation of this record | 🟢 dct:format | apkg-rec:Link | dct:MediaType| 0-1  | 0-1  | ianaMediaType | |
