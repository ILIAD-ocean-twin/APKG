# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Organisation Class 

- Table B.3.2

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| name | Name of the Organisation | 🟢 rov:legalName | 🔴 apkg-rec:Organisation | xsd:string | 1 | 1 | | |
| url | URL of the webpage of Organisation | 🟢 foaf:homepage | 🔴 apkg-rec:Organisation | 🟢 foaf:Document | 1 | 1 | |                                   
| address | Address of the Organisation | 🟢 vcard:hasAddress| 🔴 apkg-rec:Organisation | 🔴 apkg-rec:Address | 1 | 1 |  |                                                             |  