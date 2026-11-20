# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Format Class 

- Table B6

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| name | The name of the format the resource that the record describes. | 🟢 dct:title | 🔴 apkg-rec:Format | xsd:string | 0-1 | 0-1 |  |  |
| mediatype | The media type of the format the resource that the record describes. |🔴 apkg-rec:mediaType | 🔴 apkg-rec:Format | xsd:string | 0-1 | 0-1 | ianaMediaType | In v3, `dcat:mediaType` is passed with IANA IRIs (`dct:MediaType`) |
| identifier | The identifier of the contact. | 🟢dct:identifier| 🔴apkg-rec:Contact| xsd:string | 0-1 |0-1| ||
| name | The name of the responsible person. | 🟢  vcard:fn |🔴 apkg-rec:Contact| xsd:string | 0-1 |0-1| | 
| position |  The name of the role or position of the responsible person taken from the organization's formal organizational hierarchy or chart. | 🟢 vcard:title |🔴 apkg-rec:Contact| xsd:string |0-1 | 0-1 |
| organisation | Organization/affiliation of the contact. | 🟢 vcard:organization-name | 🔴apkg-rec:Contact| xsd:string | 0-1 |0-1| | |
| logo | Graphic identifying a contact. | 🔴 apkg-rec:hasLogo | 🔴apkg-rec:Contact | 🔴apkg-rec:Link | 0-1|0-1| |The 'rel' property of the  Link Class must be 'icon', and the 'type' property a mime type.

