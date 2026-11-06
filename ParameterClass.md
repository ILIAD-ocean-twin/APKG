

# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Parameter Class 

- Table D17

| OGC Property | Description | Vocabulary Term | Domain | Range |  Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|-----|------|
|id|  The unique identifier for the object   | 🟢dct:identifier |🔴apkg-rec:Parameter   | xsd:string  |  1    |    |    |
|type | The type of data     |   🟢dct:type    |   🔴apkg-rec:Parameter |  xsd:string   | 1   | enum: null, boolean, int, long, float, double, string, File, Directory  | 
| doc |A documentation string        | 🟢 dcterms:description |🔴apkg-rec:Parameter     | xsd:string  | 0-1         |      |
