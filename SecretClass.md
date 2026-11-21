# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Secret Class 



- Table D21

| Property | Description | Vocabulary Term | Domain | Range | Cardinality | VES/SES | Note |
|----------|-------------|-----------------|--------|-------|-------------|---------|------|
| secrets | The ID of an input parameter considered secret. | 🔴 apkg-rec:secretInputID | 🔴 apkg-rec:Secret | xsd:string | 1-M | | owl:DatatypeProperty; rdfs:seeAlso cwltool:secrets. Each value is the id of an input parameter of the Process (Table D18). apkg-rec:Secret represents the cwltool:Secrets hint as a whole (rdfs:subClassOf cwltool:Secrets). Not a field of the v1 JSON: derived from the hint in the CWL file. |
