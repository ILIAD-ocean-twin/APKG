# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Format Class

- Table B6

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| name | The name of the format of the resource that the record describes. | 🟢 dct:title | 🔴 apkg-rec:Format | xsd:string | 0-1 | 0-1 | | |
| mediatype | The media type of the format of the resource that the record describes. | 🔴 apkg-rec:mediaType | 🔴 apkg-rec:Format | xsd:string | 0-1 | 0-1 | ianaMediaType | owl:DatatypeProperty, shared with apkg-rec:Link, apkg-rec:LinkTemplate and apkg-pro:CWLDescriptor (domain: union of the four). In v3 it becomes dcat:mediaType with IANA IRIs (dct:MediaType). |

[<- main](README.md)
