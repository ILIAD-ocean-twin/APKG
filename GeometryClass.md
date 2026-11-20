# APKG Linked Data Application Profile

[<- main](README.md)
<!-->
## Resource properties related to the Geometry Class 

- Table B7

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| type | The type of the object  |🔴 apkg-rec:geometryType | 🔴 apkg-rec:Geometry | xsd:string | 1 | 1 | RFC 7946 | sh:in ("Point" "MultiPoint" "LineString" "MultiLineString" "Polygon" "MultiPolygon" "GeometryCollection")
| coordinates | The coordinates of the  object |🟢 apkg-rec:coordinates |🔴 apkg-rec:Geometry | xsd:string | 1 | 1 |syntax of RFC 7946.| uma string com o array JSON completo, por exemplo "[[[-8.6,41.1],[-8.5,41.1],…]]"|

-->

## Resource properties related to the Geometry Class

- Table B7

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| box | The bounding box of the geometry (two lat/long pairs). | 🔴 apkg-rec:box | 🔴 apkg-rec:Geometry | xsd:string | 1 | 1 | schema.org box syntax (SES) | owl:DatatypeProperty. sh:pattern "^-?\\d+(\\.\\d+)?( -?\\d+(\\.\\d+)?){3}$".  In v3 it becomes geo:asWKT or geo:asGeoJSON. |
