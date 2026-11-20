# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Phone Class 
<!--
- Table B11

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| value | The value is the phone number itself. | 🟢 vcard:hasValue | 🔴apkg-rec:Phone | xsd:string | 1 | 1 | E.164 | sh:pattern "^\\+[1-9]{1}[0-9]{3,14}$" |
| role | The type of phone number. | 🔴 apkg-rec:role | 🔴apkg-rec:Phone | xsd:string | 0-M | 0-M | | enum: private, work.|
-->

- Table B12

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| value | The value is the phone number itself. | 🟢 vcard:value | 🔴 apkg-rec:Phone | xsd:string | 1 | 1 | E.164 (SES) | vCard data property for values that need property parameters. Validated with sh:pattern "^\\+[1-9][0-9]{3,14}$". In v3 it becomes vcard:hasValue with a tel: IRI (RFC 3966). |
| roles | The type of phone number. | 🔴 apkg-rec:contactPointType | 🔴 apkg-rec:Phone | xsd:string | 0-M | 0-M | enum: private, work | owl:DatatypeProperty, shared with apkg-rec:Address and apkg-rec:Email (domain: union of the three). Plain string values because of v1 data; validated with sh:in. In v3, private and work can be expressed with the vCard types vcard:Home and vcard:Work (as rdf:type of the Phone node). |