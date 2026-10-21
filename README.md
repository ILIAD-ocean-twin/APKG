# APKG Linked Data Application Profile

# 1. NameSpaces
| Prefix      | URI                                                  |
| ----------  | -----------------------------------------------------|
| xsd         | http://www.w3.org/2001/XMLSchema#                    |
| rdf         | http://www.w3.org/1999/02/22-rdf-syntax-ns#          |
| adms        | http://www.w3.org/ns/adms#         ????              |
| apkg-rec    | http://w3id.org/apkg/records#                        |                       
| dcat        | http://www.w3.org/ns/dcat#                           |
| dct         | http://purl.org/dc/terms/                            |
| doap        | http://usefulinc.com/ns/doap#                        |
| foaf        | http://xmlns.com/foaf/0.1/                           |
| geo         | http://www.opengis.net/ont/geosparql#                |
| geojson     | http://purl.org/geojson/vocab#                   |
| hydra       | https://www.w3.org/ns/hydra/core#                    |
| ianaRelation   | http://www.iana.org/assignments/relation/         |
| ianaMediaType | https://www.iana.org/assignments/media-types/      |
| prov        | http://www.w3.org/ns/prov#                           |
| rec         | https://www.opengis.net/def/ogc-api/records/         | 
| time        | http://www.w3.org/2006/time#                         |
| org         | http://www.w3.org/ns/org#                            |
| cito        | http://purl.org/spar/cito/                           |
| fabio       | http://purl.org/spar/fabio/                          |
| ISO639-2    | http://purl.org/dc/terms/ISO639-2    |         



a ver se precisamos

| Prefix     | URI                                                  |
|------------|------------------------------------------------------|
| schema     | http://schema.org/                                   |
| cwl        | https://w3id.org/cwl/cwl#                            |
| cwltool    | http://commonwl.org/cwltool#                         |


-----------------------------------------------------------------------

## 2. Module Core

🟢 $\color{green}{\rightarrow}$ a term from another ontology.
🔴 $\color{red}{\rightarrow}$ apkg-rec ontology

Table 1 - Core classes related to the catalogue record


|Class | Description | Term | Notes|
|---|---|---|--|
| Record | A record in the catalogue | 🔴 apkg-rec:Record  | rdfs:subClassOf rdfs:Resource|
  Link    | A link related to this record    |🟢 hydra:Link | |

Table 2 - Core properrties related to the catalogue record
| OGC Property   | Description                                                                              | Vocabulary Term                          | Domain                                   | Range                             | Cardinality OGC | Cardinality APKG | VES | Note |
|----------------|------------------------------------------------------------------------------------------|-------------------------|------------------------------------------|-----------------------------------|-------------|-----|------|--|
| id             | A unique record identifier assigned by the server.                                       |🔴  apkg-rec:recordId                        | apkg-rec:Record                       | xsd:string                       | 1         | 1         |     |   owl:DatatypeProperty, rdfs:subPropertyOf dct:identifier |
| created        | The date this record was created in the server.                                          | 🔴 apkg-rec:createdAt                               | apkg-rec:Record                             | xsd:dateTimeStamp                      | 0-1         | 0-1         |     |   owl:DatatypeProperty, rdfs:subPropertyOf dcterms:created  |
| updated        | The most recent date on which the record was changed.                                    | 🔴 apkg-rec:updatedAt                             | apkg-rec:Record                             | xsd:dateTimeStamp                          | 0-1         | 0-1         |     |     owl:DatatypeProperty , rdfs:subPropertyOf dcterms:modified.  |
| conformsTo     | The extensions/conformance classes used in this record                                   | 🔴 apkg-rec:conformsTo                           | apkg-rec:Record                            | dct:Standard                      | 0-M         | 0-M         |     |   owl:ObjectProperty, rdfs:subPropertyOf dcterms:conformsTo |
| language       | The language used for textual values (i.e., titles, descriptions, etc.) of this record. | 🔴 apkg-rec:language                              | apkg-rec:Record                            | dct:LinguisticSystem          | 0-1         | 0-1  | ISO639-2    |   rdfs:subPropertyOf dct:language; It migth require to match with https://schemas.opengis.net/ogcapi/records/part1/1.0/openapi/schemas/language.yaml in Version 2 (TODO) |
| languages       | The list of other languages in which this record is available. | 🔴 apkg-rec:alternateLanguage                         | apkg-rec:Record                            | dct:LinguisticSystem         | 0-M         | 0-M         |   ISO639-2  |  rdfs:subPropertyOf dct:language; See note in _language_.     |
| links          | A related link of the record                                                            |          🟢  dct:relation             | apkg-rec:Record                            | hydra:Link                      | 0-M         | 0-M         |     |    |
| title          | A title of the related link   |          🟢  dct:title             | apkg-rec:Link                            | xsd:string                     | 0-1        | 0-1        |     | |
| href          | A URL related to this record    |          🟢  dct:             | apkg-rec:Record                            | apkg-rec:Link                      | 0-M         | 0-M         |     |    |
| rel          | The type of relation of this record    |          🟢  dct:relation            | apkg-rec:Link                            | xsd:anyURI | 1 | 1 | ianaRelation    |    |
| type | Media type of the relation of this record | 🟢 dct:format | apkg-rec:Link | dct:MediaType| 0-1  | 0-1  | ianaMediaType | |
| linkTemplates  | A link template related to this record                                                   |            🟢 hydra:IriTemplate         | apkg-rec:Record                           |                       | 0-1         | 0-1         |     |   |

Table 3- Core classes related to the resource
|Class | Description | Term | Notes|
|---|---|---|--|
| Geometry | The geometry of the object | 🟢geo:Geometry |
| Theme | A theme of the Record | 🔴 apkg-rec:Theme |
| Concept | A concept of the theme | 🔴 apkg-rec:Concept |
| Format | A format of file | 🔴 apkg-rec:Format | https://schemas.opengis.net/ogcapi/records/part1/1.0/openapi/schemas/format.yaml . |
| Contact | A contact of the record | 🔴 apkg-rec:Contact | subClassOf dct:Agent


Table 4 - Core properties related to the resource.

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
| name | The name of the responsible person. | 🔴 apkg-rec:contactName | apkg-rec:Contact| xsd:string | 0-1 |0-1| |rdfs:subPropertyOf foaf:name
| position |  The name of the role or position of the responsible person taken from the organization's formal organizational hierarchy or chart. | 🟢 org:holds | apkg-rec:Contact| xsd:string |0-1 | 0-1 |
| organisation | Organization/affiliation of the contact. | 🔴 apkg-rec:contactOrganisationName | apkg-rec:Contact| xsd:string | 0-1 |0-1| rdfs:subPropertyOf foaf:name
| licence| The legal provisions under which the resource described by this record is made available. | | apkg-rec:Record  |   | | |
| rights| A statement that concerns all rights not addressed by the license such as a copyright statement.| | apkg-rec:Record  | | | |

Table 5 - Extension classes related to the Process .

|Class | Description | Term | Notes|
|---|---|---|--|
| Process | A Provcess | 🔴 apkg-rec:Process |

Table 6 - Extension properties related to the Process .

| Property | Description                                                               | Vocabulary Term                          | Domain                                   | Range                             | Cardinality | VES | Note |
|--------------|---------------------------------------------------------------------|------------------------------------------|------------------------------------------|-----------------------------------|-------------|-----|------|
|     Identifier         | Unique identifier of the process. Pensar nisto....       |      |apkg-rec:Process          
|      none        | Family of this application package (identifier without version)???REVER     | apkg:family                              | apkg-rec:Process                  | xsd:anyURI                        | 1-1         |     |      |
|    none          | The application package has several software versions                         | 🟢doap:release                   | apkg-rec:Process                  | doap:Version                    | 1-M         |     |      |
| __Version__ | A version of the Application Process | 🟢doap:Version |
| none | The date of creation of the version | 🟢doap:creation | doap:Version | xsd:date| 0-1 | 
| none | The major revision | 🔴 apkg-rec:majorVersion | doap:Version | xsd:integer | 1-1 | | owl:FunctionalProperty |
| none | The minor revision | 🔴 apkg-rec:minorVersion | doap:Version | xsd:integer | 1-1 | | owl:FunctionalProperty |
| none | The patch revision | 🔴 apkg-rec:patchVersion | doap:Version | xsd:integer | 1-1 | | owl:FunctionalProperty
| none | The registration of the application package | 🟢 prov:wasGeneratedBy | apkg-rec:Process | prov:Activity
|  none            | This is the latest version of the application package  NãO É PRECISO RETIRAR!              |
| __Registry__          | Registry where the application package is registered in. | 🟢prov:Activity |
| none |  The agent where you reistered |🟢 prov:wasAssociatedWith | prov:Activity
| none | Date and time of registration | 🟢 prov:atTime | prov:Activity | xsd:dateTimeStamp |       
| none | URL of the registration | 🟢 rdfs:seeAlso | prov:Activity  | | | | Force in SHACL :sh:property [  sh:path rdfs:seeAlso ; sh:nodeKind sh:IRI ;  sh:pattern^https://" ; sh:maxCount 1 ; ] .
|   none           | The Application Package has a CWL                                | 🔴 apkg-rec:hasCWLDescriptor                            | apkg-rec:Process                  | dcat:Distribution                      | 0-1         |     |  apkg-rec:hasCWLDescriptor  rdfs:subPropertyOf dcat:distribution    |
| __CWL-URL__       | The CWL Application Package definition |   🟢 dcat:Distribution|
|   | THe CWL URL | 🟢 dcat:accessURL |  dcat:Distribution | xsd:anyURI | 1-1 |
|   | THe CWL format | 🟢 dct:format |  dcat:Distribution |<https://www.iana.org/assignments/media-types/application/x-cwl> |1-1||Force on SHACL (sh:hasValue <https://www.iana.org/assignments/media-types/application/x-cwl>; sh:minCount 1 ; sh:maxCount 1 ; )|
|    none          | Citation of a work related to the application package               | 🟢 cito:cites                         | apkg-rec:Process                  | fabio:ResearchPaper                       | 0-M         |   _
|     none         | License of the application package                                  | 🟢 dct:license                              | apkg-rec:Process                  | dct:LicenseDocument               | 0-1         |     |      |
|    none          | Author of the application package                                   | 🟢 dct:creator                            | apkg-rec:Process                  | foaf:Person; foaf:Organization                       | 1-M         |     |      |
|    none          | Contributor of the application package                              | 🟢 dct:contributor                       | apkg-rec:Process                  | foaf:Person; foaf:Organization                       | 0-M         |     |      |
|    none          | Maintainer of the application package                               | 🟢 doap:maintainer                        | apkg-rec:Process                  | foaf:Person; foaf:Organization                        | 0-M         |     |      |
|    none          | Publisher of the application package                                | schema:publisher                         | apkg-rec:Process                  | foaf:Person; foaf:Organization                        | 0-1         |     |      |
|     none         | Organisations involved in the application package                   | schema:sourceOrganization                | apkg-rec:Process                  | foaf:Organization                 | 1-M         |     |      |
|     none         | Organisation that produced the application package                  | schema:author                            | apkg-rec:Process                  | apkg:Organisation                 | 1-1         |     |      |
|     none         | Spatial coverage of the application package                         | schema:spatialCoverage                   | apkg-rec:Process                  | schema:Place                      | 1-1         |     |      |
|     none         | URL of the application package code repository                      | schema:codeRepository                    | apkg-rec:Process                  | schema:URL                        | 0-1         |     |      |
|              | Programming language of the application package                     | schema:programmingLanguage               | apkg-rec:Process                  | schema:Text                       | 0-1         |     |      |
|              | Original URL of the application package when registered             | apkg:originalURL                         | apkg-rec:Process                  | schema:URL                        | 0-1         |     |      |
| Link of the application package                                     | apkg-rec:Process                   | apkg:Link                               | apkg:hasLink                             | 1-M         |                                 |                                                             |
| __Person__                                                          |                                          |                                          | apkg:Person                              |             |                                 | rdfs:subClassOf schema:Person                               |
| Name(s) of the Person                                               | apkg:Person                              | xsd:string                               | schema:name                              | 1-1         |                                 |                                                             |
| Email address of the person                                         | apkg:Person                              | xsd:string                               | schema:email                             | 1-1         |                                 |                    |                                                    | __Organisation__                                                    |                                          |                                          | apkg:Organisation                        |             |                                 | rdfs:subClassOf schema:Organization                         |
| Name of the Organisation                                            | apkg:Organisation                        | xsd:string                               | schema:name                              | 1-1         |                                 |                                                             |
| URL of the webpage of Organisation                                  | apkg:Organisation                        |  schema:URL                              | schema:url                               | 1-1         |                                 |                                                             |                                   
| Address of the Organisation                                         | apkg:Organisation                        | apkg:PostalAddress                       | schema:address                           | 1-1         |                                 |                                                             |  
| __PostalAddress__                                                   |                                          |                                          | apkg:PostalAddress                       |             |                                 | rdfs:subClassOf schema:PostalAddress                        |   
| Country                                                             | apkg:PostalAddress                       | xsd:string                               | schema:addressCountry                    | 1-1         |                                 |                                                             |                                                     
| __Process__                                                         |                                          |                                          | apkg:Process                             |             |                                 | rdfs:subClassOf cwl:Process                                 |
| Class of the Process (CommandLineTool or Workflow)                  | apkg:Process                             | xsd:string                               | dct:type                                 | 1-1         | ["CommandLineTool", "Workflow"] |                                                             |
| Input of the Process                                                | apkg:Process                             | apkg:Parameter                           | apkg:hasInput                            | 0-M         |                                 |                                                             |
| Output of the Process                                               | apkg:Process                             | apkg:Parameter                           | apkg:hasOutput                           | 1-M         |                                 |                                                             |
| __Parameter__                                                       |                                          |                                          | apkg:Parameter                           |             |                                 | rdfs:subClassOf cwl:InputParameter                          |
| The unique identifier for the object                                | apkg:Parameter                           | xsd:string                               | dct:identifier                           | 0-1         |                                 |                                                             |
| The type of data                                                    | apkg:Parameter                           | xsd:string                               | dct:type                                 | 1-1         |  ["null","boolean", "int", "long", "float", "double", "string", "File", "Directory" ] |       |
| A short, human-readable label                                       | apkg:Parameter                           | xsd:string                               | apkg:label                               | 0-1         |                                 |                                                             |
| A documentation string                                              | apkg:Parameter                           | xsd:string                               | apkg:doc                                 | 0-1         |                                 |                                                             |
| The file format that will be assigned to the output File object     | apkg:Parameter                           | xsd:string                               | schema:fileFormat                        | 0-1         |                                 | Use only when apkg:hasType is a CWLtype=File                |
| __Temporal Coverage__                                               |                                          |                                          | apkg:TemporalCoverage                    |             |                                 | rdfs:subClassOf time:TemporalEntity                         |
| Start date-time                                                     | apkg:TemporalCoverage                    | apkg:Instant                             | time:hasBeginning                        | 0-1         |                                 |                                                             |
| End date-time                                                       | apkg:TemporalCoverage                    | apkg:Instant                             | time:hasEnd                              | 0-1         |                                 |                                                             |                                                      
| __TimeInstant__                                                     |                                          |                                          | apkg:Instant                             |             |                                 | rdfs:subClassOf time:Instant                                |
| Date-time                                                           | apkg:Instant                             | **xsd:dateTimeStamp**                    | **time:inXSDDateTimeStamp  **            | 1-1         |                                 |                                                             |
| __Spatial validity of the model__                                   |                                          |                                          | apkg:Geometry                            |             |                                 |  rdfs:subClassOf gj:Geometry                                |
| Coordinates                                                         | apkg:Geometry                            | gj:coordinates                           | gj:coordinates                           | 1-M         |                                 |                                                             |
| Type                                                                | apkg:Geometry                            | xsd:anyURI                              | gj:type                                 | 1-1         | gj:Polygon                    |                                                             |
| __Link of the application package__                                 |                                          |                                          | apkg:Link                                |             |                                 |                                                             |
| Title of the destination                                            | apkg:Link                                | xsd:string                               | dct:title                                | 0-1         |                                 |                                                             |
| Type or semantics of the relation                                   | apkg:Link                                | xsd:string                               | dct:type                                 | 0-1         | ["root", "self", "alternate", "collection"]  |                                                |
| The URL of the link                                                 | apkg:Link                                | schema:URL                               | schema:url                               | 1-1         |                                 |                                                             |
| The mimetype of the link                                            | apkg:Link                                | xsd:string                               | dcat:mediaType                           | 0-1         | https://w3id.org/spar/mediatype/ |                                                            |
| __Secrets__                                                         |                                          |                                          | apkg:Secrets                             |             |                                 |  rdfs:subClassOf cwl:Secrets                                |
| The ID of the Input parameters considered secret                    | apkg:Secrets                             | xsd:string                               | cwltool:secrets                          | 0-M         |                                 |                                                             |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


&copy; INESC TEC, 2026
