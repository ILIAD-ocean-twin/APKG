# APKG Linked Data Application Profile

[<- main](README.md)

## Core properties related to the LinkTemplate Class 
- Table B11

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| uriTemplate | A URI template (RFC 6570) whose variables are substituted at runtime before resolving the link. | 🟢 hydra:template | 🔴 apkg-rec:LinkTemplate | 🟢 hydra:Rfc6570Template | 1 | 1 | RFC 6570 (SES) | Domain of hydra:template is hydra:IriTemplate, consistent with apkg-rec:LinkTemplate rdfs:subClassOf hydra:IriTemplate. hydra:Rfc6570Template is not in the OWL 2 datatype map; if the reasoner rejects it, use apkg-rec:uriTemplate (xsd:string). |
| variables | Description of the variables used in the URI template. | 🟢 hydra:mapping | 🔴 apkg-rec:LinkTemplate | 🔴 apkg-rec:IriTemplateMapping | 0-1 | 0-M | | The OGC variables object is mapped to one hydra:IriTemplateMapping per variable (hydra:variable, dct:description; Table B8). The JSON Schema of each variable (type, enum, …) has no Hydra equivalent in this version. |
| varBase | A base path to retrieve semantic information about the variables used in the URI template. | 🔴 apkg-rec:varBase | 🔴 apkg-rec:LinkTemplate | xsd:anyURI | 0-1 | 0-1 | RFC 3986 (SES) | owl:DatatypeProperty. Literal, as OGC allows relative paths (xsd:anyURI accepts relative references). No existing term. |
| rel | The type of relation of this link template. | 🔴 apkg-rec:rel | 🔴 apkg-rec:LinkTemplate | xsd:string | 1 | 1 | ianaRelation | owl:DatatypeProperty, shared with apkg-rec:Link (domain: union of Link and LinkTemplate). Validated with sh:in. In v3 it becomes dcat:hadRole with IANA link relation IRIs (dcat:Role). |
| type | Media type of the resource pointed to by the link template. | 🔴 apkg-rec:mediaType | 🔴 apkg-rec:LinkTemplate | xsd:string | 0-1 | 0-1 | ianaMediaType | owl:DatatypeProperty, shared with apkg-rec:Link, apkg-rec:Format and apkg-pro:CWLDescriptor (domain: union of the four). In v3 it becomes dcat:mediaType with IANA IRIs (dct:MediaType). |
| hreflang | A hint indicating what the language of the result of dereferencing the link should be. | 🔴 apkg-rec:hreflang | 🔴 apkg-rec:LinkTemplate | 🔴 apkg-rec:Language | 0-1 | 0-1 | | owl:ObjectProperty, shared with apkg-rec:Link. The language code (RFC 5646) is defined in the Language class (skos:notation, Table B9). |
| title | A title of the link template. | 🟢 dct:title | 🔴 apkg-rec:LinkTemplate | xsd:string | 0-1 | 0-1 | | |
| length | The size in bytes of the target resource. | 🔴 apkg-rec:length | 🔴 apkg-rec:LinkTemplate | xsd:nonNegativeInteger | 0-1 | 0-1 | | owl:DatatypeProperty, shared with apkg-rec:Link. Not dcat:byteSize, to avoid inferring every LinkTemplate as dcat:Distribution. |
| profile | One or more identifiers that provide information about additional semantics (constraints, conventions, extensions), in addition to those defined by the media type, that are associated with the target resource. | 🔴 apkg-rec:profile | 🔴 apkg-rec:LinkTemplate | xsd:anyURI | 0-M | 0-M | RFC 3986 (SES) | owl:DatatypeProperty, shared with apkg-rec:Link. In v3 it becomes dct:conformsTo (dct:Standard). |
| created | Date of creation of the resource pointed to by the link template. | 🟢 dct:created | 🔴 apkg-rec:LinkTemplate | xsd:dateTimeStamp | 0-1 | 0-1 | RFC 3339 (SES) | RFC 3339 date-time requires a time offset. Describes the target, not the LinkTemplate node. |
| updated | Most recent date on which the resource pointed to by the link template was changed. | 🟢 dct:modified | 🔴 apkg-rec:LinkTemplate | xsd:dateTimeStamp | 0-1 | 0-1 | RFC 3339 (SES) | RFC 3339 date-time requires a time offset. Describes the target, not the LinkTemplate node. |

[<- main](README.md)