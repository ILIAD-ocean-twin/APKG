# APKG Linked Data Application Profile

[<- main](README.md)

## Properties related to the Catalogue Record  

- Table A.1.1

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|---|---|---|---|---|---|---|---|---|
| id | A unique record identifier assigned by the server. | 🟢 dct:identifier | 🔴 apkg-rec:Record | xsd:string | 1 | 1 |  |  |
| created | The date this record was created in the server. | 🟢 dct:created | 🔴 apkg-rec:Record | xsd:dateTimeStamp | 0-1 | 0-1 |  | RFC 3339 date-time requires a time offset → xsd:dateTimeStamp |
| updated | The most recent date on which the record was changed. | 🟢 dct:modified | 🔴 apkg-rec:Record | xsd:dateTimeStamp | 0-1 | 0-1 |  |  |
| conformsTo | The extensions/conformance classes used in this record | 🟢 dct:conformsTo | 🔴 apkg-rec:Record | 🟢 dct:Standard (IRI) | 0-M | 0-M |  | Values are OGC conformance class IRIs |
| language | The language used for textual values (i.e., titles, descriptions, etc.) of this record. | 🟢 dct:language | 🔴 apkg-rec:Record | 🔴 apkg-rec:Language | 0-1 | 0-1 |  | apkg-rec:Language rdfs:subClassOf dct:LinguisticSystem |
| languages | The list of other languages in which this record is available. | 🔴 apkg-rec:hasAlternateLanguage | 🔴 apkg-rec:Record | 🔴 apkg-rec:Language | 0-M | 0-M |  | owl:ObjectProperty; rdfs:seeAlso dct:language. No existing term distinguishes primary vs other languages |
| links | A related link of the record | 🟢 dcat:qualifiedRelation | 🔴 apkg-rec:Record | 🔴 apkg-rec:Link | 0-M | 0-M |  | apkg-rec:Link rdfs:subClassOf dcat:Relationship |
| linkTemplates | A link template related to this record | 🔴 apkg-rec:hasLinkTemplate | 🔴 apkg-rec:Record | 🔴 apkg-rec:LinkTemplate | 0-M | 0-M |  | owl:ObjectProperty; apkg-rec:LinkTemplate rdfs:subClassOf hydra:IriTemplate |

[<- main](README.md)

## Properties related to the Resource

- Table A.1.2

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| type | The nature or genre of the resource described by this record. | 🟢 dct:type | 🔴 apkg-rec:Record | IRI | 0-1 | 0-1 | dct:DCMIType | DCMI range of dct:type is rdfs:Class; dct:DCMIType is a VES, not a range. Non-DCMI values need a local VES (TODO) |
| title | A human-readable name given to the resource described by this record. | 🟢 dct:title | 🔴 apkg-rec:Record | rdf:langString | 0-1 | 1 |  |  |
| description | A free-text description of the resource described by this record. | 🟢 dct:description | 🔴 apkg-rec:Record | rdf:langString | 0-1 | 0-1 |  |  |
| geometry | A spatial extent associated with the resource described by this record. | 🟢 geo:hasGeometry | 🔴 apkg-rec:Record | 🔴 apkg-rec:Geometry | 0-1 | 0-1 |  | GeoSPARQL domain geo:Feature: apkg-rec:Record is inferred as geo:Feature. apkg-rec:Geometry rdfs:subClassOf geo:Geometry |
| time | A temporal extent associated with the resource described by this record. | 🟢 time:hasTime | 🔴 apkg-rec:Record | 🟢 time:TemporalEntity | 0-1 | 0-1 |  | time:Interval (time:hasBeginning / time:hasEnd) or time:Instant (time:inXSDDateTimeStamp, or time:inXSDDate for dates). Open-ended interval: omit time:hasEnd |
| keywords | Free-form keyword or tag associated with the resource described by this record. | 🟢 dcat:keyword | 🔴 apkg-rec:Record | rdf:langString | 0-M | 0-M |  | DCAT domain dcat:Resource: apkg-rec:Record is inferred as dcat:Resource |
| themes | The subject areas, topics or categories that the record falls under, drawn from a recognised classification system or thesaurus. | 🔴 apkg-rec:hasTheme | 🔴 apkg-rec:Record | 🔴 apkg-rec:Theme | 0-M | 0-M |  | owl:ObjectProperty. A Theme groups concepts from one scheme (dcat:theme points to a single concept) |
| resourceLanguages | The list of languages in which the resource described by this record can be retrieved. | 🔴 apkg-rec:resourceLanguage | 🔴 apkg-rec:Record | 🔴 apkg-rec:Language | 0-M | 0-M |  | owl:ObjectProperty; rdfs:seeAlso dct:language. dct:language is already used for the language of the record |
| externalIds | One or more identifiers, assigned by an external entity, for the resource described by this record. | 🟢 adms:identifier | 🔴 apkg-rec:Record | 🟢 adms:Identifier | 0-M | 0-M |  | OGC externalId = {scheme, value}: value → skos:notation; scheme → TODO (dct:creator or adms:schemaAgency) |
| formats | The list of available distribution formats for the resource that a record describes. It can include both physical and digital distribution formats. | 🔴 apkg-rec:hasFormat | 🔴 apkg-rec:Record | 🔴 apkg-rec:Format | 0-M | 0-M |  | owl:ObjectProperty. dct:hasFormat links to another version of the resource, not to a format description |
| contacts | A list of contacts qualified by their role(s) in association to the record or the resource described by this record. | 🟢 dcat:contactPoint | 🔴 apkg-rec:Record | 🔴 apkg-rec:Contact | 0-M | 0-M |  | apkg-rec:Contact rdfs:subClassOf vcard:Kind (DCAT range of dcat:contactPoint). Roles: TODO |
| licence | The legal provisions under which the resource described by this record is made available. | 🟢 dct:license | 🔴 apkg-rec:Record | 🟢 dct:LicenseDocument (IRI) | 0-1 | 0-1 | SPDX | OGC value is a string (e.g. SPDX id): use the SPDX licence IRI |
| rights | A statement that concerns all rights not addressed by the license such as a copyright statement. | 🟢 dct:rights | 🔴 apkg-rec:Record | 🟢 dct:RightsStatement | 0-1 | 0-1 |  | Statement text as rdfs:label of the dct:RightsStatement node |

[<- main](README.md)