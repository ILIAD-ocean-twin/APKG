# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the SpatialCoverage Class 

- Table B.3.2

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| geo | | 🔴apkg-rec:hasGeo | apkg-rec:SpatialCoverage | 🔴apkg-rec:Geo    | 1 | 1 | |  | 
| class | The scheme structure of the geo element | 🔴apkg-rec:GeoScheme | 🔴apkg-rec:SpatialCoverage | xsd:string | 1 | 1 | In this profile the value is always "schema:GeoShape". | Use SHACL to validate. |
