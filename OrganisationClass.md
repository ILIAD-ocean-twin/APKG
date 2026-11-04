# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Theme Class 

- Table B.3.2

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| name | Name of the Organisation | (?) | 🔴 apkg-rec:Organisation | xsd:string | 1 | 1 | | |
| url | URL of the webpage of Organisation | (?) | 🔴 apkg-rec:Organisation | xsd:anyURI | 1 | 1 | |                                   
| address | Postal address of the Organisation | (?) | 🔴 apkg-rec:Organisation | 🔴 apkg-rec:PostalAddress | 1 | 1 | | (?) Should we use the 🔴 apkg-.rec:Address and make the addressCountry mandatory? |  