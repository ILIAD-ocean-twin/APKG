# APKG Linked Data Application Profile

# 1. NameSpaces
| Prefix      | URI                                                  |
| ----------  | -----------------------------------------------------|
| xsd         | http://www.w3.org/2001/XMLSchema#                    |
| rdf         | http://www.w3.org/1999/02/22-rdf-syntax-ns#          |
| rdfs        | FALTA |
| adms        | http://www.w3.org/ns/adms#         ????              |
| apkg-rec    | http://w3id.org/apkg/records#                        |
| cito        | http://purl.org/spar/cito/                           |
| dcat        | http://www.w3.org/ns/dcat#                           |
| dct         | http://purl.org/dc/terms/                            |
| doap           | http://usefulinc.com/ns/doap#                        |
| fabio          | http://purl.org/spar/fabio/                          |
| foaf           | http://xmlns.com/foaf/0.1/                           |
| geo            | http://www.opengis.net/ont/geosparql#                |
| geojson        | http://purl.org/geojson/vocab#                       |
| hydra          | https://www.w3.org/ns/hydra/core#                    |
| ianaRelation   | http://www.iana.org/assignments/relation/         |
| ianaMediaType  | https://www.iana.org/assignments/media-types/     |
| ISO639-2       | http://purl.org/dc/terms/ISO639-2                 |
| org         | http://www.w3.org/ns/org#                            |
| prov        | http://www.w3.org/ns/prov#                           |
| rec         | https://www.opengis.net/def/ogc-api/records/         |
| time        | http://www.w3.org/2006/time#                         |
|vcard        | http://www.w3.org/2006/vcard/ns#                     |


        



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

Table A - Core classes related to the catalogue record


| id |Class | Description | Term | Notes| Table(s) |
|---|---|---|---|--|- | 
| 1 | [Record](RecordClass.md) | A record in the catalogue | 🔴 apkg-rec:Record  | rdfs:subClassOf rdfs:Resource | Table A.1.1; Table A.1.2 |
| 2 | [Link](LinkClass.md)    | A link related to this record    | 🔴apkg-rec:Link|  | Table A.2.1 | 


Table B - Core classes related to the resource

| id |Class | Description | Term | Notes| Table(s) |
|---|---|---|---|--|- | 
| 3 | [Geometry](GeometryClass.md) | The geometry of the object | 🔴 apkg-rec:Geometry | rdfs:subClassOf geo:Geometry |
| 4 | [Theme](ThemeClass.md) | A theme of the Record | 🔴 apkg-rec:Theme | |
| 5 | [Concept](ConceptClass.md) | A concept of the theme | 🔴 apkg-rec:Concept | |
| 6 | [Format](FormatClass.md) | A format of file | 🔴 apkg-rec:Format | https://schemas.opengis.net/ogcapi/records/part1/1.0/openapi/schemas/format.yaml . |
| 7 | [Contact](ContactClass.md) | A contact of the record | 🔴 apkg-rec:Contact | rdfs:subClassOf dct:Agent |
| 8 | [Language](LanguageClass.md) | The language used for textual values in this record | 🔴 apkg-rec:Language |  |
| 9  | [Address](AddressClass.md) | The Physical location at which contact can be made.| 🔴apkg-rec:Address | rdfs:subClassOf vcard:Address |
| 10 | [Email](EmailClass.md) | Email addresses at which contact can be made. |🔴 apkg-rec:Email |
| 11 | [Phone](PhoneClass.md) | Telephone numbers at which contact can be made | 🔴apkg-rec:Phone |
| 12 | [Role](RoleClass.md) | The set of named duties, job functions and/or permissions associated with this contact. (e.g. developer, administrator, etc.).| 🔴 apkg-rec:Role |




Table 5 - Extension classes related to the Process .

| id |Class | Description | Term | Notes| Table(s) |
|---|---|---|---|--|- | 
| 7 | Process | A Process | 🔴 apkg-rec:[Process](ProcessClass.md) |

Table C - Extension Classes and properties related to the Process .

| Property | Description                                                               | Vocabulary Term                          | Domain                                   | Range                             | Cardinality | VES | Note |
|--------------|---------------------------------------------------------------------|------------------------------------------|------------------------------------------|-----------------------------------|-------------|-----|------|
|     identifier         | Unique identifier of the process. Pensar nisto....       |      |apkg-rec:Process          
|      family        | Family of this application package (identifier without version)???REVER     | apkg:family                              | apkg-rec:Process                  | xsd:anyURI                        | 1-1         |     |      |
|    none      | The application package has several software versions                         | 🟢doap:release                   | apkg-rec:Process                  | doap:Version                    | 1-M         |     |      |
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
