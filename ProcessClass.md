# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Process Class

- Table C13

| Property | Description | Vocabulary Term | Domain | Range | Cardinality | VES/SES | Note |
|----------|-------------|-----------------|--------|-------|-------------|---------|------|
| identifier | Unique identifier of the process. | 🔴 apkg-rec:processID | 🔴 apkg-rec:Process | xsd:string | 1 |  | owl:DatatypeProperty; rdfs:seeAlso dct:identifier. dct:identifier is already used for the record id (apkg-rec:Process rdfs:subClassOf apkg-rec:Record) |
| family | Family of this application package (identifier without version) | 🔴 apkg-rec:familyID | 🔴 apkg-rec:Process | xsd:string | 0-1 |  | owl:DatatypeProperty; rdfs:seeAlso dct:identifier |
| software_version | The software version of the application package | 🟢 pav:version | 🔴 apkg-rec:Process | xsd:string | 1 |  |  |
| sdDatePublished | The registration date of the application package | 🔴 apkg-rec:registrationDate | 🔴 apkg-rec:Process | xsd:dateTimeStamp | 0-1 |  | owl:DatatypeProperty; rdfs:seeAlso dct:dateSubmitted. Alternative: prov:endedAtTime on the apkg-rec:Registry activity |
| latest | This is the latest version of the application package | 🔴 apkg-rec:isLatestVersion | 🔴 apkg-rec:Process | xsd:boolean | 0-1 |  | owl:DatatypeProperty |
| url | The Application Package as a CWL | 🔴 apkg-rec:cwlDescriptor | 🔴 apkg-rec:Process | IRI (foaf:Document) | 0-1 |  | owl:ObjectProperty |
| citation | Citation of a work related to the application package | 🟢 cito:cites | 🔴 apkg-rec:Process | IRI | 0-M |  | For DOI/URI values. If free text is needed, use a local owl:DatatypeProperty instead |
| license | License of the application package | 🟢 dct:license | 🔴 apkg-rec:Process | 🟢 dct:LicenseDocument (IRI) | 0-1 | SPDX |  |
| author | Author of the application package | 🟢 dct:creator | 🔴 apkg-rec:Process | 🔴 apkg-rec:Person | 1-M |  | DCMI range dct:Agent. Consider an agent range (persons or organisations) |
| contributor | Contributor of the application package | 🟢 dct:contributor | 🔴 apkg-rec:Process | 🔴 apkg-rec:Person | 0-M |  |  |
| maintainer | Maintainer of the application package | 🔴 apkg-rec:hasMaintainer | 🔴 apkg-rec:Process | 🔴 apkg-rec:Person | 0-M |  | owl:ObjectProperty; rdfs:seeAlso dct:contributor, doap:maintainer (domain doap:Project, not reused) |
| sdPublisher | Publisher of the application package | 🟢 dct:publisher | 🔴 apkg-rec:Process | 🔴 apkg-rec:Person | 0-1 |  | |
| sourceOrganization | Organisations responsible for creating or maintaining the tool. It helps establish the origin and credibility of the tool | 🔴 apkg-rec:hasSourceOrganisation | 🔴 apkg-rec:Process | 🔴 apkg-rec:Organisation | 1-M |  | owl:ObjectProperty |
| provider | The service provider. The organisation(s) providing the Process as a service. | 🔴 apkg-rec:hasProviderOrganisation | 🔴 apkg-rec:Process | 🔴 apkg-rec:Organisation | 0-M |  | owl:ObjectProperty |
| producer | Main organisation responsible for the tool. It helps establish the origin and credibility of the tool. | 🔴 apkg-rec:hasProducerOrganisation | 🔴 apkg-rec:Process | 🔴 apkg-rec:Organisation | 1 |  | owl:ObjectProperty; rdfs:subPropertyOf apkg-rec:hasSourceOrganisation |
| spatial_coverage | Spatial coverage of the application package | 🟢 bf:geographicCoverage | 🔴 apkg-rec:Process | 🔴 apkg-rec:SpatialCoverage | 0-1 |  | Bounding box following the schema.org box syntax |
| temporal_coverage | Indicates the period that the content applies; should be defined by a textual string indicating a time (single date or a date range). | 🔴 apkg-rec:temporalCoverage | 🔴 apkg-rec:Process | 🟢 time:TemporalEntity | 0-1 |  | owl:ObjectProperty; rdfs:subPropertyOf time:hasTime (time:hasTime is already used for the record temporal extent). time:Interval or time:Instant |
| code_repository | URL of the application package code repository | 🔴 apkg-rec:codeRepository | 🔴 apkg-rec:Process | 🟢 doap:Repository | 0-1 |  | owl:ObjectProperty; rdfs:seeAlso doap:repository, schema:codeRepository. Allows doap:GitRepository, doap:SVNRepository, doap:HgRepository |
| programming_language | Programming language of the application package | 🔴 apkg-rec:programmingLanguage | 🔴 apkg-rec:Process | IRI (skos:Concept) | 0-M | Programming languages SKOS (TODO) | owl:ObjectProperty; rdfs:seeAlso doap:programming-language, schema:programmingLanguage |
| original_url | Original URL of the application package when registered | 🟢 pav:retrievedFrom | 🔴 apkg-rec:Process | IRI (prov:Entity) | 0-1 |  | PAV domain/range prov:Entity: apkg-rec:Process is inferred as prov:Entity (disjoint with prov:Activity) |
| class | Class of the Process (CommandLineTool or Workflow) | 🟢 rdf:type | 🔴 apkg-rec:Process | cwl:CommandLineTool or cwl:Workflow | 1 | CWL classes | Both are subclasses of cwl:Process. dct:type is already used for the record type |
| inputs | Input of the Process | 🔴 apkg-rec:hasInput | 🔴 apkg-rec:Process | 🔴 apkg-rec:Parameter | 0-M |  | owl:ObjectProperty; rdfs:seeAlso cwl:inputs; owl:propertyDisjointWith apkg-rec:hasOutput |
| outputs | Output of the Process | 🔴 apkg-rec:hasOutput | 🔴 apkg-rec:Process | 🔴 apkg-rec:Parameter | 0-M |  | owl:ObjectProperty; rdfs:seeAlso cwl:outputs |
| secrets | The Input parameter IDs considered secret | 🔴 apkg-rec:hasSecret | 🔴 apkg-rec:Process | 🔴 apkg-rec:Parameter | 0-M |  | owl:ObjectProperty; rdfs:subPropertyOf apkg-rec:hasInput (secrets are inferred as inputs, hence never outputs) |

&copy; INESC TEC, 2026

