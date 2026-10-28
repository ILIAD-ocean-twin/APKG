

# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Parameter Class 

- Table

| OGC Property | Description | Vocabulary Term | Domain | Range |  Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|-----|------|
||  The unique identifier for the object   | apkg-rec:parameterID |apkg-rec:Parameter   | xsd:string  |  1-1    |    |  | rdfs:subClassOf dct:identifier  |
| | The type of data      |            dct:type                | xsd:string                               | apkg-rec:Parameter                                  | 1-1         |  |       | ["null","boolean", "int", "long", "float", "double", "string", "File", "Directory" ] --> CWL TYpes make a sKOS!
|| A short, human-readable label    |                            |         apkg-rec:Parameter  |     xsd:string                          | 0-1         |                                 |                                                             |
| |A documentation string        | |apkg-rec:Parameter                           | xsd:string                                     | 0-1         |                                 |                                                             |
| |The file format that will be assigned to the output File object     | | apkg-re:Parameter                         | xsd:string                                                    | 0-1         |                                 | Use only when the parameter type is "File" is a CWLtype=File                |