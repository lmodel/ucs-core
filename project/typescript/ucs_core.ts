export type EntityId = string
export type NamedThingId = string
export type AdministrativeEntityId = string
export type AgentId = string
export type InformationContentEntityId = string
export type PublicationId = string
export type EvidenceTypeId = string
export type ProjectId = string
export type SystemId = string
export type SoftwareOrDeviceId = string
export type SoftwareId = string
export type HardwareId = string
export type OperatingSystemId = string
export type SolarisId = string
export type LinuxId = string
export type WindowsId = string
export type AssociationId = string
/**
 * linkml:Any type is an experimental feature for allowing arbitrary objects
 */
export interface MetaObject  {
}
/**
 * A concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a ucs compatible KG can be considered both instances of ucs classes, and OWL classes in their own right. In general you should not need to use this class directly.  Instead, use the appropriate ucs class, i.e. cso:ComputationalProcess
 */
export interface OntologyClass  {
}
/**
 * Model root class for entity annotations.
 */
export interface Annotation  {
}
/**
 * A value of an attribute that is quantitative and measurable, available as a combination of a unit and a numeric value
 */
export interface QuantityValue  extends Annotation  {
    /**
     * connects a quantity value to a unit
     */hasUnit?: string,
    /**
     * connects a quantity value to a number
     */hasNumericValue?: number,
}
/**
 * A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
 */
export interface Attribute  extends Annotation, OntologyClass  {
    /**
     * The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.
     */name?: string,
    /**
     * connects an attribute to a class that describes it
     */hasAttributeType?: OntologyClass,
    /**
     * Connects an attribute to a value
     */hasQuantitativeValue?: QuantityValue[],
    /**
     * connects an attribute to a value
     */hasQualitativeValue?: NamedThingId,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Object (person, place, text, thing, etc.) from which something (information, goods, etc.) comes or is acquired
     */src?: string,
}
/**
 * Root Universal Model class for all things and informational relationships, real or imagined.
 */
export interface Entity  {
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * a databased entity or concept/class
 */
export interface NamedThing  extends Entity  {
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * A mixin that can be used on any entity that can be taxonomically classified. This includes individual entities, their products, and other operational entities and processes.
 */
export interface ThingWithTaxon  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
}
/**
 * Relating to the arrangements and work that is needed to control the operation of a plan
 */
export interface AdministrativeEntity  extends NamedThing  {
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * person, group, organization or project that provides a piece of information (i.e. a knowledge association)
 */
export interface Agent  extends AdministrativeEntity  {
    /**
     * a professional relationship between one provider (x) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.
     */affiliation?: string,
    /**
     * Collection of information that describes the location of a building, apartment, or other structure
     */address?: string,
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * A piece of information that typically describes some topic of discourse or is used as support.
 */
export interface InformationContentEntity  extends NamedThing  {
    license?: string,
    rights?: string,
    format?: string,
    /**
     * date on which an entity was created. This can be applied to nodes or edges
     */creationDate?: date,
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed materials, either directly or in one of the Publication Csolink category subclasses.
 */
export interface Publication  extends InformationContentEntity  {
    /**
     * Connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".
     */authors?: string,
    /**
     * Page number of source referenced for statement or publication
     */pages?: string,
    /**
     * executive  summary of a publication
     */summary?: string,
    /**
     * keywords tagging a publication
     */keywords?: string,
    /**
     * Library of Congress Subject Headings (LCSH) terms tagging a publication
     */lcshTerms?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    license?: string,
    rights?: string,
    format?: string,
    /**
     * date on which an entity was created. This can be applied to nodes or edges
     */creationDate?: date,
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Class of evidence that supports an association
 */
export interface EvidenceType  extends InformationContentEntity  {
    license?: string,
    rights?: string,
    format?: string,
    /**
     * date on which an entity was created. This can be applied to nodes or edges
     */creationDate?: date,
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Collaborative enterprise, frequently involving research or design, that is carefully planned to achieve a particular aim
 */
export interface Project  extends AdministrativeEntity  {
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * An entity that intends to perform some functions, interacting with other systems. Relative to a given system, the entities with which it interacts, are considered its environment. A system is structurally composed of a set of components bound together.
 */
export interface System  extends NamedThing, ThingWithTaxon  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Either software or hardware
 */
export interface SoftwareOrDevice  extends System  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * A set of instructions in a computer programming language that can be executed by a computer, possibly after compilation into another programming language. The term Software includes ComputerPrograms (free-standing software), object methods, subroutines and software packages.
 */
export interface Software  extends SoftwareOrDevice  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * physical components of a computer
 */
export interface Hardware  extends SoftwareOrDevice  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Philosophy about free redistribution and access to a product
 */
export interface OpenSource  {
}
/**
 * An operating system (OS) is system software that manages computer hardware, software resources, and provides common services for computer programs.
 */
export interface OperatingSystem  extends Software  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * Unix operating system originally developed by Sun Microsystems
 */
export interface Solaris  extends OperatingSystem  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * family of Unix-like operating systems using Linux kernel and open source
 */
export interface Linux  extends OperatingSystem, OpenSource  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * family of computer operating systems developed by Microsoft
 */
export interface Windows  extends OperatingSystem  {
    /**
     * connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon'
     */inTaxon?: NamedThingId[],
    /**
     * The value in this nodeProperty represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     */providedBy?: string,
    /**
     * Alternate CURIEs for a thing
     */xref?: string,
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * Anchoring point (of a name) in taxonomy
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}
/**
 * computing technique for setting up virtual versions of operating systems or computer resources
 */
export interface Virtualization  {
}
/**
 * A typed association between two entities, supported by evidence
 */
export interface Association  extends Entity  {
    /**
     * Connects an association to the subject of the association. For example, in a apple-to-orange association, the apple is subject and orange is object.
     */subject?: NamedThingId,
    /**
     * A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     */predicate?: string,
    /**
     * Connects an association to the object of the association. For example, in a apple-to-orange assocation, the apple is subject and orange is object.
     */object?: NamedThingId,
    /**
     * if set to true, then the association is negated i.e. is not true
     */negated?: boolean,
    /**
     * connects an association to qualifiers that modify or qualify the meaning of that association
     */qualifiers?: OntologyClass[],
    /**
     * connects an association to publications supporting the association
     */publications?: PublicationId[],
    /**
     * connects an association to an instance of supporting evidence
     */hasEvidence?: EvidenceTypeId[],
    /**
     * A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     */id?: string,
    /**
     * An IRI for an entity. This is determined by the id using expansion rules.
     */iri?: string,
    /**
     * Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a universal model class URI.
This field is multi-valued. It should include values for ancestors of the universal class.
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base.
     */category?: string,
    /**
     * rdf:type of ucs-core:Association should be fixed at rdf:Statement
     */type?: string,
    /**
     * A human-readable name for an attribute or entity.
     */name?: string,
    /**
     * a human-readable description of an entity
     */description?: string,
    /**
     * connects any entity to an attribute
     */hasAttribute?: Attribute[],
}

