# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Contact Class 

- Table B.3.2

[!NOTE]
Note Constraint: at least one of name or organization is required.

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| identifier | The identifier of the contact. | 🔴apkg-rec:contactIdentifier | apkg-rec:Contact| xsd:string | 0-1 |0-1| |rdfs:subPropertyOf dct:identifier
| name | The name of the responsible person. | 🔴 apkg-rec:contactName | apkg-rec:Contact| xsd:string | 0-1 |0-1| | rdfs:subPropertyOf foaf:name
| position |  The name of the role or position of the responsible person taken from the organization's formal organizational hierarchy or chart. | 🟢 org:holds | apkg-rec:Contact| xsd:string |0-1 | 0-1 |
| organization | Organization/affiliation of the contact. | 🔴 apkg-rec:contactOrganisationName | apkg-rec:Contact| xsd:string | 0-1 |0-1| | rdfs:subPropertyOf foaf:name
| logo | Graphic identifying a contact. | 🔴 apkg-rec:hasLogo | apkg-rec:Contact | 🔴 apkg-rec:[Link](./LinkClass.md) | 0-1|0-1| |The 'rel' property of the  Link Class must be 'icon', and the 'type' property a mime type.|
| phones | Telephone numbers at which contact can be made. | 🟢 vcard:hasTelephone |  apkg-rec:Contact  | 🔴apkg-rec:[Phone](./PhoneClass.md) | 0-M| 0-M|
| emails | Email addresses at which contact can be made. | 🟢 vcard:hasEmail | apkg-rec:Contact  | 🔴 apkg-rec:[Email](./EmailClass.md) | 0-M| 0-M|
| addresses | Email addresses at which contact can be made. | 🟢 vcard:hasAddress | apkg-rec:Contact  | 🔴apkg-rec:[Address](./AddressClass.md) | 0-M| 0-M|
| links | On-line information about the contact. | 🔴apkg-rec:hasLink | apkg-rec:Contact  | 🔴apkg-rec:[Link](./LinkClass.md) | 0-M| 0-M|
| hoursOfService | Time period when the contact can be contacted. | 🔴apkg-rec:hoursOfService | apkg-rec:Contact | xsd:string  | 0-1| 0-1|
| contactInstructions | Supplemental instructions on how or when to contact the responsible party. | 🔴 apkg-rec:contactInstructions(?) | apkg-rec:Contact  | xsd:string| 0-1| 0-1|
|  roles | The list of duties, job functions or permissions assigned by the system and associated with the context of this member. | vcard:role | apkg-rec:Contact  | xsd:string | 0-M | 0-M | | VCARD Individuals |

