# APKG Linked Data Application Profile

🟢 $\color{green}{\rightarrow}$ a term from another ontology.
🔴 $\color{red}{\rightarrow}$ apkg-rec ontology


# 1. Namespaces
Find [here](NameSpaces.md) the list of the namespaces.


# 2. Module Core

Table A - Core classes related to the catalogue record


| id |Class | Description | Term | Notes| Table(s) |
|---|---|---|---|--|- | 
| 1 | [Record](RecordClass.md) | A record in the catalogue | 🔴 apkg-rec:Record  | rdfs:subClassOf rdfs:Resource | Table A.1.1; Table A.1.2 |
| 2 | [Link](LinkClass.md)    | A link related to this record    | 🔴apkg-rec:Link| apkg-rec:Link rdfs:subClassOf dcat:Relationship | Table A.2.1 | 
| 3 | [LinkTemplate](LinkTemplateClass.md)    | A link template related to this record    | 🔴apkg-rec:LinkTemplae|  apkg-rec:LinkTemplate rdfs:subClassOf hydra:IriTemplate , dcat:Relationship | Table A.3.1 | 


Table B - Core classes related to the resource

| id |Class | Description | Term | Notes| Table(s) |
|---|---|---|---|--|- | 
| 4 | [Geometry](GeometryClass.md) | The geometry of the object | 🔴 apkg-rec:Geometry | rdfs:subClassOf geo:Geometry |
| 5 | [Theme](ThemeClass.md) | A theme of the Record | 🔴 apkg-rec:Theme | |
| 6 | [Concept](ConceptClass.md) | A concept of the theme | 🔴 apkg-rec:Concept | |
| 7 | [Format](FormatClass.md) | A format of file | 🔴 apkg-rec:Format | https://schemas.opengis.net/ogcapi/records/part1/1.0/openapi/schemas/format.yaml . |
| 8 | [Contact](ContactClass.md) | A contact of the record | 🔴 apkg-rec:Contact | rdfs:subClassOf dct:Agent |
| 9 | [Language](LanguageClass.md) | The language used for textual values in this record | 🔴 apkg-rec:Language | apkg-rec:Language rdfs:subClassOf dct:LinguisticSystem  |
| 10  | [Address](AddressClass.md) | The Physical location at which contact can be made.| 🔴apkg-rec:Address | rdfs:subClassOf vcard:Address |
| 11 | [Email](EmailClass.md) | Email addresses at which contact can be made. |🔴 apkg-rec:Email |
| 12 | [Phone](PhoneClass.md) | Telephone numbers at which contact can be made | 🔴apkg-rec:Phone |


# 3. Module Process

Table C - Extension classes related to the Process .

| id |Class | Description | Term | Notes| Table(s) |
|---|---|---|---|--|- | 
| 13 | [Process](ProcessClass.md) | A Process | 🔴 apkg-rec:Process | rdfs:subClassOf cwl:Process ; rdfs:subClassOf apkg-rec:Record .  
| 14 | [Registry](RegistryClass.md)  | The Registry where the application package is registered in. | 🔴 apkg-rec:Registry | rdfs:subClassOf prov:Activity |
| 15 | [CWLDescriptor](CWLDescriptorClass.md) | THe CWL descriptor of the Application package | 🔴 apkg-rec:CWLDescriptor | rdfs:subClassOf dcat:Distribution| 
| 16 | [Parameter](ParameterClass.md) | The Parameter of the Input or Output of the Process |  🔴 apkg-rec:Parameter | rdfs:subClassOf cwl:Parameter ; cwl:Parameter a owl:Class . --> We need to define as a OWL class because in the CWL ttl it is a rdfs:Class|
| 17 | [SpatialCoverage](SpatialCoverageClass.md) | The Spatial Coverage of the Process |  🔴 apkg-rec:Spatialcoverage | |
| 18 | [Geo](GeoClass.md) | A Bounding Box |  🔴 apkg-rec:Geo | |
| 19 | [Person](PersonClass.md) | A Person |  🔴 apkg-rec:Person | rdfs:subClassOf foaf:Person |
| 20 | [Organisation](OrganisationClass.md) | An Organisation |  🔴 apkg-rec:Organisation |rdfs:subClassOf org:Organization  |
| 21 | [Secret](SecretClass.md) | The items of the input that need to keep safe, secret |  🔴 apkg-rec:Secret |rdfs:subClassOf cwl:secrets  |


&copy; INESC TEC, 2026
