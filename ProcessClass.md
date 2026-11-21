# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Process Class

- Table C14


| Property | Description | Vocabulary Term | Domain | Range | Cardinality | VES/SES | Note |
|----------|-------------|-----------------|--------|-------|-------------|---------|------|
| identifier | Unique identifier of the process. | 🔴 apkg-pro:processID | 🔴 apkg-pro:Process | xsd:string | 1 | | owl:DatatypeProperty; rdfs:seeAlso dct:identifier. dct:identifier is already used for the record id, which a Process also inherits (apkg-pro:Process rdfs:subClassOf apkg-rec:Record). |
| family | Family of this application package (identifier without version). | 🔴 apkg-pro:familyID | 🔴 apkg-pro:Process | xsd:string | 0-1 | | owl:DatatypeProperty; rdfs:seeAlso dct:identifier. |
| software_version | The software version of the application package. | 🟢 pav:version | 🔴 apkg-pro:Process | xsd:string | 1 | | |
| date_created | Creation date of the application package (software, not record). | 🔴 apkg-pro:dateCreated | 🔴 apkg-pro:Process | xsd:date or xsd:dateTimeStamp | 0-1 | ISO 8601 / RFC 3339 (SES) | owl:DatatypeProperty. v1 data has both forms ("2024-12-01", "2025-05-26T10:06:27Z"): validated with sh:or ([sh:datatype xsd:date] [sh:datatype xsd:dateTimeStamp]). Not dct:created, which is used for the record creation date (Table A.1.1). |
| sdDatePublished | The registration date of the application package. | 🔴 apkg-pro:registrationDate | 🔴 apkg-pro:Process | xsd:dateTimeStamp | 0-1 | RFC 3339 (SES) | owl:DatatypeProperty; rdfs:seeAlso dct:dateSubmitted. RFC 3339 date-time requires a time offset. In v3 it becomes prov:endedAtTime on an apkg-pro:Registry activity. |
| latest | This is the latest version of the application package. | 🔴 apkg-pro:isLatestVersion | 🔴 apkg-pro:Process | xsd:boolean | 0-1 | | owl:DatatypeProperty. |
| url | The Application Package as a CWL. | 🔴 apkg-pro:cwlDescriptor | 🔴 apkg-pro:Process | 🔴 apkg-pro:CWLDescriptor | 0-1 | | owl:ObjectProperty. The URL of the descriptor is held by the apkg-pro:CWLDescriptor node (Table D15). |
| citation | Citation of a work related to the application package. | 🔴 apkg-pro:citation | 🔴 apkg-pro:Process | xsd:string | 0-M | | owl:DatatypeProperty. Free-text citation. In v3 it can become cito:cites pointing to the cited work. |
| author | Author of the application package. | 🟢 dct:creator | 🔴 apkg-pro:Process | 🔴 apkg-pro:Person | 1-M | | DCMI range dct:Agent. |
| contributor | Contributor of the application package. | 🟢 dct:contributor | 🔴 apkg-pro:Process | 🔴 apkg-pro:Person | 0-M | | DCMI range dct:Agent. |
| maintainer | Maintainer of the application package. | 🔴 apkg-pro:hasMaintainer | 🔴 apkg-pro:Process | 🔴 apkg-pro:Person | 0-M | | owl:ObjectProperty; rdfs:seeAlso dct:contributor, doap:maintainer (domain doap:Project, not reused). |
| sdPublisher | Publisher of the application package. | 🟢 dct:publisher | 🔴 apkg-pro:Process | 🔴 apkg-pro:Organisation| 0-1 | | DCMI range dct:Agent. |
| sourceOrganization | Organisations responsible for creating or maintaining the tool. It helps establish the origin and credibility of the tool. | 🔴 apkg-pro:hasSourceOrganisation | 🔴 apkg-pro:Process | 🔴 apkg-pro:Organisation | 1-M | | owl:ObjectProperty. The producer counts as a source organisation only after inference; SHACL validation of minCount must run on the inferred graph. |
| provider | The service provider. The organisation(s) providing the Process as a service. | 🔴 apkg-pro:hasProviderOrganisation | 🔴 apkg-pro:Process | 🔴 apkg-pro:Organisation | 0-M | | owl:ObjectProperty. |
| producer | Main organisation responsible for the tool. It helps establish the origin and credibility of the tool. | 🔴 apkg-pro:hasProducerOrganisation | 🔴 apkg-pro:Process | 🔴 apkg-pro:Organisation | 1 | | owl:ObjectProperty; rdfs:subPropertyOf apkg-pro:hasSourceOrganisation. |
| spatial_coverage | Spatial coverage of the application package. | 🟢 bf:geographicCoverage | 🔴 apkg-pro:Process | 🔴 apkg-pro:SpatialCoverage | 0-1 | | owl:ObjectProperty. Bounding box via geo:hasGeometry → apkg-pro:Geo (Tables D20, D16). Distinct from the Record geometry property (geo:hasGeometry → apkg-rec:Geometry), which a Process also inherits. |
| temporal_coverage | Indicates the period that the content applies; should be defined by a textual string indicating a time (single date or a date range). | 🔴 apkg-pro:temporalCoverage | 🔴 apkg-pro:Process | xsd:string | 0-1 | ISO 8601 date or interval (SES) | owl:DatatypeProperty. Plain string because of v1 data. Distinct from the Record time property (time:hasTime), which a Process also inherits. In v3 it becomes time:hasTime with time:TemporalEntity. |
| code_repository | URL of the application package code repository. | 🔴 apkg-pro:codeRepository | 🔴 apkg-pro:Process | xsd:anyURI | 0-1 | RFC 3986 (SES) | owl:DatatypeProperty. Typed literal (xsd:anyURI), not an IRI node, because of v1 data. rdfs:seeAlso schema:codeRepository. In v3 it becomes doap:repository with a doap:Repository node (doap:GitRepository, doap:SVNRepository, …). |
| programming_language | Programming language of the application package. | 🔴 apkg-pro:programmingLanguage | 🔴 apkg-pro:Process | xsd:string | 0-M | | owl:DatatypeProperty; rdfs:seeAlso doap:programming-language, schema:programmingLanguage. |
| original_url | Original URL of the application package when registered. | 🔴 apkg-pro:originalURL | 🔴 apkg-pro:Process | xsd:anyURI | 0-1 | RFC 3986 (SES) | owl:DatatypeProperty. Typed literal (xsd:anyURI), not an IRI node, because of v1 data. In v3 it becomes pav:retrievedFrom (domain and range prov:Entity, so apkg-pro:Process will be inferred as prov:Entity). |
| class | Class of the Process (CommandLineTool or Workflow). | 🔴 apkg-pro:processClass | 🔴 apkg-pro:Process | xsd:string | 1 | enum: CommandLineTool, Workflow | owl:DatatypeProperty. Plain string because of v1 data; validated with sh:in. Not dct:type, which is used for the record type. In v3 it becomes rdf:type cwl:CommandLineTool / cwl:Workflow (subclasses of cwl:Process). |
| inputs | Input of the Process. | 🔴 apkg-pro:hasInput | 🔴 apkg-pro:Process | 🔴 apkg-pro:Parameter | 0-M | | owl:ObjectProperty; rdfs:seeAlso cwl:inputs; owl:propertyDisjointWith apkg-pro:hasOutput. |
| outputs | Output of the Process. | 🔴 apkg-pro:hasOutput | 🔴 apkg-pro:Process | 🔴 apkg-pro:Parameter | 0-M | | owl:ObjectProperty; rdfs:seeAlso cwl:outputs. |
| secrets | The input parameter IDs considered secret. | 🔴 apkg-pro:hasSecret | 🔴 apkg-pro:Process | 🔴 apkg-pro:Secret | 0-M | | owl:ObjectProperty; rdfs:seeAlso cwl:hints. |

[<- main](README.md)

&copy; INESC TEC, 2026


