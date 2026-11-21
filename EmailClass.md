# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Email Class

- Table B5

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| value | The email address itself. | 🟢 vcard:value | 🔴 apkg-rec:Email | xsd:string | 1 | 1 | RFC 5322 addr-spec (SES) | vCard data property for values that need property parameters. Plain string because of v1 data (e.g. "maria@exemplo.pt", without mailto:). Validated with sh:pattern "^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$". In v3 it becomes vcard:hasValue with a mailto: IRI (RFC 6068). |
| roles | The type of email. | 🔴 apkg-rec:contactPointType | 🔴 apkg-rec:Email | xsd:string | 0-M | 0-M | enum: private, work | owl:DatatypeProperty, shared with apkg-rec:Address and apkg-rec:Phone (domain: union of the three). Plain string values because of v1 data; validated with sh:in. In v3, private and work can be expressed with the vCard types vcard:Home and vcard:Work (as rdf:type of the Email node). |

[<- main](README.md)
