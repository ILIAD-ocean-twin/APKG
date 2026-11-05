

# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Parameter Class 

- Table D17

| OGC Property | Description | Vocabulary Term | Domain | Range |  Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|-----|------|
||  The unique identifier for the object   | 🔴 apkg-rec:parameterID |🔴apkg-rec:Parameter   | xsd:string  |  1    |    |   rdfs:seeAlso dct:identifier  |
| | The type of data     |            🟢dct:type    | xsd:string    | 🔴apkg-rec:Parameter   | 1   | enum: null, boolean, int, long, float, double, string, File, Directory  | 
|| A short, human-readable label    |  🟢 rdfs:label   |  🔴 apkg-rec:Parameter  |     xsd:string   | 0-1   |  |    |
| |A documentation string        | 🟢 rdfs:comment |🔴apkg-rec:Parameter     | xsd:string  | 0-1         |      |                                                             |
| |The file format that will be assigned to the output File object     | 🟢 edam:has_format	 | 🔴apkg-re:Parameter      | IRI  | 0-1         |   | Use only when the parameter type is "File" is a CWLtype=File  |