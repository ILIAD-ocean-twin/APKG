# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the CWL Descriptor Class 


- Table D15

| Property | Description | Vocabulary Term | Domain | Range | Cardinality | VES/SES | Note |
|----------|-------------|-----------------|--------|-------|-------------|---------|------|
| url (Process) | The URL of the CWL file. | 🔴 apkg-pro:descriptorURL | 🔴 apkg-pro:CWLDescriptor | xsd:anyURI | 1 | RFC 3986 (SES) | owl:DatatypeProperty. Typed literal (xsd:anyURI), not an IRI node, because of v1 data (url field of the Process, Table C14). apkg-pro:CWLDescriptor rdfs:subClassOf dcat:Distribution. In v3 it becomes dcat:downloadURL with the URL as an IRI. |
| — (constant) | The media type of the CWL file. | 🔴 apkg-rec:mediaType | 🔴 apkg-pro:CWLDescriptor | xsd:string | 1 | | owl:DatatypeProperty; no rdfs:domain declared, so that it can be used by classes of both modules (apkg-rec and apkg-pro). The classes that use it (Link, LinkTemplate, Format, CWLDescriptor) are constrained in SHACL. Not a field of the v1 JSON: fixed value "application/cwl+yaml", the media type the registry uses for the CWL (YAML) representation (url ending in ?f=cwl). Enforced with sh:hasValue "application/cwl+yaml"; sh:minCount 1; sh:maxCount 1. In v3 it becomes dcat:mediaType. |