# APKG-LDAP — Rationale for the Choice of Terms

The terms of the APKG-LDAP were chosen so that the resulting knowledge graph can be processed by an OWL reasoning stack while remaining interoperable with existing Linked Data. Every term was therefore selected by the same set of principles, described below.

## Selection procedure

For each element, a set of candidate terms was collected and compared on the same dimensions: definition, suitability for reasoning, advantages, disadvantages and namespace. The chosen term is the one that best satisfies the principles above.

## Mixing vocabularies

As an application profile is not bound only to a single source vocabulary. For each concept, the term that best fits the intended meaning and the reasoning requirements is chosen, whatever its namespace. Mixing is limited only by logical compatibility: combined terms must not lead to an inconsistent ontology under the reasoner.

## Matching the kind of term

Each element of the profile is filled with a term of the same kind: classes for entity types and properties for relationships and attributes. Object properties are preferred when the value is itself an entity that can be typed and described further. This lets the profile assign a range-class to a object property from a diferent namespace, for instance `bf:geographicCoverage` has as range `apkg-rec:SpatialCoverage`.

## Reuse before minting

Wherever an established vocabulary already defines the intended concept, its term is reused rather than a new one being created. Reuse makes the data immediately understandable to agents that know those vocabularies and links the profile to existing communities of practice.

## Formal OWL semantics

Because the profile must support automated reasoning, only terms with formal OWL semantics are accepted: classes declared as `owl:Class`, and properties typed as `owl:ObjectProperty` or `owl:DatatypeProperty`. Terms defined only as `rdf:Property`, as is the case in schema.org and dcterms, are excluded. Such terms leave the property type undetermined for a description-logic reasoner and cannot take part reliably in inference.

## Respect for namespace ownership

Terms from external namespaces are used as their owners define them and are never redeclared locally. The profile does not add domains, ranges or other axioms to a term it does not own. When a more specific meaning is needed, a new term is created in the profile's own namespace (`apkg-rec:`) and related to the external term through `rdfs:subClassOf` or `rdfs:subPropertyOf`. For example, `apkg-rec:Process` is declared a subclass of `cwl:Process` and of `apkg-rec:Record`, rather than altering either external definition.
