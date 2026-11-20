

# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Parameter Class 
<!--
- Table D17

| OGC Property | Description | Vocabulary Term | Domain | Range |  Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|-----|------|
|id|  The unique identifier for the object   | 🟢dct:identifier |🔴apkg-rec:Parameter   | xsd:string  |  1    |    |    |
|type | The type of data     |   🟢dct:type    |   🔴apkg-rec:Parameter |  xsd:string   | 1   | enum: null, boolean, int, long, float, double, string, File, Directory  | 
| doc |A documentation string        | 🟢 dcterms:description |🔴apkg-rec:Parameter     | xsd:string  | 0-1         |      |
-->

- Table D18

| CWL Property | Description | Vocabulary Term | Domain | Range | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|------------------|---------|------|
| id | The unique identifier for the object. | 🟢 dct:identifier | 🔴 apkg-rec:Parameter | xsd:string | 1 | | |
| type | The type of data. | 🔴 apkg-rec:parameterType | 🔴 apkg-rec:Parameter | xsd:string | 1 | enum: null, boolean, int, long, float, double, string, File, Directory | owl:DatatypeProperty. Validated with sh:in. Not dct:type, whose range rdfs:Class would turn the literal values into classes. Composite CWL types (array, record, enum) and optional types are not used in v1 data. In v3 it follows CWL (sld:type, with XSD datatypes for primitive types and cwl:File / cwl:Directory as classes). |
| doc | A documentation string. | 🟢 dct:description | 🔴 apkg-rec:Parameter | xsd:string | 0-1 | | |
