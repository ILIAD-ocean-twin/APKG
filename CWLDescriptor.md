# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Version Class 

- Table

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
|   | THe CWL URL | 🟢 dcat:accessURL |  apkg-rec:CWLDescriptor | xsd:anyURI | 1-1 |
|   | THe CWL format | 🟢 dct:format |  apkg-rec:CWLDescriptor |<https://www.iana.org/assignments/media-types/application/x-cwl> |1-1||Force on SHACL (sh:hasValue <https://www.iana.org/assignments/media-types/application/x-cwl>; sh:minCount 1 ; sh:maxCount 1 ; )|
