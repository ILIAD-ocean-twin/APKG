# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Person Class 


- Table D19

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| name | Name of the Person. | 🟢 foaf:name | 🔴 apkg-pro:Person | xsd:string | 1 | 1 | |  |
| email | Email address of the Person. | 🟢 vcard:hasEmail | 🔴 apkg-pro:Person | 🔴 apkg-rec:Email | 1 | 1 | | Same pattern as the Contact class: the address is held by vcard:value on the apkg-rec:Email node (Table B5). |

