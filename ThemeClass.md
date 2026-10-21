## Resource properties related to the Theme Class 

- Table 3.2

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| concepts |The classification of the KOS defined on theme | 🔴apkg-rec:hasConcept | apkg-rec:Theme |  apkg-rec:Concept    | 0-M |0-M | | Listing 22 and Listing 38 at https://docs.ogc.org/is/20-004r1/20-004r1.html show divergent uses of hasConcept term of the Themes Class. In the first it is a Class with _id_ and _url_ and at the second  a list of xsd:String. | 
| scheme | THe KOS scheme  of the Concepts in the specific theme | skos:inScheme | apkg-rec:Theme | xsd:anyURI | 1 | 1 |
