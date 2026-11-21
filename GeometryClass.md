# APKG Linked Data Application Profile

[<- main](README.md)


## Resource properties related to the Geometry Class

- Table B7

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| type | The type of the geometry. | 🔴 apkg-rec:geometryType | 🔴 apkg-rec:Geometry | xsd:string | 1 | 1 | enum: Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon, GeometryCollection | owl:DatatypeProperty. GeoJSON geometry types (RFC 7946), validated with sh:in. Not geojson:type, which GeoJSON-LD maps to rdf:type. apkg-rec:Geometry rdfs:subClassOf geo:Geometry. |
| coordinates | The coordinates of the geometry. | 🔴 apkg-rec:coordinates | 🔴 apkg-rec:Geometry | xsd:string | 1 | 1 | RFC 7946 coordinates (SES) | owl:DatatypeProperty. The whole JSON array in a single string (e.g. "[[[-8.6,41.1],[-8.5,41.1],…]]"), because multiple RDF values are unordered and coordinate order defines the geometry. Lon-lat order (RFC 7946). In v3 type and coordinates become a single geo:asGeoJSON literal (geo:geoJSONLiteral), and apkg-rec:Geometry also takes over the role of apkg-pro:Geo. |
