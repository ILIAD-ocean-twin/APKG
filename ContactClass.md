# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Contact Class 

- Table B.3.2

[!NOTE]
Note Constraint: at least one of name or organization is required.

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| identifier | The identifier of the contact. | 🟢 dct:identifier | 🔴 apkg-rec:Contact | xsd:string | 0-1 | 0-1 |  |  |
| name | The name of the responsible person. | 🟢 vcard:fn | 🔴 apkg-rec:Contact | xsd:string | 0-1 | 0-1 |  |  |
| position | The name of the role or position of the responsible person taken from the organization's formal organizational hierarchy or chart. | 🟢 vcard:title | 🔴 apkg-rec:Contact | xsd:string | 0-1 | 0-1 |  | vCard TITLE = position or job of the contact |
| organisation | Organization/affiliation of the contact. | 🟢 vcard:organization-name | 🔴 apkg-rec:Contact | xsd:string | 0-1 | 0-1 |  | vCard ORG = organisation the contact belongs to |
| logo | Graphic identifying a contact. | 🟢 vcard:hasLogo | 🔴 apkg-rec:Contact | 🔴 apkg-rec:[Link](./LinkClass.md) | 0-1 | 0-1 |  | The rel property of the Link must be 'icon' and the type property a media type |
| phones | Telephone numbers at which contact can be made. | 🟢 vcard:hasTelephone | 🔴 apkg-rec:Contact  | 🔴apkg-rec:[Phone](./PhoneClass.md) | 0-M| 0-M|
| emails | Email addresses at which contact can be made. | 🟢 vcard:hasEmail | apkg-rec:Contact  | 🔴 apkg-rec:[Email](./EmailClass.md) | 0-M| 0-M|
| addresses | Postal addresses at which contact can be made. | 🟢 vcard:hasAddress | 🔴apkg-rec:Contact  | 🔴apkg-rec:[Address](./AddressClass.md) | 0-M| 0-M|
| links | On-line information about the contact. | 🔴apkg-rec:hasLink | apkg-rec:Contact  | 🔴apkg-rec:[Link](./LinkClass.md) | 0-M| 0-M|
| hoursOfService | Time period when the contact can be contacted. | 🔴apkg-rec:hoursOfService |🔴 apkg-rec:Contact |🟢 time:Interval  | 0-1| 0-1|
| contactInstructions | Supplemental instructions on how or when to contact the responsible party. | 🔴 apkg-rec:contactInstructions | 🔴apkg-rec:Contact  | xsd:string| 0-1| 0-1|
| roles | The list of duties, job functions or permissions assigned by the system and associated with the context of this member. | 🟢 vcard:role |🔴 apkg-rec:Contact  | xsd:string | 0-M | 0-M | enum: resourceProvider, custodian, owner, user, distributor, originator, pointOfContact, principalInvestigator, processor, publisher, author, sponsor, coAuthor, collaborator, editor, mediator, rightsHolder, contributor, funder, stakeholder  | ISO 19115 CI_RoleCode ; https://standards.iso.org/iso/19115/resources/Codelists/ or https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml |

[<- main](README.md)