# APKG Linked Data Application Profile

[<- main](README.md)

## Core properties related to the Link Class

- Table A.2.1


| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| href | A URL related to this record | 🟢 foaf:page | 🔴 apkg-rec:Link | 🟢 foaf:Document | 1 | 1 |  |  |
| rel | The type of relation of this record | 🟢 dct:type | 🔴 apkg-rec:Link | xsd:string | 1 | 1 | ianaRelation | DCMI range of dct:type is rdfs:Class: IANA relation terms are inferred as classes of links |
| type | Media type of the relation of this record | 🟢 dct:format | 🔴 apkg-rec:Link | 🟢 dct:MediaType | 0-1 | 0-1 | ianaMediaType |  |
| hreflang | A hint indicating what the language of the result of dereferencing the link should be. | 🟢 dct:language | 🔴 apkg-rec:Link | 🔴 apkg-rec:Language | 0-1 | 0-1 |  | apkg-rec:Language rdfs:subClassOf dct:LinguisticSystem. Language code (RFC 5646) defined in the Language class |
| title | A title of the related link | 🟢 dct:title | 🔴 apkg-rec:Link | rdf:langString | 0-1 | 0-1 |  |  |
| length | The size in bytes of the target resource | 🟢 dcat:byteSize | 🔴 apkg-rec:Link | xsd:nonNegativeInteger | 0-1 | 0-1 |  | DCAT domain of dcat:byteSize is dcat:Distribution: apkg-rec:Link is inferred as dcat:Distribution |
| profile | One or more identifiers that provide information about additional semantics (constraints, conventions, extensions), in addition to those defined by the media type, that are associated with the target resource. | 🟢 dct:conformsTo | 🔴 apkg-rec:Link | IRI (prof:Profile) | 0-M | 0-M |  | prof:Profile rdfs:subClassOf dct:Standard (DCMI range of dct:conformsTo) |
| created | Date of creation of the resource pointed to by the link. | 🟢 dct:created | 🔴 apkg-rec:Link | xsd:dateTimeStamp | 0-1 | 0-1 |  | RFC 3339 date-time requires a time offset |
| updated | Most recent date on which the resource pointed to by the link was changed. | 🟢 dct:modified | 🔴 apkg-rec:Link | xsd:dateTimeStamp | 0-1 | 0-1 |  | RFC 3339 date-time requires a time offset |

[<- main](README.md)