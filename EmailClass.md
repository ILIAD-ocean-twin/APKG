# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Email Class 

- Table B.3.2

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| value | The value is the email number itself. | 🟢 | 🔴apkg-rec:Email |(?) xsd:string | 1 | 1 | | email format |
| roles | The type of email (e.g. home, work, etc.). | 🔴 | 🔴apkg-rec:Email |(?) xsd:string | 0-M | 0-M | | (?) List of terms (e.g. home, work, etc.) |
