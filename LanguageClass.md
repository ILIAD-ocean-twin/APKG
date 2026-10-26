# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Language Class 

- Table B.3.2

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| code | The language tag as per RFC-5646. | 🔴 (?) | apkg-rec:Language| xsd:string | 1 |1| |
| name | The untranslated name of the language. | 🔴 (?)  | apkg-rec:Language | xsd:string | 0-1 |0-1| | 
| alternate |  The name of the language in another well-understood language, usually English. | 🟢 (?) | apkg-rec:Language | xsd:string |0-1 | 0-1 |
| dir | The direction for text in this language. The default, `ltr` (left-to-right), represents the most common situation. However, care should be taken to set the value of `dir` appropriately if the language direction is not `ltr`. Other values supported are `rtl` (right-to-left), `ttb` (top-to-bottom), and `btt` (bottom-to-top). | 🔴 (?)  | apkg-rec:Language | xsd:string | 0-1 |0-1| |  enum: ltr; rtl; ttb; btt; default: ltr

