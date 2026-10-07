# APKG Linked Data Application Profile

# 1. NameSpaces
| Prefix      | URI                                                  |
| ----------  | -----------------------------------------------------|
| xsd         | http://www.w3.org/2001/XMLSchema#                    |
| rdf         | http://www.w3.org/1999/02/22-rdf-syntax-ns#          |
| adms        | http://www.w3.org/ns/adms#                           |
| apkg-rec    | http://w3id.org/apkg/records#                        |                       
| dcat        | http://www.w3.org/ns/dcat#                           |
| dct         | http://purl.org/dc/terms/                            |
| doap        | http://usefulinc.com/ns/doap#                        |
| geo         | http://www.opengis.net/ont/geosparql#                |
| gj          | http://purl.org/geojson/vocab#                       | 
| prov        | http://www.w3.org/ns/prov#                           |
| rec         | https://www.opengis.net/def/ogc-api/records/         | 
| time        | http://www.w3.org/2006/time#                         
|



tenos de ver a hydra.

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

Table 1 - Core properties related to the catalogue record

| OGC Property   | Description                                                                              | Vocabulary Term                          | Domain                                   | Range                             | Cardinality | VES | Note |
|----------------|------------------------------------------------------------------------------------------|-------------------------|------------------------------------------|-----------------------------------|-------------|-----|------|
|  | Record  | 🔴 apkg-rec:Record                              |                                          |                                          |             |     | rdfs:subClassOf rdfs:Resource    |
| id             | A unique record identifier assigned by the server.                                       |🔴  apkg-rec:recordId                        | apkg-rec:Record                       | xsd:string                       | 1-1         |     |   owl:DatatypeProperty, rdfs:subPropertyOf rec:value
| created        | The date this record was created in the server.                                          | 🔴 apkg-rec:createdAt                               | apkg-rec:Record                             | xsd:dateTimeStamp                      | 0-1         |     |   owl:DatatypeProperty, rdfs:subPropertyOf dcterms:created  |
| updated        | The most recent date on which the record was changed.                                    | 🔴 apkg-rec:updatedAt                             | apkg-rec:Record                             | xsd:dateTimeStamp                          | 0-1         |     |     owl:DatatypeProperty with range xsd:dateTimeStamp, and make it a rdfs:subPropertyOf dcterms:modified.  |
| conformsTo     | The extensions/conformance classes used in this record                                   | 🔴 apkg-rec:conformsTo                           | apkg-rec:Record                            | dct:Standard                      | 0-M         |     |   owl:ObjectProperty, rdfs:subPropertyOf dcterms:conformsTo 
| language       | The language used for textual values (i.e., titles, descriptions, etc.) of this record. | apkg-rec:primaryLanguage                              | apkg-rec:Record                            | dct:LinguisticSystem          | 0-1         |     |  ISTO NAO FAZ SENTIDO EM RDF!!! Se o objetivo é etiquetar cada campo: a abordagem mais correta em RDF é simplesmente usar a tag de idioma no próprio literal (dcterms:title "Processo"@pt), não uma propriedade separada. Mas se querem colocar, rdfs:subPropertyOf dct:language e  |
| languages       | The list of other languages in which this record is available. | apkg-rec:recordLanguage                         | apkg-rec:Record                            | dct:LinguisticSystem         | 0-M         |     |  rdfs:subPropertyOf dct:language. Se "the list of other languages" for mesmo distinto do campo language anterior (isto é, "idioma principal" vs. "também disponível em"), a forma OWL-correta de o expressar não é definir um segundo termo semanticamente diferente, mas usar dcterms:language de forma multi-valor e, se for preciso uma distinção "principal", introduzir sub-propriedades funcionais/não-funcionais. Isto mantém as duas coisas no mesmo eixo semântico (idioma do registo) em vez de as espalhar por vocabulários diferentes.    |
| links          | A link related to this record                                                            |          🟢  rdfs:seeAlso             | apkg-rec:Record                            | xsd:anyURI                        | 0-M         |     |  Como no language, aqui a ambiguidade está em saber se "link" é mesmo uma relação semântica não tipada (então rdfs:seeAlso chega) ou se, na prática, vai sempre apontar para tipos específicos de recursos relacionados (versão anterior, documento fonte, registo duplicado), caso em que valeria a pena partir logo para sub-propriedades de dcterms:relation.    |
| linkTemplates  | A link template related to this record                                                   |            🟢 hydra:IriTemplate         | apkg-rec:Record                           |                       | 0-M         |     |   Dado que já escolhemos  rdfs:seeAlso para links, o par natural aqui é distinguir claramente as duas classes de objeto: links aponta para um recurso real (algo resolvido e navegável), enquanto linkTemplates aponta para um hydra:IriTemplate (algo que precisa de substituição de variáveis antes de ser navegável). Misturar os dois na mesma propriedade perderia essa distinção semântica, que é justamente o tipo de coisa que um reasoner consegue detetar como erro (maior precisão)   --> preciso de ver isto melhor,exemplo no excel, passar por criar uma classe? O hydra nao tem URI para Semantic Web,parece ser so uma coisa para XML

Table 2 - Core properties related to the resource.		SE AQUI É RESOURCE....PODEMOS CRIAR UMA CLASSE RESOURCE. DISCUTIR COM MARCO				

| Property OGC | Description                                                               | Vocabulary Term                          | Domain                                   | Range                             | Cardinality | VES | Note |
|--------------|---------------------------------------------------------------------|------------------------------------------|------------------------------------------|-----------------------------------|-------------|-----|------|
|      type        |          The nature or genre of the resource described by this record. |   🔴 apkg-rec:resourceType  |  apkg-rec:Record        |0-1 ??? |              |definir uma taxonomia propria? |owl:ObjectProperty, rdfs:subPropertyOf dcterms:type . Não precisamos de redeclarar rdfs:range dcterms:DCMIType em process:recordType. Pela cadeia de regras RDFS (subpropriedade → propriedade base → range). Um registo pode ter mais do que um dcterms:type em simultâneo? Se a resposta for sempre não, FunctionalProperty é a escolha certa e ganhamoss deteção de erros. Se houver casos ambíguos (por exemplo, um registo que é ao mesmo tempo "Dataset" e "Service"), então não declaramos functional, para não gerar falsos positivos de inconsistência sempre que isso acontecer.   .
|          title    | A human-readable name given to the resource described by this record.                                   | 🔴 apkg-rec:title                                | apkg-rec:Record                  | rdf:langString                      | 0-1?         |     |   owl:DatatypeProperty, rdfs:subPropertyOf dcterms:title, cardinality depends on whether a record can have titles in multiple languages: if so, don't make it functional, and instead rely on distinct language-tagged literals ("Título"@pt, "Title"@en) for the same property, which RDF already supports without any extra modelling. Escolher rdf:langString como range (em vez de xsd:string ou rdfs:Literal) é a opção mais útil aqui, porque obriga os valores a ter uma tag de idioma associada ("Título"@pt),  |
|  description            | 	A free-text description of the resource described by this record.                              | 🔴 apkg-rec:description                          | apkg-rec:Record                     | xsd:string  or rdf:langString? (obriga a tag de idioma e cardinalidade M)                | 0-M     ?    |     |   rdfs:subPropertyOf dcterms:description;xsd:string if language tagging isn't needed here. As with title, don't make it functional if descriptions can exist in multiple languages — rely on distinct language-tagged literals instead.   |
|   geometry           | A spatial extent associated with the resource described by this record. | 🟢 geo:hasGeometry                  | apkg-rec:Record                | geo:Geometry                     | 0-1         |     |   geo:hasGeometry pointing to a geo:Geometry individual with geo:asWKT "POLYGON(...)"^^geo:wktLiteral. Um exemplo: ex:record123 a apkg-rec:Record, geo:hasGeometry ex:record123-geom . ex:record123-geom a geo:Geometry,    geo:asWKT "POLYGON((-8.63 41.15, -8.60 41.15, -8.60 41.18, -8.63 41.18, -8.63 41.15))"^^geo:wktLiteral.|  
 | time | A temporal extent associated with the resource described by this record.                         |          🟢 time:hasTime           |    apkg-rec:Record                   | time:Interval   or time:Instant      | 0-1 | | ex:record123 a apkg-rec:Record, time:hasTime ex:record123-time. ex:record123-time a time:Interval, time:hasBeginning ex:record123-start time:hasEnd  ex:record123-end . ex:record123-start a time:Instant, time:inXSDDateTimeStamp "2026-01-01T00:00:00Z"^^xsd:dateTimeStamp . ex:record123-end a time:Instant, time:inXSDDateTimeStamp "2026-06-30T23:59:59Z"^^xsd:dateTimeStamp . o time:Instant é para o caso de ser somente "date" ou "timestamp".
|      keywords        | Free-form keyword or tag associated with the resource described by this record.                                | 🟢 dcat:keyword                             | apkg-rec:Record                     | rdfs:Literal                      | 0-M         |     |      |
| themes |   The subject areas, topics or categories that the record falls under, drawn from a recognised classification system or thesaurus.    | 🟢 dcat:theme    |apkg-rec:Record   | skos:Concept| 0-M| | 
| concept |The classification of the KOS defined on theme | |    | |  | | |
| resourceLanguages| The list of languages in which the resource described by this record can be retrieved. | 🔴 apkg-rec:resourceLanguage                              | apkg-rec:Record                                | dct:LinguisticSystem     | 0-M| |rdfs:subPropertyOf dct:language.
| externalIds | One or more identifiers, assigned by an external entity, for the resource described by this record. | 🟢 adms:identifier    | apkg-rec:Record                     | adms:Identifier   |     0-M     
| formats | The formats property indicates the list of available distribution formats for the resource that a record describes. These can include both physical and digital distribution formats.| 🟢 dct:formats |apkg-rec:Record   | dct::MediaTypeOrExtent| 0-M|
| contacts | A list of contacts qualified by their role(s) in association to the record or the resource described by this record. | |apkg-rec:Record   | | |
| licence| The legal provisions under which the resource described by this record is made available. | | apkg-rec:Record  |   | |
| rights| A statement that concerns all rights not addressed by the license such as a copyright statement.| | apkg-rec:Record  | | |




Table 3 - Process-extension properties related to the resource-process . SE AQUI SÂO ESPECIFICAS PARA O PROCESSO, PODEMOS CRIAR UMA CLASSE PROCESSO, SUB-CLASS THE RESOURCE

| Property OGC | Description                                                               | Vocabulary Term                          | Domain                                   | Range                             | Cardinality | VES | Note |
|--------------|---------------------------------------------------------------------|------------------------------------------|------------------------------------------|-----------------------------------|-------------|-----|------|
| __Process__| A Process Application package??? | 🔴 apkg-rec:Process| | | |  | rdfs:subClassOf apkg-rec:Resource |
|     none         | Unique identifier of the process. Pensar nisto....       |      |apkg-rec:Process          
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
|    none          | Citation of a work related to the application package               | schema:citation                          | apkg-rec:Process                  | schema:Text                       | 0-1         |   _
|     none         | License of the application package                                  | dct:license                              | apkg-rec:Process                  | dct:LicenseDocument               | 0-1         |     |      |
|    none          | Author of the application package                                   | schema:author                            | apkg-rec:Process                  | apkg:Person                       | 1-M         |     |      |
|    none          | Contributor of the application package                              | schema:contributor                       | apkg-rec:Process                  | apkg:Person                       | 0-M         |     |      |
|    none          | Maintainer of the application package                               | schema:maintainer                        | apkg-rec:Process                  | apkg:Person                       | 0-M         |     |      |
|    none          | Publisher of the application package                                | schema:publisher                         | apkg-rec:Process                  | apkg:Person                       | 0-1         |     |      |
|     none         | Organisations involved in the application package                   | schema:sourceOrganization                | apkg-rec:Process                  | apkg:Organisation                 | 1-M         |     |      |
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
