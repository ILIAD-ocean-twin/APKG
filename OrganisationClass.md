# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Organisation Class 

- Table D16

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| name | Name of the Organisation | 🟢 rov:legalName | 🔴 apkg-rec:Organisation | xsd:string | 1 | 1 | | |
| url | URL of the webpage of Organisation | 🟢 foaf:homepage | 🔴 apkg-rec:Organisation | 🟢 foaf:Document | 1 | 1 | |                                   
| address | Postal address of the Organisation | 🟢 vcard:hasAddress| 🔴 apkg-rec:Organisation | 🔴 apkg-rec:Address | 1 | 1 |  |                                                             |  

- Table D16

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| name | Name of the Organisation. | 🟢 skos:prefLabel | 🔴 apkg-rec:Organisation | xsd:string | 1 | 1 | | The W3C ORG ontology recommends skos:prefLabel for the organisation names. |
| url | URL of the webpage of the Organisation. | 🔴 apkg-rec:homepage | 🔴 apkg-rec:Organisation | xsd:anyURI | 1 | 1 | RFC 3986 (SES) | owl:DatatypeProperty. Typed literal (xsd:anyURI), not an IRI node, because of v1 data. In v3 it becomes foaf:homepage (foaf:Document); foaf:homepage is inverse functional, so organisations sharing a homepage are inferred to be the same individual. |
| address | Postal address of the Organisation. | 🟢 vcard:hasAddress | 🔴 apkg-rec:Organisation | 🔴 apkg-rec:Address | 1 | 1 | | Same property as in the Contact class. |