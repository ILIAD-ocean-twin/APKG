# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Phone Class 

- Table B.3.2

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| value | The value is the phone number itself. | 🟢 | 🔴apkg-rec:Phone | (?) xsd:string | 1 | 1 | | pattern: "^\\+[1-9]{1}[0-9]{3,14}$" |
| role | The type of phone number (e.g. home, work, fax, etc.). | vcard:role | 🔴apkg-rec:Phone | (?) xsd:string | 0-M | 0-M | | list of terms (e.g. home, work, fax, etc.).|
