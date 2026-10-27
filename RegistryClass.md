

# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Registry Class 

- Table

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| none |  The agent where you registered |🟢 prov:wasAssociatedWith | apkg-rec:Activity| |1-1 | 1-1| 
| none | Date and time of registration | 🟢 prov:atTime | apkg-rec:Activity | xsd:dateTimeStamp | 0-1 | 0-1 |
| none | URL of the registration | 🟢 rdfs:seeAlso | apkg-rec:Activity  | |1-1  |1-1  | Force in SHACL :sh:property [  sh:path rdfs:seeAlso ; sh:nodeKind sh:IRI ;  sh:pattern^https://" ; sh:maxCount 1 ; ] 