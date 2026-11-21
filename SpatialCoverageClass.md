# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the SpatialCoverage Class 
- Table D20

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| geo | The bounding box of the spatial coverage. | 🟢 geo:hasGeometry | 🔴 apkg-pro:SpatialCoverage | 🔴 apkg-pro:Geo | 1 | 1 | | GeoSPARQL owl:ObjectProperty; domain geo:Feature, so apkg-pro:SpatialCoverage is inferred as geo:Feature. Range geo:Geometry, consistent with apkg-pro:Geo rdfs:subClassOf geo:Geometry. Same property as the Record geometry (Table A.1.2), with a different range |
| class | The scheme structure of the geo element. | 🔴 apkg-pro:geoClass | 🔴 apkg-pro:SpatialCoverage | xsd:string | 1 | 1 | | owl:DatatypeProperty. Legacy field: the value is always "schema:GeoShape" (validated with sh:hasValue). Dropped in v3. |