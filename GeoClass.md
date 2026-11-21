# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Geo Class 

- Table D16


| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| box | The bounding box (two lat/long pairs: lower-left and upper-right corners). | 🔴 apkg-pro:box | 🔴 apkg-pro:Geo | xsd:string | 1 | 1 | schema.org box syntax (SES) | owl:DatatypeProperty. Not schema:box (rdf:Property only). Validated with sh:pattern "^-?\\d+(\\.\\d+)?( -?\\d+(\\.\\d+)?){3}$" (lat/long ranges need a sh:sparql constraint). apkg-pro:Geo rdfs:subClassOf geo:Geometry. Dropped in v3: replaced by apkg-rec:Geometry with geo:asWKT or geo:asGeoJSON; conversion must swap to lon-lat order. |