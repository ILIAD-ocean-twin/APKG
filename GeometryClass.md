# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Geometry Class 

- Table B7

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| type | The type of the object  |🟢 geojson:type | apkg-rec:Geometry | IRI | 1 | 1 | geojson concept scheme | O concept scheme tem de ser defnido em skos.
| coordinates | The coordinates of the  object |🟢 geojson:coordinates | apkg-rec:Geometry | xsd:string | 1-M | 1-M |
