# APKG Linked Data Application Profile

The APKG Linked Data Application Profile (APKG-LDAP) describes the records of the [Application Package registry](https://iliad-registry.inesctec.pt/collections/apkg/items?f=html) as Linked Data. It is a semantic uplift of the OGC API - Records catalogue record, extended with the description of the application package itself (a CWL Process: a CommandLineTool or a Workflow).

This is **version 2** of the profile. It keeps the current registry data (v1) unchanged: values that v1 holds as strings stay literals, and the notes "In v3 it becomes ..." in the tables say how each term will change in version 3, which will be fully aligned with Semantic Web principles.

## Repository contents

| Folder / file | Content |
|---------------|---------|
| This README and the `*Class.md` files | The profile: one table per class, with the OGC/CWL property, the vocabulary term, domain, range, cardinalities, value encoding schemes and notes |
| [NameSpaces.md](NameSpaces.md) | The prefixes and namespaces used in the profile |
| [terms/](terms/README.md) | The OWL ontology: Record module (`apkg-rec`), Process module (`apkg-pro`) and declarations module |
| [shacl/](shacl/README.md) | The SHACL shapes to validate data against the profile |
| [examples/](examples/README.md) | Registry records converted to Turtle and JSON-LD, and the source JSON |
| [scripts/](scripts/README.md) | Scripts to download the registry, convert JSON to RDF (Turtle, JSON-LD) and validate |
| [skos/](skos/) | The RFC 5646 language subtag registry as a SKOS concept scheme |
| [APKG-LDAP — Rationale for the Choice of Terms.md](APKG-LDAP%20—%20Rationale%20for%20the%20Choice%20of%20Terms.md) | Rationale for the choice of terms |

## Quick start

Open a terminal in the root folder of the repository (see [scripts/README.md](scripts/README.md) for the requirements):

```
python scripts\download_registry.py --with-cwl --convert    download all records, convert and validate
python scripts\json2rdf.py record.json --format both        convert one record to Turtle and JSON-LD
python scripts\validate.py                                  validate the files in examples\
```

## Legend

🟢 $\color{green}{\rightarrow}$ a term from another ontology.
🔴 $\color{red}{\rightarrow}$ APKG ontology: apkg-rec (module Core, tables A and B) or apkg-pro (module Process, tables C and D)


## 1. Namespaces
Find [here](NameSpaces.md) the list of the namespaces.


## 2. Module Core

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
| 7 | [Geometry](GeometryClass.md) | A GeoJSON geometry. | 🔴 apkg-rec:Geometry | rdfs:subClassOf geo:Geometry. In v3 it also takes over the role of apkg-pro:Geo. | B7 |
| 8 | [IriTemplateMapping](IriTemplateMappingClass.md) | A variable of a link template. | 🔴 apkg-rec:IriTemplateMapping | rdfs:subClassOf hydra:IriTemplateMapping | B8 |
| 9 | [Language](LanguageClass.md) | Language used for textual values. | 🔴 apkg-rec:Language | rdfs:subClassOf dct:LinguisticSystem | B9 |
| 10 | [Link](LinkClass.md) | Link related to a record. | 🔴 apkg-rec:Link | rdfs:subClassOf dcat:Relationship. Inferred as prov:Influence (dcat:qualifiedRelation is a sub-property of prov:qualifiedInfluence). | B10 |
| 11 | [LinkTemplate](LinkTemplateClass.md) | Link template related to a record. | 🔴 apkg-rec:LinkTemplate | rdfs:subClassOf hydra:IriTemplate | B11 |
| 12 | [Phone](PhoneClass.md) | Telephone number at which contact can be made. | 🔴 apkg-rec:Phone | | B12 |
| 13 | [Theme](ThemeClass.md) | A theme of the Record. | 🔴 apkg-rec:Theme | rdfs:subClassOf bf:Topic | B13 |


## 3. Module Process

Table C - Process Class

| id | Class | Description | Term | Notes | Table(s) |
|---|---|---|---|---|---|
| 14 | [Process](ProcessClass.md) | A Process: an information artefact that specifies a computation, as distinct from any execution of it. | 🔴 apkg-pro:Process | rdfs:subClassOf cwl:Process, apkg-rec:Record | C14 |

Table D - Classes related to the Process

| id | Class | Description | Term | Notes | Table(s) |
|---|---|---|---|---|---|
| 15 | [CWLDescriptor](CWLDescriptorClass.md) | The CWL descriptor of the application package. | 🔴 apkg-pro:CWLDescriptor | rdfs:subClassOf dcat:Distribution | D15 |
| 16 | [Geo](GeoClass.md) | The bounding box of a spatial coverage (schema.org GeoShape box). | 🔴 apkg-pro:Geo | rdfs:subClassOf geo:Geometry. Dropped in v3 (replaced by apkg-rec:Geometry). | D16 |
| 17 | [Organisation](OrganisationClass.md) | An Organisation. | 🔴 apkg-pro:Organisation | rdfs:subClassOf org:Organization | D17 |
| 18 | [Parameter](ParameterClass.md) | The Parameter of the Input or Output of the Process. | 🔴 apkg-pro:Parameter | rdfs:subClassOf cwl:Parameter | D18 |
| 19 | [Person](PersonClass.md) | A Person. | 🔴 apkg-pro:Person | rdfs:subClassOf foaf:Person | D19 |
| 20 | [SpatialCoverage](SpatialCoverageClass.md) | The Spatial Coverage of the Process. | 🔴 apkg-pro:SpatialCoverage | rdfs:subClassOf bf:GeographicCoverage. Inferred as geo:Feature (domain of geo:hasGeometry). | D20 |
| 21 | [Secret](SecretClass.md) | The input items that must be kept secret. | 🔴 apkg-pro:Secret | rdfs:subClassOf cwltool:Secrets | D21 |

> [!NOTE]
>Declarations for non-OWL superclasses. 
>Some reused classes are declared only as rdfs:Class in their source vocabularies. For OWL 2 DL reasoning they are declared as owl:Class in a separate declarations module ([terms/apkg-declarations-v2.ttl](terms/apkg-declarations-v2.ttl)), not in the APKG ontology (apkg-rec / apkg-pro): cwl:Process, cwl:Parameter, cwltool:Secrets, hydra:IriTemplate, hydra:IriTemplateMapping, dct:LinguisticSystem, dct:MediaTypeOrExtent.

&copy; INESC TEC, 2026