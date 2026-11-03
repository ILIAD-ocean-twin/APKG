# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Process Class

- Table B.3.2


| Property | Description                                                               | Vocabulary Term                          | Domain                                   | Range                             | Cardinality | VES/SES | Note |
|--------------|---------------------------------------------------------------------|------------------------------------------|------------------------------------------|-----------------------------------|-------------|-----|------|
|     identifier | Unique identifier of the process. |  🔴 apkg-rec:processID |apkg-rec:Process |xsd:anyURI | 1| |owl:DatatypeProperty, rdfs:subPropertyOf dct:identifier| 
|     family | Family of this application package (identifier without version)     | 🔴 apkg-rec:familyID   | apkg-rec:Process     | xsd:string                     | 0-1         |    |   owl:DatatypeProperty, rdfs:subPropertyOf dct:identifier    |
|    software_version | The software version of the application package | 🟢pav:version    | apkg-rec:Process  |  xsd:string                    | 1 |     |      |
|    sdDatePublished | The registration date of the application package | 🟢 apkg-rec:registrationDate | apkg-rec:Process | 🔴 xsd:dateTime | 0-1 |ISO 8601 | rdfs:seeAlso dct:dateSubmitted |
|  latest | This is the latest version of the application package | 🔴 apkg-rec:isLatestVersion | apkg-rec:Process | xsd:boolean | 0-1 | | |
|    url | The Application Package as a CWL                                | 🔴 apkg-rec:cwlDescriptor                            | apkg-rec:Process                  | xsd:anyURI                      | 0-1         |     |    |
|    citation | Citation of a work related to the application package | 🔴 apkg-rec:cites | apkg-rec:Process | xsd:string | 0-1 |  
|    license | License of the application package                                  | 🟢 dct:license                              | apkg-rec:Process                  | dct:LicenseDocument               | 0-1         |     |      |
|    author | Author of the application package                                   | 🔴 apkg-rec:creator   | apkg-rec:Process  |  foaf:Person   | 1-M  |     |   rdfs:subPropertyOf dct:creator    |
|    contributor | Contributor of the application package                              | 🔴 apkg-contributor   | apkg-rec:Process  |  foaf:Person   | 0-M         |     |  rdfs:subPropertyOf  dct:contributor    |
|    maintainer | Maintainer of the application package                               | 🔴 apkg-rec:maintainer    | apkg-rec:Process            |  foaf:Person   | 0-M    |     |   rdfs:subPropertyOf  dct:contributor   |
|    sdPublisher | Publisher of the application package                                | 🔴apkg-rec:publisher      | apkg-rec:Process                  | foaf:Person       | 0-1         |     |   rdfs:subPropertyOf  dct:publisher     |
|    sourceOrganization | Organisations responsible for creating or maintaining the tool. It helps establish the origin and credibility of the tool | 🔴 apkg-rec:SourceOrganisation | apkg-rec:Process | foaf:Organization | 1-M | | (?) This should be an apkg-rec:Organisation or subClass of it |
|    provider | The service provider. The organisation(s) providing the Process as a service. | 🔴apkg-rec:ProviderOrganisation | apkg-rec:Process                  | foaf:Organization | 0-M | | (?) This should be an apkg-rec:Organisation or subClass of it |
|    producer | Main organisation responsible for the tool. It helps establish the origin and credibility of the tool. | 🔴 apkg-rec:ProducerOrganisation | apkg-rec:Process | foaf:Organization | 1 | | (?) This should be an apkg-rec:Organisation or subClass of it |
|    spatial_coverage | Spatial coverage of the application package | 🟢 bf:geographicCoverage   | apkg-rec:Process     |  🔴 apkg-rec:SpatialCoverage | 0-1 | | |
|    temporal_coverage | Indicates the period that the content applies; should be defined by a textual string indicating a time (single date or a date range). |    🔴 apkg-rec:temporalCoverage   | apkg-rec:Process |  time:Interval | 0-1 | ISO 8601 | rdfs:subPropertyOf time:hasTime |
|    code_repository | URL of the application package code repository | 🔴 apkg-rec:codeRepository | apkg-rec:Process |     doap:Repository    | 0-1 | | apkg-rec:codeRepository a owl:ObjectProperty ;     rdfs:domain apkg-rec:Process ;     rdfs:range doap:Repository ;     skos:closeMatch doap:repository, schema:codeRepository ;  --> Permite tipar o repositório com subclasses. O DOAP tem doap:GitRepository, doap:SVNRepository, doap:HgRepository   |
|    programming_language | Programming language of the application package                     |      🔴apkg-rec:programmingLanguage          | apkg-rec:Process     |   xsd:string   | 0-1         ||apkg-rec:programmingLanguage a owl:ObjectProperty ;  rdfs:domain apkg-rec:Process ;  rdfs:range skos:Concept ;  skos:closeMatch doap:programming-language, schema:programmingLanguage ;  --> Definir um SKOS com programming languages!      |
|    original_url | Original URL of the application package when registered    |    🟢 pav:retrievedFrom    | apkg-rec:Process    |     prov:Entity | 0-1 |     |  sh:property [sh:path pav:retrievedFrom ;     sh:nodeKind sh:IRI ;     sh:maxCount 1 ] .    |
|    class | Class of the Process (CommandLineTool or Workflow)                  | 🟢 dct:type |apkg:Process |      xsd:string  |     1-1  |        | ["CommandLineTool", "Workflow"] | 
|    inputs | Input of the Process   |🔴 apkg-rec:hasInput | 🔴 apkg-rec:Parameter |  apkg-rc:Process  | 0-M |    | apkg-rec:hasInput skos:exactMatch cwl:inputs  ; apkg-rec:input owl:propertyDisjointWith apkg-rec:output .  | 
|    outputs | Output of the Process    | 🔴 apkg-rec:hasOutput  | 🔴 apkg-rec:Parameter   | apkg-rec:Process   | 0-M |    |    apkg-rec:hasOutput skos:exactMatch cwl:outputs |
|    secrets | The Input parameter IDs considered secret    | 🔴 apkg-rec:hasSecret  | 🔴 apkg-rec:Secret   | apkg-rec:Process   | 0-M |  |  |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



A partir de agora nao sei o que são estas coisas, como se ligam ao Process. Sao precisas object properties. A ver com o MARCO


| Property | Description                                                               | Vocabulary Term                          | Domain                                   | Range                             | Cardinality | VES | Note |
|--------------|---------------------------------------------------------------------|------------------------------------------|------------------------------------------|-----------------------------------|-------------|-----|------|
__Organisation__                                                    |                                          |                                          | apkg:Organisation                        |             |                                 | rdfs:subClassOf schema:Organization                         |
| Name of the Organisation                                            | apkg:Organisation                        | xsd:string                               | schema:name                              | 1-1         |                                 |                                                             |
| URL of the webpage of Organisation                                  | apkg:Organisation                        |                                | schema:url                               | 1-1         |                                 |                                                             |                                   
| Address of the Organisation                                         | apkg:Organisation                        | apkg:PostalAddress                       | schema:address                           | 1-1         |                                 |                                                             |  
| __Secrets__                                                         |                                          |                                          | apkg:Secrets                             |             |                                 |  rdfs:subClassOf cwl:Secrets                                |
| The ID of the Input parameters considered secret                    | apkg:Secrets                             | xsd:string                               | cwltool:secrets                          | 0-M         |                                 |                                                             |
                                                     

&copy; INESC TEC, 2026

