# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Parameter Class

- Table D18

| CWL Property | Description | Vocabulary Term | Domain | Range | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|------------------|---------|------|
| id | The unique identifier for the object. | 🟢 dct:identifier | 🔴 apkg-pro:Parameter | xsd:string | 1 | | |
| type | The type of data. | 🔴 apkg-pro:parameterType | 🔴 apkg-pro:Parameter | xsd:string | 1 | enum: null, boolean, int, long, float, double, string, File, Directory (each optionally followed by "[]" and/or "?"; unions joined with "\|") | owl:DatatypeProperty. A trailing "?" marks an optional parameter and "[]" an array in CWL (e.g. "File?", "File[]?"). CWL union types (a JSON list in v1 data, e.g. ["string?", "File?"]) are written as one string joined with "\|" (e.g. "string?\|File?"). Validated with sh:pattern "^(T)(\[\])?\??(\|(T)(\[\])?\??)*$", where T is null\|boolean\|int\|long\|float\|double\|string\|File\|Directory. Not dct:type, whose range rdfs:Class would turn the literal values into classes. Record and enum types are not used in v1 data. In v3 it follows CWL (sld:type, with XSD datatypes for primitive types and cwl:File / cwl:Directory as classes). |
| doc | A documentation string. | 🟢 dct:description | 🔴 apkg-pro:Parameter | xsd:string | 0-1 | | |
| default | The default value of the parameter. | 🔴 apkg-pro:defaultValue | 🔴 apkg-pro:Parameter | xsd:string | 0-1 | | owl:DatatypeProperty. Plain string because v1 data mixes strings and numbers (e.g. "NO", 24.069118741783797). In v3 it can take the XSD datatype given by type. |
| format | The format of the file (for File parameters). | 🔴 apkg-pro:format | 🔴 apkg-pro:Parameter | xsd:string | 0-1 | EDAM format (VES) | owl:DatatypeProperty. Plain string because of v1 data, as a prefixed name (e.g. "edam:format_3464"). In v3 it becomes an object property to the EDAM format IRI (http://edamontology.org/format_3464). |

[<- main](README.md)
