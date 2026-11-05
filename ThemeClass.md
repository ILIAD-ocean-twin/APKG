# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Theme Class 

- Table B12

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| concepts | The classification of the KOS defined on theme | 🔴 apkg-rec:hasConcept | 🔴 apkg-rec:Theme | 🔴 apkg-rec:Concept | 1-M | 1-M |  | owl:ObjectProperty. apkg-rec:Concept rdfs:subClassOf skos:Concept. Listing 22 and Listing 38 at https://docs.ogc.org/is/20-004r1/20-004r1.html show divergent uses: object with id and url vs list of strings |
| scheme | The KOS scheme of the concepts in the specific theme | 🟢 skos:inScheme | 🔴 apkg-rec:Theme | xsd:anyURI | 1 | 1 |  |  |
