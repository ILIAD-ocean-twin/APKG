# APKG Linked Data Application Profile

🟢 $\color{green}{\rightarrow}$ a term from another ontology.
🔴 $\color{red}{\rightarrow}$ apkg-rec ontology


# 1. Namespaces
Find [here](NameSpaces.md) the list of the namespaces.


# 2. Module Core

Table A - Catalogue Record class

| id | Class | Description | Term | Notes | Table(s) |
|---|---|---|---|---|---|
| 1 | [Record](RecordClass.md) | A record in the catalogue. | 🔴 apkg-rec:Record | Inferred as dcat:Resource (domain of dcat:qualifiedRelation and dcat:keyword). | A.1.1; A.1.2 |


Table B - Classes related to the Record

| id | Class | Description | Term | Notes | Table(s) |
|---|---|---|---|---|---|
| 2 | [Address](AddressClass.md) | Physical location at which contact can be made. | 🔴 apkg-rec:Address | rdfs:subClassOf vcard:Address | B2 |
| 3 | [Concept](ConceptClass.md) | A concept of a theme. | 🔴 apkg-rec:Concept | rdfs:subClassOf skos:Concept | B3 |
| 4 | [Contact](ContactClass.md) | Identification of, and means of communication with, the party responsible for a resource. | 🔴 apkg-rec:Contact | rdfs:subClassOf prov:Agent, vcard:Kind | B4 |
| 5 | [Email](EmailClass.md) | Email address at which contact can be made. | 🔴 apkg-rec:Email | | B5 |
| 6 | [Format](FormatClass.md) | A format of the resource. | 🔴 apkg-rec:Format | rdfs:subClassOf dct:MediaTypeOrExtent | B6 |
| 7 | [Geometry](GeometryClass.md) | A GeoJSON geometry. | 🔴 apkg-rec:Geometry | rdfs:subClassOf geo:Geometry. In v3 it also takes over the role of apkg-rec:Geo. | B7 |
| 8 | [IriTemplateMapping](IriTemplateMappingClass.md) | A variable of a link template. | 🔴 apkg-rec:IriTemplateMapping | rdfs:subClassOf hydra:IriTemplateMapping | B8 |
| 9 | [Language](LanguageClass.md) | Language used for textual values. | 🔴 apkg-rec:Language | rdfs:subClassOf dct:LinguisticSystem | B9 |
| 10 | [Link](LinkClass.md) | Link related to a record. | 🔴 apkg-rec:Link | rdfs:subClassOf dcat:Relationship. Inferred as prov:Influence (dcat:qualifiedRelation is a sub-property of prov:qualifiedInfluence). | B10 |
| 11 | [LinkTemplate](LinkTemplateClass.md) | Link template related to a record. | 🔴 apkg-rec:LinkTemplate | rdfs:subClassOf hydra:IriTemplate | B11 |
| 12 | [Phone](PhoneClass.md) | Telephone number at which contact can be made. | 🔴 apkg-rec:Phone | | B12 |
| 13 | [Theme](ThemeClass.md) | A theme of the Record. | 🔴 apkg-rec:Theme | rdfs:subClassOf bf:Topic | B13 |


# 3. Module Process

Table C - Process Class

| id | Class | Description | Term | Notes | Table(s) |
|---|---|---|---|---|---|
| 14 | [Process](ProcessClass.md) | A Process: an information artefact that specifies a computation, as distinct from any execution of it. | 🔴 apkg-rec:Process | rdfs:subClassOf cwl:Process, apkg-rec:Record | C14 |

Table D - Classes related to the Process

| id | Class | Description | Term | Notes | Table(s) |
|---|---|---|---|---|---|
| 15 | [CWLDescriptor](CWLDescriptorClass.md) | The CWL descriptor of the application package. | 🔴 apkg-rec:CWLDescriptor | rdfs:subClassOf dcat:Distribution | D15 |
| 16 | [Geo](GeoClass.md) | The bounding box of a spatial coverage (schema.org GeoShape box). | 🔴 apkg-rec:Geo | rdfs:subClassOf geo:Geometry. Dropped in v3 (replaced by apkg-rec:Geometry). | D16 |
| 17 | [Organisation](OrganisationClass.md) | An Organisation. | 🔴 apkg-rec:Organisation | rdfs:subClassOf org:Organization | D17 |
| 18 | [Parameter](ParameterClass.md) | The Parameter of the Input or Output of the Process. | 🔴 apkg-rec:Parameter | rdfs:subClassOf cwl:Parameter | D18 |
| 19 | [Person](PersonClass.md) | A Person. | 🔴 apkg-rec:Person | rdfs:subClassOf foaf:Person | D19 |
<!--
| 20 | [Registry](RegistryClass.md) | The Registry where the application package is registered. | 🔴 apkg-rec:Registry | rdfs:subClassOf prov:Activity | D20 |
-->
| 20 | [SpatialCoverage](SpatialCoverageClass.md) | The Spatial Coverage of the Process. | 🔴 apkg-rec:SpatialCoverage | rdfs:subClassOf bf:GeographicCoverage. Inferred as geo:Feature (domain of geo:hasGeometry). | D20 |
| 20 | [Secret](SecretClass.md) | The input items that must be kept secret. | 🔴 apkg-rec:Secret | rdfs:subClassOf cwl:Secrets | D21 |

## Declarations for non-OWL superclasses

Some reused classes are declared only as rdfs:Class in their source vocabularies. For OWL 2 DL reasoning they are declared as owl:Class in a separate declarations module, not in the apkg-rec ontology: cwl:Process, cwl:Parameter, cwl:Secrets, hydra:IriTemplate, hydra:IriTemplateMapping, dct:LinguisticSystem, dct:MediaTypeOrExtent.

&copy; INESC TEC, 2026