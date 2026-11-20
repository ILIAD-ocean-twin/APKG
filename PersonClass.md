# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Person Class 


- Table D19

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| name | Name of the Person. | 🟢 foaf:name | 🔴 apkg-rec:Person | xsd:string | 1 | 1 | |  |
| email | Email address of the Person. | 🟢 vcard:hasEmail | 🔴 apkg-rec:Person | 🔴 apkg-rec:Email | 1 | 1 | |The address is in apkg-rec:emailAddress on the apk-rec:Email (Table B5). |

