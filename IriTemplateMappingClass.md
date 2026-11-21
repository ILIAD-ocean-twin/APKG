# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the IriTemplateMapping Class

- Table B8

> [!NOTE]
> Each entry of the OGC `variables` object of a link template (Table B11) is mapped to one apkg-rec:IriTemplateMapping node (apkg-rec:IriTemplateMapping rdfs:subClassOf hydra:IriTemplateMapping). The key of the entry is the variable name. Link templates are not used in v1 data; the class is kept for conformance with OGC API – Records.

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| (variable key) | The name of the variable in the URI template. | 🟢 hydra:variable | 🔴 apkg-rec:IriTemplateMapping | xsd:string | 1 | 1 | | The key of each entry in the OGC variables object. Must match a variable name in the URI template (RFC 6570). |
| description | A description of the variable. | 🟢 dct:description | 🔴 apkg-rec:IriTemplateMapping | xsd:string | 0-1 | 0-1 | | |
| (JSON Schema keywords) | The schema of the variable (type, enum, format, …). | — | 🔴 apkg-rec:IriTemplateMapping | — | 0-1 | — | | Not mapped in v2: Hydra has no equivalent for the JSON Schema of a variable. To be revised in v3. |

[<- main](README.md)
