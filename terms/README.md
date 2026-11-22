# The __Application Package__ Application Profile V2.0 - APKG ontology

[<- main](../README.md)

This folder contains the OWL ontology of the APKG Linked Data Application Profile v2 (APKG-LDAP v2): the classes and properties that the profile defines itself (the 🔴 terms of the tables). The terms reused from other vocabularies (the 🟢 terms: DCMI, DCAT, vCard, PROV, GeoSPARQL, ...) are not redefined here; they are only used in the axioms.

## Files

| File | Ontology IRI | Prefix / namespace | Content |
|------|--------------|--------------------|---------|
| `apkg-rec-v2.ttl` | `http://w3id.org/apkg/v2/records` | `apkg-rec:` `http://w3id.org/apkg/v2/records#` | Record (Core) module, tables A.1.1, A.1.2 and B2-B13: 13 classes, 24 properties (17 datatype, 7 object) |
| `apkg-pro-v2.ttl` | `http://w3id.org/apkg/v2/process` | `apkg-pro:` `http://w3id.org/apkg/v2/process#` | Process module, tables C14 and D15-D21: 8 classes, 28 properties (20 datatype, 8 object) |
| `apkg-declarations-v2.ttl` | `http://w3id.org/apkg/v2/declarations` | (no own terms) | Declarations of reused classes that are only `rdfs:Class` in their source vocabularies |

Each ontology has `owl:versionInfo "2.0"` and an `owl:versionIRI` ending in `/2.0`.

### Modules and imports

```
apkg-pro-v2.ttl  --imports-->  apkg-rec-v2.ttl  --imports-->  apkg-declarations-v2.ttl
       \_______________________imports______________________________/
```

- **Record module** (`apkg-rec`): independent of the Process module. No axiom of `apkg-rec` mentions an `apkg-pro` term.
- **Process module** (`apkg-pro`): imports the Record module, because `apkg-pro:Process` is a subclass of `apkg-rec:Record`. Process data also uses Record classes and properties, such as `apkg-rec:Address`, `apkg-rec:Email` and `apkg-rec:mediaType`.
- **Declarations module**: declares as `owl:Class` the reused classes that are only `rdfs:Class` in their source vocabularies (`cwl:Process`, `cwl:Parameter`, `cwltool:Secrets`, `hydra:IriTemplate`, `hydra:IriTemplateMapping`, `dct:LinguisticSystem`, `dct:MediaTypeOrExtent`), so that the modules are OWL 2 DL. It is kept apart so that these declarations are not part of the APKG vocabulary itself.

## What each term carries

| Annotation | Content |
|------------|---------|
| `rdfs:label` | Name of the term (English) |
| `skos:definition` | Definition, from the Description column of the tables |
| `rdfs:comment` | Modelling notes, from the Note column (e.g. why a term was not reused) |
| `skos:editorialNote` | How the term will change in v3 ("In v3 it becomes ...") |
| `skos:scopeNote` | The table(s) of the profile where the term is defined (e.g. "APKG-LDAP v2, Table(s) C14.") |
| `rdfs:isDefinedBy` | The module (ontology IRI) that defines the term |
| `rdfs:seeAlso` | Related terms of other vocabularies that were considered but not reused (e.g. `dct:identifier`, `schema:codeRepository`) |

And the logical axioms: `rdfs:subClassOf` (alignment with the reused vocabularies), `rdfs:domain`, `rdfs:range`, `rdfs:subPropertyOf` and `owl:propertyDisjointWith`.

## Design choices

- **v2 is shaped by the v1 data.** v1 is already in production with datasets, so values that v1 holds as strings stay literals (`xsd:string` or `xsd:anyURI`) instead of IRIs or SKOS concepts. Each such term has a `skos:editorialNote` with its v3 form.
- **Shared properties.** A property used by several classes of the same module has a union domain (e.g. `apkg-rec:contactPointType` for Address, Email and Phone; `apkg-rec:rel` for Link and LinkTemplate). `apkg-rec:mediaType` is also used by `apkg-pro:CWLDescriptor`, so it has **no** `rdfs:domain`: this keeps the Record module independent of the Process module. The classes that use it are constrained in SHACL.
- **OWL 2 datatype map.** `apkg-pro:dateCreated` has no `rdfs:range`, because v1 data has both `xsd:date` and `xsd:dateTimeStamp` values and `xsd:date` is not in the OWL 2 datatype map; the datatype is checked in SHACL.
- **No sub-property of annotation properties.** `apkg-rec:alternateName` points to `rdfs:label` with `rdfs:seeAlso`, not `rdfs:subPropertyOf`, because in OWL 2 DL a datatype property cannot be a sub-property of an annotation property.
- **Inferences to be aware of.** Some reused properties classify APKG nodes through their domains, e.g. `apkg-rec:Record` is inferred as `dcat:Resource` and `geo:Feature`, `apkg-rec:Link` as `prov:Influence`, and `apkg-pro:SpatialCoverage` as `geo:Feature`. These are noted in the `rdfs:comment` of the classes.

## Using the ontology

- **Protégé**: open `apkg-pro-v2.ttl` (it imports the Record and declarations modules), or `apkg-rec-v2.ttl` for the Record module alone. The three files can also be opened from this folder in the same session.
- **Python (rdflib)**: load the three files into one graph, as `SCRIPTS/validate.py` does.

The SHACL shapes that use this ontology are in [SHACL/](../SHACL/README.md); the namespaces of all prefixes are listed in [NameSpaces.md](../NameSpaces.md).
