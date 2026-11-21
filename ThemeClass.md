# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Theme Class 

- Table B13

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| concepts | The classification of the KOS defined on theme | 🔴 apkg-rec:hasConcept | 🔴 apkg-rec:Theme | 🔴 apkg-rec:Concept | 1-M | 1-M |  | owl:ObjectProperty. apkg-rec:Concept rdfs:subClassOf skos:Concept. Listing 22 and Listing 38 at https://docs.ogc.org/is/20-004r1/20-004r1.html show divergent uses: object with id and url vs list of strings |
| scheme | The KOS scheme of the concepts in the specific theme | 🟢 skos:inScheme | 🔴 apkg-rec:Theme | xsd:anyURI | 1 | 1 |  |  |


- Table B13

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| concepts | The concepts of the theme, drawn from the knowledge organisation system (KOS) given in scheme. | 🔴 apkg-rec:hasConcept | 🔴 apkg-rec:Theme | 🔴 apkg-rec:Concept | 1-M | 1-M | | owl:ObjectProperty. apkg-rec:Theme rdfs:subClassOf bf:Topic; apkg-rec:Concept rdfs:subClassOf skos:Concept (Table B3). OGC examples diverge (Listing 22: objects with id and url; Listing 38: list of strings, https://docs.ogc.org/is/20-004r1/20-004r1.html); strings are mapped to a Concept node with that id. |
| scheme | The knowledge organisation system (KOS) of the concepts of the theme. | 🔴 apkg-rec:scheme | 🔴 apkg-rec:Theme | xsd:anyURI | 1 | 1 | RFC 3986 (SES) | owl:DatatypeProperty. Typed literal (xsd:anyURI), not an IRI node, because of v1 data. Not skos:inScheme, which links a concept (not a theme) to a skos:ConceptScheme IRI. In v3 it becomes skos:inScheme on each Concept. |