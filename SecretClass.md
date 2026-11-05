# APKG Linked Data Application Profile

[<- main](README.md)

## Core properties related to the Secret Class 

- Table D21
| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| secrets | The ID of the Input parameters considered secret | 🔴 apkg-rec:hasSecret | 🔴 apkg-rec:Process | 🔴 apkg-rec:Parameter | 0-M | 0-M |  | owl:ObjectProperty; rdfs:subPropertyOf apkg-rec:hasInput; rdfs:seeAlso cwltool:secrets. Each ID in the cwltool:Secrets hint is resolved to the IRI of the referenced input parameter |
