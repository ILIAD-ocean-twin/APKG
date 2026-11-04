# APKG Linked Data Application Profile

🟢 $\color{green}{\rightarrow}$ a term from another ontology.
🔴 $\color{red}{\rightarrow}$ apkg-rec ontology


# 1. Namespaces
Find [here](NameSpaces.md) the list of the namespaces.


# 2. Module Core

Table A - Catalogue Record class


| id |Class | Description | Term | Notes| Table(s) |
|---|---|---|---|--|- | 
| 1 | [Record](RecordClass.md) | A record in the catalogue | 🔴 apkg-rec:Record  | rdfs:subClassOf rdfs:Resource |  A.1.1;  A.1.2 |


Table B - Classes related to the Record

| id |Class | Description | Term | Notes| Table(s) |
|---|---|---|---|--|- | 
| 2 | [Address](AddressClass.md) | Physical location at which contact can be made.| 🔴apkg-rec:Address | rdfs:subClassOf vcard:Address |  B2
| 3 | [Concept](ConceptClass.md) | A concept of a theme | 🔴 apkg-rec:Concept | | B3
| 4 | [Contact](ContactClass.md) | Identification of, and means of communication with, the responsible for a resource. | 🔴 apkg-rec:Contact | rdfs:subClassOf dct:Agent |  B4
| 5 | [Email](EmailClass.md) | Email addresses at which contact can be made. |🔴 apkg-rec:Email |  B5
| 6 | [Format](FormatClass.md) | A format of file | 🔴 apkg-rec:Format | https://schemas.opengis.net/ogcapi/records/part1/1.0/openapi/schemas/format.yaml . |  B6
| 7 | [Geometry](GeometryClass.md) | The geometry of a object | 🔴 apkg-rec:Geometry | rdfs:subClassOf geo:Geometry |  B7
| 8 | [Language](LanguageClass.md) | Language used for textual values. | 🔴 apkg-rec:Language | apkg-rec:Language rdfs:subClassOf dct:LinguisticSystem  |  B8
| 9 | [Link](LinkClass.md)    | Link related to a record    | 🔴apkg-rec:Link| apkg-rec:Link rdfs:subClassOf dcat:Relationship | | Table B9
| 10 | [LinkTemplate](LinkTemplateClass.md)    | Link template related to a record    | 🔴apkg-rec:LinkTemplate|  apkg-rec:LinkTemplate rdfs:subClassOf hydra:IriTemplate , dcat:Relationship |   B10
| 11 | [Phone](PhoneClass.md) | Telephone numbers at which contact can be made | 🔴apkg-rec:Phone |  B11
| 12 | [Theme](ThemeClass.md) | A theme of the Record | 🔴 apkg-rec:Theme | |  B12


# 3. Module Process

Table C - Process Class

| id |Class | Description | Term | Notes| Table(s) |
|---|---|---|---|--|- | 
| 13 | [Process](ProcessClass.md) | A Process, information artefact that specifies a computation, as distinct from any execution of it | 🔴 apkg-rec:Process | rdfs:subClassOf cwl:Process ; rdfs:subClassOf apkg-rec:Record .  |C13

Table D - Classes related to the Process .

| id |Class | Description | Term | Notes| Table(s) |
|---|---|---|---|--|- | 
| 14 | [CWLDescriptor](CWLDescriptorClass.md) | THe CWL descriptor of the Application package | 🔴 apkg-rec:CWLDescriptor | rdfs:subClassOf dcat:Distribution| D14
| 15 | [Geo](GeoClass.md) | A Bounding Box |  🔴 apkg-rec:Geo | | D15
| 16 | [Organisation](OrganisationClass.md) | An Organisation |  🔴 apkg-rec:Organisation |rdfs:subClassOf org:Organization  | D16
| 17 | [Parameter](ParameterClass.md) | The Parameter of the Input or Output of the Process |  🔴 apkg-rec:Parameter | rdfs:subClassOf cwl:Parameter ; cwl:Parameter a owl:Class . --> We need to define as a OWL class because in the CWL ttl it is a rdfs:Class| D17
| 18 | [Person](PersonClass.md) | A Person |  🔴 apkg-rec:Person | rdfs:subClassOf foaf:Person | D18
| 19 | [Registry](RegistryClass.md)  | The Registry where the application package is registered in. | 🔴 apkg-rec:Registry | rdfs:subClassOf prov:Activity | D19
| 20 | [SpatialCoverage](SpatialCoverageClass.md) | The Spatial Coverage of the Process |  🔴 apkg-rec:Spatialcoverage | | D20
| 21 | [Secret](SecretClass.md) | The items of the input that need to keep safe, secret |  🔴 apkg-rec:Secret |rdfs:subClassOf cwl:secrets  | D21


&copy; INESC TEC, 2026
