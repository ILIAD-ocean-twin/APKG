# APKG Linked Data Application Profile

# 1. NameSpaces
| Prefix         | URI                                                  |
| -------------  | -----------------------------------------------------|
| xsd            | http://www.w3.org/2001/XMLSchema#                    |
| rdf            | http://www.w3.org/1999/02/22-rdf-syntax-ns#          |
| rdfs           | http://www.w3.org/2000/01/rdf-schema# |
| adms           | http://www.w3.org/ns/adms#         ????              |
| apkg-rec       | http://w3id.org/apkg/records#                        |
| bf             | http://id.loc.gov/ontologies/bibframe/               |
| cito           | http://purl.org/spar/cito/                           |
| cwl            | https://w3id.org/cwl/cwl#                            |
| dcat           | http://www.w3.org/ns/dcat#                           |
| dct            | http://purl.org/dc/terms/                            |
| doap           | http://usefulinc.com/ns/doap#                        |
| edam           | http://edamontology.org/                             |
| fabio          | http://purl.org/spar/fabio/                          |
| foaf           | http://xmlns.com/foaf/0.1/                           |
| geo            | http://www.opengis.net/ont/geosparql#                |
| geojson        | http://purl.org/geojson/vocab#                       |
| hydra          | https://www.w3.org/ns/hydra/core#                    |
| its            | http://www.w3.org/2005/11/its/rdf#                   |
| ianaMediaType  | https://www.iana.org/assignments/media-types/        |
| ianaRelatio    | http://www.iana.org/assignments/relation/            |
| org            | http://www.w3.org/ns/org#                            |
| prof           | http://www.w3.org/ns/dx/prof/                        |
| prov           | http://www.w3.org/ns/prov#                           |
| rec            | https://www.opengis.net/def/ogc-api/records/         |
| rov            | http://www.w3.org/ns/regorg#                         |
| time           | http://www.w3.org/2006/time#                         |
|vcard           | http://www.w3.org/2006/vcard/ns#                     |
| cwltool        | http://commonwl.org/cwltool#                         |


-----------------------------------------------------------------------

# 2. Module Core

🟢 $\color{green}{\rightarrow}$ a term from another ontology.
🔴 $\color{red}{\rightarrow}$ apkg-rec ontology

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
