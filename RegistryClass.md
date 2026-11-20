

# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Registry Class 


- Table D20

| Property | Description | Vocabulary Term | Domain | Range | Cardinality | VES/SES | Note |
|----------|-------------|-----------------|--------|-------|-------------|---------|------|
| — | The organisation where the application package was registered. | 🟢 prov:wasAssociatedWith | 🔴 apkg-rec:Registry | 🔴 apkg-rec:Organisation | 1 | | PROV-O owl:ObjectProperty; range prov:Agent, so apkg-rec:Organisation is inferred as prov:Agent. apkg-rec:Registry rdfs:subClassOf prov:Activity. |
| — | Date and time of registration. | 🟢 prov:endedAtTime | 🔴 apkg-rec:Registry | xsd:dateTimeStamp | 0-1 | RFC 3339 (SES) | PROV-O owl:DatatypeProperty (domain prov:Activity). Not prov:atTime, whose domain prov:InstantaneousEvent would infer the registry as an instantaneous event. RFC 3339 date-time requires a time offset. |
| — | URL of the registration. | 🔴 apkg-rec:registrationURL | 🔴 apkg-rec:Registry | xsd:anyURI | 1 | RFC 3986 (SES) | owl:DatatypeProperty. Typed literal (xsd:anyURI), not an IRI node, because of v1 data. Not rdfs:seeAlso (annotation property, no reasoning). Validated with sh:datatype xsd:anyURI; sh:pattern "^https://"; sh:minCount 1; sh:maxCount 1. |