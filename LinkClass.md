# APKG Linked Data Application Profile

[<- main](README.md)

## Core properties related to the Link Class
- Table B10

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| href | A URL related to this record. | 🔴 apkg-rec:href | 🔴 apkg-rec:Link | xsd:anyURI | 1 | 1 | RFC 3986 (SES) | owl:DatatypeProperty. In v3 it becomes dct:relation (target IRI). |
| rel | The type of relation of this record. | 🔴 apkg-rec:rel | 🔴 apkg-rec:Link | xsd:string | 1 | 1 | ianaRelation | owl:DatatypeProperty, shared with apkg-rec:LinkTemplate (domain: union of Link and LinkTemplate). Validated with sh:in. In v3 it becomes dcat:hadRole with IANA link relation IRIs (dcat:Role). |
| type | Media type of the target resource. | 🔴 apkg-rec:mediaType | 🔴 apkg-rec:Link | xsd:string | 0-1 | 0-1 | ianaMediaType | owl:DatatypeProperty, shared with apkg-rec:LinkTemplate, apkg-rec:Format and apkg-pro:CWLDescriptor (domain: union of the four). In v3 it becomes dcat:mediaType with IANA IRIs (dct:MediaType). |
| hreflang | A hint indicating what the language of the result of dereferencing the link should be. | 🔴 apkg-rec:hreflang | 🔴 apkg-rec:Link | 🔴 apkg-rec:Language | 0-1 | 0-1 | | owl:ObjectProperty, shared with apkg-rec:LinkTemplate (domain: union of Link and LinkTemplate). The language code (RFC 5646) is defined in the Language class (skos:notation, Table B9). |
| title | A title of the related link. | 🟢 dct:title | 🔴 apkg-rec:Link | xsd:string | 0-1 | 0-1 | | |
| length | The size in bytes of the target resource. | 🔴 apkg-rec:length | 🔴 apkg-rec:Link | xsd:nonNegativeInteger | 0-1 | 0-1 | | owl:DatatypeProperty, shared with apkg-rec:LinkTemplate (domain: union of Link and LinkTemplate). Not dcat:byteSize, to avoid inferring every Link as dcat:Distribution. |
| profile | One or more identifiers that provide information about additional semantics (constraints, conventions, extensions), in addition to those defined by the media type, that are associated with the target resource. | 🔴 apkg-rec:profile | 🔴 apkg-rec:Link | xsd:anyURI | 0-M | 0-M | RFC 3986 (SES) | owl:DatatypeProperty, shared with apkg-rec:LinkTemplate (domain: union of Link and LinkTemplate). Same treatment as the Record conformsTo property (Table A.1.1). In v3 it becomes dct:conformsTo (dct:Standard). |
| created | Date of creation of the resource pointed to by the link. | 🟢 dct:created | 🔴 apkg-rec:Link | xsd:dateTimeStamp | 0-1 | 0-1 | RFC 3339 (SES) | RFC 3339 date-time requires a time offset. Describes the target, not the Link node. |
| updated | Most recent date on which the resource pointed to by the link was changed. | 🟢 dct:modified | 🔴 apkg-rec:Link | xsd:dateTimeStamp | 0-1 | 0-1 | RFC 3339 (SES) | RFC 3339 date-time requires a time offset. Describes the target, not the Link node. |

[<- main](README.md)