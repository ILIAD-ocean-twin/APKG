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
| roles | The type of address (e.g. office, home, etc.).   | 🔴 apkg-rec:addressRole | 🔴apkg-rec:Address | xsd:string | 0-M | 0-M | | List of terms (e.g. office, home, etc.). vcard:role describes the function of a person (e.g. “Professora Auxiliar”). It does not describe the type of an address. In vCard, the address type (“office” or “home”) is modelled by typing the address with classes: ex:addr1 a apkg-rec:Address, vcard:Work .   -->   office ; ex:addr2 a apkg-rec:Address, vcard:Home .  --> home|
