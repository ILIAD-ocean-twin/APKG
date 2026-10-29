# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Address Class 

- Table B.3.2

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| deliveryPoint | Address lines for the location. | 🟢vcard:street-address | 🔴apkg-rec:Address | xsd:string | 0-M | 0-M | | |
| city | City for the location. | 🟢vcard:locality | 🔴apkg-rec:Address | xsd:string | 0-M | 0-M | | |
| administrativeArea | State or province of the location. | 🟢vcard:region | 🔴apkg-rec:Address | xsd:string | 0-1 | 0-1 | | |
| postalCode | ZIP or other postal code. | 🟢vcard:postal-code | 🔴apkg-rec:Address | xsd:string  | 0-1 | 0-1 | | |
| country | Country of the physical address.   | 🟢vcard:country-name | 🔴apkg-rec:Address | xsd:string  | 0-1 | 0-1 | | ISO 3166-1 is recommended. |
| roles | The type of address (e.g. office, home, etc.).   | 🔴 apkg-rec:addressType | 🔴apkg-rec:Address | xsd:string | 0-M | 0-M | (?) Possible : JSContact address contexts | List of terms in SKOS.
