# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Language Class 

- Table B.3.2


| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|-----|------|
| code | The language tag as per RFC-5646. | 🟢 skos:notation | 🔴 apkg-rec:Language | xsd:language | 1 | 1 | SES: RFC 5646 (subtags: https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) | xsd:language follows BCP 47 (RFC 5646) syntax and is in the OWL 2 datatype map. It validates syntax only, not registry membership. |
| name | The untranslated name of the language. | 🟢 skos:prefLabel | 🔴 apkg-rec:Language | rdf:langString | 0-1 | 0-1 |  | Language tag of the literal = value of code (e.g. "Português"@pt) |
| alternate | The name of the language in another well-understood language, usually English. | 🟢 skos:prefLabel | 🔴 apkg-rec:Language | rdf:langString | 0-1 | 0-1 |  | prefLabel with a language tag different from code (e.g. "Portuguese"@en). SKOS allows one prefLabel per language. |
| dir | The direction for text in this language. (…) | 🔴 apkg-rec:textDirection | 🔴 apkg-rec:Language | xsd:string | 0-1 | 0-1 |  | Values: ltr; rtl; ttb; btt; default: ltr (SHACL sh:in). rdfs:seeAlso its:dir (ITS 2.0 XML attribute; no RDF term covers ttb/btt) |

### Note on Validation.

The SHACL core cannot compare the label with another value of the node (sh:languageIn only accepts a fixed list), so a SHACL-SPARQL constraint is required. For example, to ensure a maximum of one alternate:
```turtle
apkg-rec:LanguageShape sh:sparql [
    sh:message "At most one prefLabel in a language other than code (alternate)." ;
    sh:select """
      SELECT $this WHERE {
        $this skos:notation ?code ; skos:prefLabel ?l .
        FILTER(!langMatches(lang(?l), str(?code)))
      } GROUP BY $this HAVING (COUNT(?l) > 1)
    """ ] .
```