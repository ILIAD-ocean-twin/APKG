# APKG Linked Data Application Profile

[<- main](README.md)

## Core properties related to the LinkTemplate Class 

- Table A.3.1


| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| uriTemplate | A URI template (RFC 6570) whose variables are substituted at runtime before resolving the link | 🟢 hydra:template | 🔴 apkg-rec:LinkTemplate | 🟢hydra:Rfc6570Template | 1 | 1 | SES: RFC 6570 | Domain of hydra:template is hydra:IriTemplate, consistent with apkg-rec:LinkTemplate rdfs:subClassOf hydra:IriTemplate |
| variables | Description of the variables used in the URI template | 🟢 hydra:mapping | 🔴 apkg-rec:LinkTemplate | 🟢hydra:IriTemplateMapping | 0-1 | 0-M |  | One mapping per variable (hydra:variable, hydra:required, dct:description). Full JSON Schema of each variable (type, enum, …) in Version 2 (TODO) |
| varBase | A base path to retrieve semantic information about the variables used in the URI template | 🔴 apkg-rec:varBase | 🔴 apkg-rec:LinkTemplate | xsd:anyURI | 0-1 | 0-1 |  | owl:DatatypeProperty. Literal, as OGC allows relative paths. No existing term |
| rel | The type of relation of this link template | 🟢 dct:type | 🔴 apkg-rec:LinkTemplate | IRI | 1 | 1 | ianaRelation | DCMI range of dct:type is rdfs:Class: IANA relation terms are inferred as classes of links |
| type | Media type of the resource pointed to by the link template | 🟢 dct:format | 🔴 apkg-rec:LinkTemplate | 🟢 dct:MediaType | 0-1 | 0-1 | ianaMediaType |  |
| hreflang | A hint indicating what the language of the result of dereferencing the link should be. | 🟢 dct:language | 🔴 apkg-rec:LinkTemplate | 🔴 apkg-rec:Language | 0-1 | 0-1 |  | apkg-rec:Language rdfs:subClassOf dct:LinguisticSystem |
| title | A title of the link template | 🟢 dct:title | 🔴 apkg-rec:LinkTemplate | rdf:langString | 0-1 | 0-1 |  |  |
| length | The size in bytes of the target resource | 🟢 dcat:byteSize | 🔴 apkg-rec:LinkTemplate | xsd:nonNegativeInteger | 0-1 | 0-1 |  | DCAT domain of dcat:byteSize is dcat:Distribution: apkg-rec:LinkTemplate is inferred as dcat:Distribution |
| profile | One or more identifiers that provide information about additional semantics (constraints, conventions, extensions), in addition to those defined by the media type, that are associated with the target resource. | 🟢 dct:conformsTo | 🔴 apkg-rec:LinkTemplate | IRI (prof:Profile) | 0-M | 0-M |  | prof:Profile rdfs:subClassOf dct:Standard |
| created | Date of creation of the resource pointed to by the link template. | 🟢 dct:created | 🔴 apkg-rec:LinkTemplate | xsd:dateTimeStamp | 0-1 | 0-1 |  | RFC 3339 date-time requires a time offset |
| updated | Most recent date on which the resource pointed to by the link template was changed. | 🟢 dct:modified | 🔴 apkg-rec:LinkTemplate | xsd:dateTimeStamp | 0-1 | 0-1 |  | RFC 3339 date-time requires a time offset |