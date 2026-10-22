# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Contact Class 

- Table B.3.2

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| identifier | The identifier of the contact. | 🔴apkg-rec:contactIdentifier | apkg-rec:Contact| xsd:string | 0-1 |0-1| |rdfs:subPropertyOf dct:identifier
| name | The name of the responsible person. | 🔴 apkg-rec:contactName | apkg-rec:Contact| xsd:string | 0-1 |0-1| | rdfs:subPropertyOf foaf:name
| position |  The name of the role or position of the responsible person taken from the organization's formal organizational hierarchy or chart. | 🟢 org:holds | apkg-rec:Contact| xsd:string |0-1 | 0-1 |
| organisation | Organization/affiliation of the contact. | 🔴 apkg-rec:contactOrganisationName | apkg-rec:Contact| xsd:string | 0-1 |0-1| | rdfs:subPropertyOf foaf:name
| logo | Graphic identifying a contact. | 🔴 apkg-rec:hasLogo | apkg-rec:Contact | apkg-rec:Link | 0-1|0-1| |The 'rel' property of the  Link Class must be 'icon', and the 'type' property a mime type.|
| phones | ....| 🟢 vcard:hasTelephone |  apkg-rec:Contact  | 🔴apkg-rec:Phone | 0-M| 0-M|
| emails |  | 🟢 vcard:hasEmail | apkg-rec:Contact  | 🔴 apkg-rec:Email | 0-M| 0-M|
| addresses |  | 🟢 vcard:hasAddress | apkg-rec:Contact  | 🔴apkg-rec:Address | 0-M| 0-M|
| links |  | 🔴apkg-rec:hasLink | apkg-rec:Contact  | 🔴apkg-rec:Link | 0-M| 0-M|
| hoursOfService |  | 🟢 time:hasTime | apkg-rec:Contact | time:ProperInterval  | 0-M| 0-M|
| contactInstructions |  |  | apkg-rec:Contact  | xsd:string| 0-1| 0-1|
|  roles | | hasRole 