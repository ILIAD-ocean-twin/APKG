# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Email Class 

- Table B5

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| value | The value is the email number itself. | 🟢 vcard:hasEmail  | 🔴apkg-rec:Email | xsd:string | 1 | 1 |  | a standard URI scheme (RFC 6068). In SHACL you validate with sh:nodeKind sh:IRI plus sh:pattern "^mailto:". |
| roles | The type of email. | 🔴apkg-rec:role | 🔴apkg-rec:Email |xsd:string | 0-M | 0-M | enum: private, work| |
