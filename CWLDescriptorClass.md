# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the CWL Descriptor Class 


- Table D15

| Property | Description | Vocabulary Term | Domain | Range | Cardinality | VES/SES | Note |
|----------|-------------|-----------------|--------|-------|-------------|---------|------|
| url (Process) | The URL of the CWL file. | 🔴 apkg-rec:descriptorURL | 🔴 apkg-rec:CWLDescriptor | xsd:anyURI | 1 | RFC 3986 (SES) | owl:DatatypeProperty. Typed literal (xsd:anyURI), not an IRI node, because of v1 data (url field of the Process, Table C14). apkg-rec:CWLDescriptor rdfs:subClassOf dcat:Distribution. In v3 it becomes dcat:downloadURL with the URL as an IRI. |
| — (constant) | The media type of the CWL file. | 🔴 apkg-rec:mediaType | 🔴 apkg-rec:CWLDescriptor | xsd:string | 1 | | owl:DatatypeProperty, shared with apkg-rec:Link, apkg-rec:LinkTemplate and apkg-rec:Format (domain: union of the four). Not present in v1 data: fixed value enforced with sh:hasValue "application/x-cwl"; sh:minCount 1; sh:maxCount 1. application/x-cwl is not registered at IANA, so no IANA IRI is used. In v3 it becomes dcat:mediaType. |