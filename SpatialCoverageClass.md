# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the SpatialCoverage Class 
<!--

- Table D21

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| geo | | 🔴apkg-rec:hasGeo | 🔴apkg-rec:SpatialCoverage | 🔴apkg-rec:Geometry    | 1 | 1 | |  | 
| class | The scheme structure of the geo element | 🔴apkg-rec:GeoScheme | 🔴apkg-rec:SpatialCoverage | xsd:string | 1 | 1 | In this profile the value is always "schema:GeoShape". | Use SHACL to validate. |
-->


- Table D21

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| geo | The bounding box of the spatial coverage. | 🟢 geo:hasGeometry | 🔴 apkg-rec:SpatialCoverage | 🔴 apkg-rec:Geo | 1 | 1 | | GeoSPARQL owl:ObjectProperty; domain geo:Feature, so apkg-rec:SpatialCoverage is inferred as geo:Feature. Range geo:Geometry, consistent with apkg-rec:Geo rdfs:subClassOf geo:Geometry. Same property as the Record geometry (Table A.1.2), with a different range |
| class | The scheme structure of the geo element. | 🔴 apkg-rec:geoClass | 🔴 apkg-rec:SpatialCoverage | xsd:string | 1 | 1 | | owl:DatatypeProperty. Legacy field: the value is always "schema:GeoShape" (validated with sh:hasValue). Dropped in v3. |