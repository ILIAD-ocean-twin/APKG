@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix voaf:<http://purl.org/vocommons/voaf#> .
@prefix schema: <http://schema.org/> .
@prefix cwl: <https://w3id.org/cwl/cwl#> .
@prefix cwltool: <http://commonwl.org/cwltool#> .
@prefix apkg: <http://purl.org/apkg#> .
@prefix time:<http://www.w3.org/2006/time#> .



  #===========  #------<>-------------------------------<>-----#  ===========#
  #===========  #------<>       CLASSES                 <>-----#  ===========#
  #===========  #------<>-------------------------------<>-----#  ===========#
                #======<>===============================<>=====#

apkg:ApplicationPackage
	a rdfs:Class;
	rdfs:label "Application Package"@en;
 	rdfs:subClassOf schema:SoftwareApplication ;
  rdfs:subClassOf schema:SoftwareSourceCode.

apkg:Person
	a rdfs:Class;
	rdfs:label "A Person"@en;
	rdfs:subClassOf foaf:Person .

apkg:Organisation
  a rdfs:Class;
  rdfs:label "An Organisation"@en;
  rdfs:subClassOf schema:Organization .

apkg:PostalAddress
  a rdfs:Class;
  rdfs:label "An Address"@en;
  rdfs:subClassOf schema:PostaLAddress .

apkg:Process
  a rdfs:Class;
  rdfs:label "A Process"@en;
  rdfs:subClassOf cwl:Process .

apkg:Parameter
  a rdfs:Class;
  rdfs:label "A Parameter (input or output)"@en;
  rdfs:subClassOf cwl:InputParameter ;
  rdfs:subClassOf cwl:OutputParameter.

apkg:Secrets
  a rdfs:Class;
  rdfs:label "The passswords of the software"@en;
  rdfs:subClassOf cwltool:Secrets.

apkg:Instant
  a rdfs:Class;
  rdfs:label "The time Instanta of the validity of the Application Package"@en;
  rdfs:subClassOf time:TemporalEntity.

apkg:TemporalCoverage
  a rdfs:Class;
  rdfs:label "The temporal coverage of the Application Package"@en;
  rdfs:subClassOf time:Instant.

apkg:Registry
  a rdfs:Class;
  rdfs:label "The Registry of the Application Package"@en.

apkg:Link
  a rdfs:Class;
  rdfs:label "The Link of the Application Package"@en.

apkg:Geometry
  a rdfs:Class;
  rdfs:label "The Geometry"@en.

              #======<>===============================<>=====#
#===========  #------<>-------------------------------<>-----#  ===========#
#===========  #------<>          Properties           <>-----#  ===========#
#===========  #------<>-------------------------------<>-----#	===========#
              #======<>===============================<>=====#

#>-----------------------------------------<#
#>           Object Properties             <#
#>-----------------------------------------<#

apkg:hasInput
  a rdf:Property, owl:ObjectProperty;
  rdfs:label "The Input of the process"@en;
  rdfs:domain apkg:Process;
  rdfs:range apkg:Parameter.

apkg:hasOutput
  a rdf:Property, owl:ObjectProperty;
  rdfs:label "The Output of the process"@en;
  rdfs:domain apkg:Process;
  rdfs:range apkg:Parameter.

apkg:hasTemporalCoverage
  a rdf:Property, owl:ObjectProperty;
  rdfs:label "The Application Package has a Time Validity"@en;
  rdfs:domain apkg:ApplicationPackage;
  rdfs:range apkg:TemporalCoverage.

apkg:hasGeometry
  a rdf:Property, owl:ObjectProperty;
  rdfs:label "The Application Package has a geometry"@en;
  rdfs:domain apkg:ApplicationPackage;
  rdfs:range apkg:Geometry.

apkg:hasLink
  a rdf:Property, owl:ObjectProperty;
  rdfs:label "The Application Package has a Link."@en;
  rdfs:domain apkg:ApplicationPackage;
  rdfs:range apkg:Link.

#>-----------------------------------------<#
#>           Data Properties             <#
#>-----------------------------------------<#
apkg:label
    a rdf:Property,owl:DataProperty;
    rdfs:label "A short, human-readable label  ."@en;
    rdfs:domain apkg:Parameter;
    rdfs:range xsd:string.

apkg:doc
	a rdf:Property,	owl:DataProperty;
	rdfs:label "A documentation string or an array of strings which should be concatenated."@en;
  rdfs:domain apkg:Parameter;
	rdfs:range xsd:string.

apkg:family
a rdf:Property,	owl:DataProperty;
	rdfs:label "The Family of the application package (identifier without version)."@en;
  rdfs:domain apkg:ApplicationPackage;
	rdfs:range xsd:anyURI.

apkg:latest
a rdf:Property,	owl:DataProperty;
	rdfs:label "Identifies the latest version of the ApplicationPackage."@en;
  rdfs:domain apkg:ApplicationPackage;
	rdfs:range xsd:boolean.

apkg:originalURL
a rdf:Property;
a rdfs:subPropertyOf schema:url;
rdfs:label "Original URL of the application package when registered."@en.

#>---------------------------------------------------------<#
#>      THE END END END END END END END END END            <#
#>---------------------------------------------------------<#
