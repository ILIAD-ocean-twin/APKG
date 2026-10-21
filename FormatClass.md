## Resource properties related to the Format Class 

- Table 3.2

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| name | The name of the format the resource that the record describes. | 🟢 dct:title |apkg-rec:Format   | xsd:string| 0-1| 0-1|
| mediatype | The media of the format the resource that the record describes.| 🟢 dct:format |apkg-rec:Format   | dct:MediaTypeOrExtent| 0-1| 0-1|
| identifier | The identifier of the contact. | 🔴apkg-rec:contactIdentifier | apkg-rec:Contact| xsd:string | 0-1 |0-1| |rdfs:subPropertyOf dct:identifier
| name | The name of the responsible person. | 🔴 apkg-rec:contactName | apkg-rec:Contact| xsd:string | 0-1 |0-1| | rdfs:subPropertyOf foaf:name
| position |  The name of the role or position of the responsible person taken from the organization's formal organizational hierarchy or chart. | 🟢 org:holds | apkg-rec:Contact| xsd:string |0-1 | 0-1 |
| organisation | Organization/affiliation of the contact. | 🔴 apkg-rec:contactOrganisationName | apkg-rec:Contact| xsd:string | 0-1 |0-1| | rdfs:subPropertyOf foaf:name
| logo | Graphic identifying a contact. | 🔴 apkg-rec:hasLogo | apkg-rec:Contact | apkg-rec:Link | 0-1|0-1| |The 'rel' property of the  Link Class must be 'icon', and the 'type' property a mime type.