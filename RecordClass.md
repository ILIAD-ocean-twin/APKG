[<- main](README.md)

## Core properties related to the Record Class 

- Table 1.1

| OGC Property   | Description                                                                              | Vocabulary Term                          | Domain                                   | Range                             | Cardinality OGC | Cardinality APKG | VES | Note |
|----------------|------------------------------------------------------------------------------------------|-------------------------|------------------------------------------|-----------------------------------|-------------|-----|------|--|
| id             | A unique record identifier assigned by the server.                                       |🔴  apkg-rec:recordId                        | apkg-rec:Record                       | xsd:string                       | 1         | 1         |     |   owl:DatatypeProperty, rdfs:subPropertyOf dct:identifier |
| created        | The date this record was created in the server.                                          | 🔴 apkg-rec:createdAt                               | apkg-rec:Record                             | xsd:dateTimeStamp                      | 0-1         | 0-1         |     |   owl:DatatypeProperty, rdfs:subPropertyOf dcterms:created  |
| updated        | The most recent date on which the record was changed.                                    | 🔴 apkg-rec:updatedAt                             | apkg-rec:Record                             | xsd:dateTimeStamp                          | 0-1         | 0-1         |     |     owl:DatatypeProperty , rdfs:subPropertyOf dcterms:modified.  |
| conformsTo     | The extensions/conformance classes used in this record                                   | 🔴 apkg-rec:conformsTo                           | apkg-rec:Record                            | dct:Standard                      | 0-M         | 0-M         |     |   owl:ObjectProperty, rdfs:subPropertyOf dcterms:conformsTo |
| language       | The language used for textual values (i.e., titles, descriptions, etc.) of this record. | 🔴 apkg-rec:language                              | apkg-rec:Record                            | dct:LinguisticSystem          | 0-1         | 0-1  | ISO639-2    |   rdfs:subPropertyOf dct:language; It migth require to match with https://schemas.opengis.net/ogcapi/records/part1/1.0/openapi/schemas/language.yaml in Version 2 (TODO) |
| languages       | The list of other languages in which this record is available. | 🔴 apkg-rec:alternateLanguage                         | apkg-rec:Record                            | dct:LinguisticSystem         | 0-M         | 0-M         |   ISO639-2  |  rdfs:subPropertyOf dct:language; See note in _language_.     |
| links          | A related link of the record                      |          🟢  dct:relation             | apkg-rec:Record                            | apkg-rec:Link                      | 0-M         | 0-M         |     |    |
| linkTemplates  | A link template related to this record                                                   |            🟢 hydra:IriTemplate         | apkg-rec:Record                           |                       | 0-1         | 0-1         |     |   |


## Resource properties related to the Record Class 

- Table 1.2

| Property OGC | Description                                                               | Vocabulary Term                          | Domain                                   | Range                             | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|---------------------------------------------------------------------|------------------------------------------|------------------------------------------|-----------------------------------|-------------|-----|------|--|
|      type        |          The nature or genre of the resource described by this record. |   🔴 apkg-rec:resourceType  |  apkg-rec:Record        | dct:DCMIType |  0-1             |  0-1             | |owl:ObjectProperty, rdfs:subPropertyOf dcterms:type . Não precisamos de redeclarar rdfs:range dcterms:DCMIType em process:recordType. Pela cadeia de regras RDFS (subpropriedade → propriedade base → range).    .
|          title    | A human-readable name given to the resource described by this record.                                   | 🔴 apkg-rec:title                                | apkg-rec:Record                  | xsd:string                      | 0-1         | 1         |     |   owl:DatatypeProperty, rdfs:subPropertyOf dcterms:title |
|  description            | 	A free-text description of the resource described by this record.                              | 🔴 apkg-rec:description                          | apkg-rec:Record                     | xsd:string                 | 0-1   | 0-1   |     |   rdfs:subPropertyOf dct:description   |
|   has geometry           | A spatial extent associated with the resource described by this record. | 🟢 geo:hasGeometry                  | apkg-rec:Record                | geo:Geometry                     | 0-1         | 0-1         |     |   |  
| type | The type of the object  |🟢 geojson:type | geo:Geometry | xsd:anyURI | 1 | 1 | geojson concept scheme | O concept scheme tem de ser defnido em skos.
| coordinates | The coordinates of the  object |🟢 geojson:coordinates | geo:Geometry | xsd:string | 1-M | 1-M
| time | A temporal extent associated with the resource described by this record.                         |          🟢 time:hasTime           |    apkg-rec:Record                   | time:Interval   or time:Instant      | 0-1 | 0-1 | | ex:record123 a apkg-rec:Record, time:hasTime ex:record123-time. ex:record123-time a time:Interval, time:hasBeginning ex:record123-start time:hasEnd  ex:record123-end . ex:record123-start a time:Instant, time:inXSDDateTimeStamp "2026-01-01T00:00:00Z"^^xsd:dateTimeStamp . ex:record123-end a time:Instant, time:inXSDDateTimeStamp "2026-06-30T23:59:59Z"^^xsd:dateTimeStamp . o time:Instant é para o caso de ser somente "date" ou "timestamp".
|      keywords      | Free-form keyword or tag associated with the resource described by this record.                                | 🟢 dcat:keyword                             | apkg-rec:Record                     | xsd:string                       | 0-M         | 0-M         |     |      |
| themes |   The subject areas, topics or categories that the record falls under, drawn from a recognised classification system or thesaurus.    | 🟢 apkg-rec:hasTheme    |apkg-rec:Record   | 🔴 apkg:Theme| 0-M| 0-M|
| concepts |The classification of the KOS defined on theme | 🔴apkg-rec:hasConcept | apkg-rec:Theme |  apkg-rec:Concept    | 0-M |0-M | | Listing 22 and Listing 38 at https://docs.ogc.org/is/20-004r1/20-004r1.html show divergent uses of hasConcept term of the Themes Class. In the first it is a Class with _id_ and _url_ and at the second  a list of xsd:String. | 
| scheme | THe KOS scheme  of the Concepts in the specific theme | skos:inScheme | apkg-rec:Theme | xsd:anyURI | 1 | 1 |
| id | The id of the concept | apkg-rec:schemaIdentifier | apkg-rec:Concept | xsd:string | 0-1| 0-1| owl:DatatypeProperty, rdfs:subPropertyOf dct:identifier
| uri | The URI of the concept | skos:Concept | apkg-rec:Concept | xsd:anyURI | 0-1| 0-1|| 
| resourceLanguages| The list of languages in which the resource described by this record can be retrieved. | 🔴 apkg-rec:resourceLanguage | apkg-rec:Record     | dct:LinguisticSystem     | 0-M| 0-M| ISO639-2 |rdfs:subPropertyOf dct:language. See note in _language_.
| externalIds | One or more identifiers, assigned by an external entity, for the resource described by this record. | 🔴 apkg-rec:externalIdentifier    | apkg-rec:Record                     | xsd:string   |     0-M|     0-M |  | owl:DatatypeProperty, rdfs:subPropertyOf dct:identifier   
| formats | The list of available distribution formats for the resource that a record describes. It can include both physical and digital distribution formats.| 🟢 dct:hasFormat |apkg-rec:Record   | apkg-rec:Format| 0-M| 0-M|
| name | The name of the format the resource that the record describes. | 🟢 dct:title |apkg-rec:Format   | xsd:string| 0-1| 0-1|
| mediatype | The media of the format the resource that the record describes.| 🟢 dct:format |apkg-rec:Format   | dct:MediaTypeOrExtent| 0-1| 0-1|
| contacts | A list of contacts qualified by their role(s) in association to the record or the resource described by this record. | apkg-rec:hasContact |apkg-rec:Record   | apkg-rec:Contact| 0-M|0-M |
| identifier | The identifier of the contact. | 🔴apkg-rec:contactIdentifier | apkg-rec:Contact| xsd:string | 0-1 |0-1| |rdfs:subPropertyOf dct:identifier
| name | The name of the responsible person. | 🔴 apkg-rec:contactName | apkg-rec:Contact| xsd:string | 0-1 |0-1| | rdfs:subPropertyOf foaf:name
| position |  The name of the role or position of the responsible person taken from the organization's formal organizational hierarchy or chart. | 🟢 org:holds | apkg-rec:Contact| xsd:string |0-1 | 0-1 |
| organisation | Organization/affiliation of the contact. | 🔴 apkg-rec:contactOrganisationName | apkg-rec:Contact| xsd:string | 0-1 |0-1| | rdfs:subPropertyOf foaf:name
| logo | Graphic identifying a contact. The link relation should be icon  and the media type should be an image media type.| 🔴 apkg-rec:hasLogo | apkg-rec:Contact | apkg-rec:Link ||
| licence| The legal provisions under which the resource described by this record is made available. | | apkg-rec:Record  |   | | |
| rights| A statement that concerns all rights not addressed by the license such as a copyright statement.| | apkg-rec:Record  | | | |