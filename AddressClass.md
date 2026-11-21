# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Address Class

- Table B2

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| street_address | Address lines for the location. | 🟢 vcard:street-address | 🔴 apkg-rec:Address | xsd:string | 0-M | 0-M | | Multiple RDF values are unordered, so the order of the address lines is not kept. |
| address_locality | City for the location. | 🟢 vcard:locality | 🔴 apkg-rec:Address | xsd:string | 0-M | 0-M | | |
| administrative_area | State or province of the location. | 🟢 vcard:region | 🔴 apkg-rec:Address | xsd:string | 0-1 | 0-1 | | |
| postal_code | ZIP or other postal code. | 🟢 vcard:postal-code | 🔴 apkg-rec:Address | xsd:string | 0-1 | 0-1 | | |
| address_country | Country of the address. | 🟢 vcard:country-name | 🔴 apkg-rec:Address | xsd:string | 0-1 | 0-1 | ISO 3166-1 alpha-2 (SES) | v1 data holds a two-letter country code (e.g. "PT"), stored with vcard:country-name for lack of a better OWL term (vcard:country-name is meant for the country name). Validated with sh:pattern "^[A-Z]{2}$". |
| roles | The type of address. | 🔴 apkg-rec:contactPointType | 🔴 apkg-rec:Address | xsd:string | 0-M | 0-M | enum: private, work, billing, delivery | owl:DatatypeProperty, shared with apkg-rec:Phone and apkg-rec:Email (domain: union of the three). Plain string values because of v1 data; validated with sh:in. In v3, private and work can be expressed with the vCard types vcard:Home and vcard:Work (as rdf:type of the Address node); billing and delivery have no vCard equivalent. |

[<- main](README.md)
