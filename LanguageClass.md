# APKG Linked Data Application Profile

[<- main](README.md)

## Resource properties related to the Language Class 

- Table B9

| OGC Property | Description | Vocabulary Term | Domain | Range | Cardinality OGC | Cardinality APKG | VES/SES | Note |
|--------------|-------------|-----------------|--------|-------|-----------------|------------------|---------|------|
| code | The language tag as per RFC 5646. | 🟢 skos:notation | 🔴 apkg-rec:Language | xsd:language | 1 | 1 | SES: RFC 5646 (subtags: https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) | skos:notation is an owl:DatatypeProperty. xsd:language follows BCP 47 (RFC 5646) syntax and is in the OWL 2 datatype map; it validates syntax only, not registry membership.  |
| name | The untranslated name of the language. | 🟢 skos:prefLabel | 🔴 apkg-rec:Language | rdf:langString | 0-1 | 0-1 | | The language tag of the literal is the value of code (e.g. "Português"@pt), derived at mapping time. skos:prefLabel is an owl:AnnotationProperty (no inference). |
| alternate | The name of the language in another well-understood language, usually English. | 🔴 apkg-rec:alternateName | 🔴 apkg-rec:Language | xsd:string | 0-1 | 0-1 | | owl:DatatypeProperty; rdfs:seeAlso rdfs:label (not rdfs:subPropertyOf: in OWL 2 DL a datatype property cannot be a sub-property of an annotation property). Plain string because the language of the value is not given in v1 data. In v3 it becomes skos:prefLabel with an explicit language tag. |
| dir | The direction for text in this language: ltr (left-to-right, the default), rtl (right-to-left), ttb (top-to-bottom) or btt (bottom-to-top). | 🔴 apkg-rec:textDirection | 🔴 apkg-rec:Language | xsd:string | 0-1 | 0-1 | | owl:DatatypeProperty. Values validated with sh:in ("ltr" "rtl" "ttb" "btt"); absence means ltr. rdfs:seeAlso its:dir (ITS 2.0 XML attribute). No RDF term covers ttb/btt; RDF 1.2 base direction supports only ltr/rtl and applies to literals, not to languages. |

[<- main](README.md)

### Note on Validation

SHACL Core cannot compare the language tag of a label with another value of the same node (`sh:languageIn` only accepts a fixed list), so a SHACL-SPARQL constraint is required to ensure that the language tag of `name` equals `code`. SHACL-SPARQL does not inherit Turtle prefixes, so they are declared with `sh:prefixes`.

```turtle
apkg-rec:LanguageShape a sh:NodeShape ;
    sh:targetClass apkg-rec:Language ;
    sh:property [
        sh:path skos:notation ;
        sh:datatype xsd:language ;
        sh:minCount 1 ; sh:maxCount 1 ] ;
    sh:property [
        sh:path skos:prefLabel ;
        sh:datatype rdf:langString ;
        sh:maxCount 1 ] ;
    sh:property [
        sh:path apkg-rec:alternateName ;
        sh:datatype xsd:string ;
        sh:maxCount 1 ] ;
    sh:property [
        sh:path apkg-rec:textDirection ;
        sh:datatype xsd:string ;
        sh:in ( "ltr" "rtl" "ttb" "btt" ) ;
        sh:maxCount 1 ] ;
    sh:sparql [
        sh:message "The language tag of name (skos:prefLabel) must equal code (skos:notation)." ;
        sh:prefixes apkg-rec: ;
        sh:select """
          SELECT $this ?value WHERE {
            $this skos:notation ?code ;
                  skos:prefLabel ?value .
            FILTER (LCASE(LANG(?value)) != LCASE(STR(?code)))
          }
        """ ] .

apkg-rec: sh:declare [
    sh:prefix "skos" ;
    sh:namespace "http://www.w3.org/2004/02/skos/core#"^^xsd:anyURI ] .
```
