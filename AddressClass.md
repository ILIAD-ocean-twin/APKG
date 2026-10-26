# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Address Class 

- Table B.3.2

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
|  |  | 🟢 |  | | | | | |
|  |  | 🔴 |  | | | | | |
| deliveryPoint | Address lines for the location. | 🔴 | 🔴apkg-rec:Address | (?) xsd:string | 0-M | 0-M | | |
| city | City for the location. | 🔴 | 🔴apkg-rec:Address | (?) | 0-M | 0-M | | |
| administrativeArea | State or province of the location. | 🔴 | 🔴apkg-rec:Address | (?) | 0-1 | 0-1 | | |
| postalCode | ZIP or other postal code. | 🔴 | 🔴apkg-rec:Address | (?) | 0-1 | 0-1 | | |
| country | Country of the physical address.   | 🔴 | 🔴apkg-rec:Address | (?) | 0-1 | 0-1 | | ISO 3166-1 is recommended. |
| roles | The type of address (e.g. office, home, etc.).   | 🔴 | 🔴apkg-rec:Address | (?) xsd:string | 0-M | 0-M | | (?) List of terms (e.g. office, home, etc.). |
