# Auto generated from ucs_core.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-04-16T18:53:32
# Schema: ucs-core
#
# id: https://w3id.org/lmodel/ucs-core
# description: Classes and Properties shared across Usecases Framework
# license: Apache Software License 2.0

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Date, Double, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
AML = CurieNamespace('AML', 'https://w3id.org/i40/aml#')
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
BTO = CurieNamespace('BTO', 'http://purl.obolibrary.org/obo/BTO_')
CDAO = CurieNamespace('CDAO', 'http://purl.obolibrary.org/obo/CDAO_')
CSO = CurieNamespace('CSO', 'https://cso.kmi.open.ac.uk/topics/')
CTRL = CurieNamespace('CTRL', 'https://w3id.org/ibp/CTRLont#')
DOI = CurieNamespace('DOI', 'http://identifiers.org/doi/')
ECO = CurieNamespace('ECO', 'http://purl.obolibrary.org/obo/ECO_')
EFO = CurieNamespace('EFO', 'http://identifiers.org/efo/')
GR = CurieNamespace('GR', 'http://purl.org/goodrelations/v1#')
GSSO = CurieNamespace('GSSO', 'http://purl.obolibrary.org/obo/GSSO_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
LCSH = CurieNamespace('LCSH', 'http://id.loc.gov/authorities/subjects/')
LOINC = CurieNamespace('LOINC', 'http://loinc.org/rdf/')
MS = CurieNamespace('MS', 'http://purl.obolibrary.org/obo/MS_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBAN = CurieNamespace('OBAN', 'http://purl.org/oban/')
OIO = CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#')
OM = CurieNamespace('OM', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
ONTOAVIDA = CurieNamespace('ONTOAVIDA', 'http://purl.obolibrary.org/obo/ONTOAVIDA_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
REPR = CurieNamespace('REPR', 'https://w3id.org/reproduceme#')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
SAN = CurieNamespace('SAN', 'https://www.irit.fr/recherches/MELODI/ontologies/SAN.html#')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
SWO = CurieNamespace('SWO', 'http://purl.obolibrary.org/obo/SWO_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
XAPI = CurieNamespace('XAPI', 'http://ns.inria.fr/ludo/v1/docs/xapi.html#')
AML = CurieNamespace('aml', 'https://w3id.org/i40/aml#')
CORE = CurieNamespace('core', 'https://w3id.org/lmodel/ucs-core/')
CSRC = CurieNamespace('csrc', 'https://csrc.nist.gov/glossary/term/')
CTRL = CurieNamespace('ctrl', 'https://w3id.org/ibp/CTRLont#')
DCID = CurieNamespace('dcid', 'https://datacommons.org/browser/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DWC = CurieNamespace('dwc', 'https://dwc.tdwg.org/terms/#dc:')
EDAM_DATA = CurieNamespace('edam_data', 'http://edamontology.org/data_')
EDAM_FORMAT = CurieNamespace('edam_format', 'http://edamontology.org/format_')
EDAM_OPERATION = CurieNamespace('edam_operation', 'http://edamontology.org/operation_')
EDAM_TOPIC = CurieNamespace('edam_topic', 'http://edamontology.org/topic_')
GEOLINK = CurieNamespace('geolink', 'http://schema.geolink.org/1.0/base/main.html#')
GR = CurieNamespace('gr', 'http://purl.org/goodrelations/v1#')
GVP = CurieNamespace('gvp', 'http://vocab.getty.edu/ontology#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OM = CurieNamespace('om', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RR = CurieNamespace('rr', 'http://www.w3.org/ns/r2rml#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SSN = CurieNamespace('ssn', 'http://www.w3.org/ns/ssn/')
SSN_SYSTEM = CurieNamespace('ssn-system', 'http://www.w3.org/ns/ssn/systems/')
SUMO = CurieNamespace('sumo', 'https://w3id.org/sumo/kb/')
UBERON = CurieNamespace('uberon', 'http://purl.obolibrary.org/obo/UBERON_')
UCO_CORE = CurieNamespace('uco-core', 'https://w3id.org/lmodel/uco-core/')
UCO_IDENTITY = CurieNamespace('uco-identity', 'https://w3id.org/lmodel/uco-identity/')
UCO_OBSERVABLE = CurieNamespace('uco-observable', 'https://w3id.org/lmodel/uco-observable/')
UCO_TYPES = CurieNamespace('uco-types', 'https://w3id.org/lmodel/uco-types/')
WIKIDATA = CurieNamespace('wikidata', 'http://identifiers.org/wikidata/')
WIKIDATA_PROPERTY = CurieNamespace('wikidata_property', 'https://www.wikidata.org/wiki/Property:')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CORE


# Types
class CategoryType(Uriorcurie):
    """ A primitive type in which the value denotes a class within the universal model.  The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the universal class, for example universal:Service. For an RDF representation, the value should be a URI such as https://w3id.org/lmodel/base/vocab/Service """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "category type"
    type_model_uri = CORE.CategoryType


class IriType(Uriorcurie):
    """ An IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = CORE.IriType


class LabelType(String):
    """ A string that provides a human-readable name for an entity """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = CORE.LabelType


class PredicateType(Uriorcurie):
    """ A CURIE from the csolink related_to hierarchy. For example, schema:related_to """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "predicate type"
    type_model_uri = CORE.PredicateType


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "narrative text"
    type_model_uri = CORE.NarrativeText


class Unit(String):
    type_class_uri = UO["0000000"]
    type_class_curie = "UO:0000000"
    type_name = "unit"
    type_model_uri = CORE.Unit


# Class references
class EntityId(extended_str):
    pass


class NamedThingId(EntityId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class AgentId(AdministrativeEntityId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class EvidenceTypeId(InformationContentEntityId):
    pass


class ProjectId(AdministrativeEntityId):
    pass


class SystemId(NamedThingId):
    pass


class SoftwareOrDeviceId(SystemId):
    pass


class SoftwareId(SoftwareOrDeviceId):
    pass


class HardwareId(SoftwareOrDeviceId):
    pass


class OperatingSystemId(SoftwareId):
    pass


class SolarisId(OperatingSystemId):
    pass


class LinuxId(OperatingSystemId):
    pass


class WindowsId(OperatingSystemId):
    pass


class AssociationId(EntityId):
    pass


MetaObject = Any

class OntologyClass(YAMLRoot):
    """
    A concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a ucs compatible KG can be
    considered both instances of ucs classes, and OWL classes in their own right. In general you should not need to
    use this class directly. Instead, use the appropriate ucs class, i.e. cso:ComputationalProcess
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.OntologyClass
    class_class_curie: ClassVar[str] = "core:OntologyClass"
    class_name: ClassVar[str] = "OntologyClass"
    class_model_uri: ClassVar[URIRef] = CORE.OntologyClass


class Annotation(YAMLRoot):
    """
    Model root class for entity annotations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO-CORE.Annotation
    class_class_curie: ClassVar[str] = "uco-core:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = CORE.Annotation


@dataclass
class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, available as a combination of a unit and a numeric
    value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.QuantityValue
    class_class_curie: ClassVar[str] = "core:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = CORE.QuantityValue

    hasUnit: Optional[Union[str, Unit]] = None
    hasNumericValue: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hasUnit is not None and not isinstance(self.hasUnit, Unit):
            self.hasUnit = Unit(self.hasUnit)

        if self.hasNumericValue is not None and not isinstance(self.hasNumericValue, float):
            self.hasNumericValue = float(self.hasNumericValue)

        super().__post_init__(**kwargs)


@dataclass
class Attribute(Annotation):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age,
    crispiness. An environmental sample may have attributes such as depth, lat, long, material.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Attribute
    class_class_curie: ClassVar[str] = "core:Attribute"
    class_name: ClassVar[str] = "Attribute"
    class_model_uri: ClassVar[URIRef] = CORE.Attribute

    hasAttributeType: Union[dict, OntologyClass] = None
    name: Optional[Union[str, LabelType]] = None
    hasQuantitativeValue: Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]] = empty_list()
    hasQualitativeValue: Optional[Union[str, NamedThingId]] = None
    iri: Optional[Union[str, IriType]] = None
    src: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.hasAttributeType):
            self.MissingRequiredField("hasAttributeType")
        if not isinstance(self.hasAttributeType, OntologyClass):
            self.hasAttributeType = OntologyClass()

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if not isinstance(self.hasQuantitativeValue, list):
            self.hasQuantitativeValue = [self.hasQuantitativeValue] if self.hasQuantitativeValue is not None else []
        self.hasQuantitativeValue = [v if isinstance(v, QuantityValue) else QuantityValue(**as_dict(v)) for v in self.hasQuantitativeValue]

        if self.hasQualitativeValue is not None and not isinstance(self.hasQualitativeValue, NamedThingId):
            self.hasQualitativeValue = NamedThingId(self.hasQualitativeValue)

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        if self.src is not None and not isinstance(self.src, str):
            self.src = str(self.src)

        super().__post_init__(**kwargs)


@dataclass
class Entity(YAMLRoot):
    """
    Root Universal Model class for all things and informational relationships, real or imagined.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Entity
    class_class_curie: ClassVar[str] = "core:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = CORE.Entity

    id: Union[str, EntityId] = None
    iri: Optional[Union[str, IriType]] = None
    category: Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]] = empty_list()
    type: Optional[str] = None
    name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    hasAttribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, CategoryType) else CategoryType(v) for v in self.category]

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)

        self._normalize_inlined_as_dict(slot_name="hasAttribute", slot_type=Attribute, key_name="hasAttributeType", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = CORE.NamedThing

    id: Union[str, NamedThingId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    providedBy: Optional[Union[str, List[str]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, CategoryType) else CategoryType(v) for v in self.category]

        if not isinstance(self.providedBy, list):
            self.providedBy = [self.providedBy] if self.providedBy is not None else []
        self.providedBy = [v if isinstance(v, str) else str(v) for v in self.providedBy]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class ThingWithTaxon(YAMLRoot):
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual entities,
    their products, and other operational entities and processes.
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CORE.ThingWithTaxon
    class_class_curie: ClassVar[str] = "core:ThingWithTaxon"
    class_name: ClassVar[str] = "ThingWithTaxon"
    class_model_uri: ClassVar[URIRef] = CORE.ThingWithTaxon

    inTaxon: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.inTaxon, list):
            self.inTaxon = [self.inTaxon] if self.inTaxon is not None else []
        self.inTaxon = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.inTaxon]

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeEntity(NamedThing):
    """
    Relating to the arrangements and work that is needed to control the operation of a plan
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.AdministrativeEntity
    class_class_curie: ClassVar[str] = "core:AdministrativeEntity"
    class_name: ClassVar[str] = "AdministrativeEntity"
    class_model_uri: ClassVar[URIRef] = CORE.AdministrativeEntity

    id: Union[str, AdministrativeEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

@dataclass
class Agent(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information (i.e. a knowledge association)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Agent
    class_class_curie: ClassVar[str] = "core:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = CORE.Agent

    id: Union[str, AgentId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    affiliation: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    address: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgentId):
            self.id = AgentId(self.id)

        if not isinstance(self.affiliation, list):
            self.affiliation = [self.affiliation] if self.affiliation is not None else []
        self.affiliation = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.affiliation]

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        super().__post_init__(**kwargs)


@dataclass
class InformationContentEntity(NamedThing):
    """
    A piece of information that typically describes some topic of discourse or is used as support.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.InformationContentEntity
    class_class_curie: ClassVar[str] = "core:InformationContentEntity"
    class_name: ClassVar[str] = "InformationContentEntity"
    class_model_uri: ClassVar[URIRef] = CORE.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    license: Optional[str] = None
    rights: Optional[str] = None
    format: Optional[str] = None
    creationDate: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.rights is not None and not isinstance(self.rights, str):
            self.rights = str(self.rights)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.creationDate is not None and not isinstance(self.creationDate, XSDDate):
            self.creationDate = XSDDate(self.creationDate)

        super().__post_init__(**kwargs)


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal
    or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or
    section highlighted by NLP). The scope is intended to be general and include information published on the web, as
    well as printed materials, either directly or in one of the Publication Csolink category subclasses.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Publication
    class_class_curie: ClassVar[str] = "core:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = CORE.Publication

    id: Union[str, PublicationId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    authors: Optional[Union[str, List[str]]] = empty_list()
    pages: Optional[Union[str, List[str]]] = empty_list()
    summary: Optional[str] = None
    keywords: Optional[Union[str, List[str]]] = empty_list()
    lcshTerms: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        if not isinstance(self.pages, list):
            self.pages = [self.pages] if self.pages is not None else []
        self.pages = [v if isinstance(v, str) else str(v) for v in self.pages]

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if not isinstance(self.lcshTerms, list):
            self.lcshTerms = [self.lcshTerms] if self.lcshTerms is not None else []
        self.lcshTerms = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.lcshTerms]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.EvidenceType
    class_class_curie: ClassVar[str] = "core:EvidenceType"
    class_name: ClassVar[str] = "EvidenceType"
    class_model_uri: ClassVar[URIRef] = CORE.EvidenceType

    id: Union[str, EvidenceTypeId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Project(AdministrativeEntity):
    """
    Collaborative enterprise, frequently involving research or design, that is carefully planned to achieve a
    particular aim
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Project
    class_class_curie: ClassVar[str] = "core:Project"
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = CORE.Project

    id: Union[str, ProjectId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProjectId):
            self.id = ProjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class System(NamedThing):
    """
    An entity that intends to perform some functions, interacting with other systems. Relative to a given system, the
    entities with which it interacts, are considered its environment. A system is structurally composed of a set of
    components bound together.
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CORE.System
    class_class_curie: ClassVar[str] = "core:System"
    class_name: ClassVar[str] = "System"
    class_model_uri: ClassVar[URIRef] = CORE.System

    id: Union[str, SystemId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    inTaxon: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystemId):
            self.id = SystemId(self.id)

        if not isinstance(self.inTaxon, list):
            self.inTaxon = [self.inTaxon] if self.inTaxon is not None else []
        self.inTaxon = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.inTaxon]

        super().__post_init__(**kwargs)


@dataclass
class SoftwareOrDevice(System):
    """
    Either software or hardware
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CORE.SoftwareOrDevice
    class_class_curie: ClassVar[str] = "core:SoftwareOrDevice"
    class_name: ClassVar[str] = "SoftwareOrDevice"
    class_model_uri: ClassVar[URIRef] = CORE.SoftwareOrDevice

    id: Union[str, SoftwareOrDeviceId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

@dataclass
class Software(SoftwareOrDevice):
    """
    A set of instructions in a computer programming language that can be executed by a computer, possibly after
    compilation into another programming language. The term Software includes ComputerPrograms (free-standing
    software), object methods, subroutines and software packages.
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = UCO-CORE.Software
    class_class_curie: ClassVar[str] = "uco-core:Software"
    class_name: ClassVar[str] = "Software"
    class_model_uri: ClassVar[URIRef] = CORE.Software

    id: Union[str, SoftwareId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoftwareId):
            self.id = SoftwareId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Hardware(SoftwareOrDevice):
    """
    physical components of a computer
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CORE.Hardware
    class_class_curie: ClassVar[str] = "core:Hardware"
    class_name: ClassVar[str] = "Hardware"
    class_model_uri: ClassVar[URIRef] = CORE.Hardware

    id: Union[str, HardwareId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HardwareId):
            self.id = HardwareId(self.id)

        super().__post_init__(**kwargs)


class OpenSource(YAMLRoot):
    """
    Philosophy about free redistribution and access to a product
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.OpenSource
    class_class_curie: ClassVar[str] = "core:OpenSource"
    class_name: ClassVar[str] = "OpenSource"
    class_model_uri: ClassVar[URIRef] = CORE.OpenSource


@dataclass
class OperatingSystem(Software):
    """
    An operating system (OS) is system software that manages computer hardware, software resources, and provides
    common services for computer programs.
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = UCO-OBSERVABLE.OperatingSystem
    class_class_curie: ClassVar[str] = "uco-observable:OperatingSystem"
    class_name: ClassVar[str] = "OperatingSystem"
    class_model_uri: ClassVar[URIRef] = CORE.OperatingSystem

    id: Union[str, OperatingSystemId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OperatingSystemId):
            self.id = OperatingSystemId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Solaris(OperatingSystem):
    """
    Unix operating system originally developed by Sun Microsystems
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CORE.Solaris
    class_class_curie: ClassVar[str] = "core:Solaris"
    class_name: ClassVar[str] = "Solaris"
    class_model_uri: ClassVar[URIRef] = CORE.Solaris

    id: Union[str, SolarisId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SolarisId):
            self.id = SolarisId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Linux(OperatingSystem):
    """
    family of Unix-like operating systems using Linux kernel and open source
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CORE.Linux
    class_class_curie: ClassVar[str] = "core:Linux"
    class_name: ClassVar[str] = "Linux"
    class_model_uri: ClassVar[URIRef] = CORE.Linux

    id: Union[str, LinuxId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LinuxId):
            self.id = LinuxId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Windows(OperatingSystem):
    """
    family of computer operating systems developed by Microsoft
    """
    _inherited_slots: ClassVar[List[str]] = ["inTaxon"]

    class_class_uri: ClassVar[URIRef] = CORE.Windows
    class_class_curie: ClassVar[str] = "core:Windows"
    class_name: ClassVar[str] = "Windows"
    class_model_uri: ClassVar[URIRef] = CORE.Windows

    id: Union[str, WindowsId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsId):
            self.id = WindowsId(self.id)

        super().__post_init__(**kwargs)


class Virtualization(YAMLRoot):
    """
    computing technique for setting up virtual versions of operating systems or computer resources
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Virtualization
    class_class_curie: ClassVar[str] = "core:Virtualization"
    class_name: ClassVar[str] = "Virtualization"
    class_model_uri: ClassVar[URIRef] = CORE.Virtualization


@dataclass
class Association(Entity):
    """
    A typed association between two entities, supported by evidence
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Association
    class_class_curie: ClassVar[str] = "core:Association"
    class_name: ClassVar[str] = "Association"
    class_model_uri: ClassVar[URIRef] = CORE.Association

    id: Union[str, AssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    negated: Optional[Union[bool, Bool]] = None
    qualifiers: Optional[Union[Union[dict, OntologyClass], List[Union[dict, OntologyClass]]]] = empty_list()
    publications: Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]] = empty_list()
    hasEvidence: Optional[Union[Union[str, EvidenceTypeId], List[Union[str, EvidenceTypeId]]]] = empty_list()
    type: Optional[str] = None
    category: Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssociationId):
            self.id = AssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers] if self.qualifiers is not None else []
        self.qualifiers = [v if isinstance(v, OntologyClass) else OntologyClass(**as_dict(v)) for v in self.qualifiers]

        if not isinstance(self.publications, list):
            self.publications = [self.publications] if self.publications is not None else []
        self.publications = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.publications]

        if not isinstance(self.hasEvidence, list):
            self.hasEvidence = [self.hasEvidence] if self.hasEvidence is not None else []
        self.hasEvidence = [v if isinstance(v, EvidenceTypeId) else EvidenceTypeId(v) for v in self.hasEvidence]

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, CategoryType) else CategoryType(v) for v in self.category]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.hasAttribute = Slot(uri=CORE.hasAttribute, name="hasAttribute", curie=CORE.curie('hasAttribute'),
                   model_uri=CORE.hasAttribute, domain=Entity, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.hasAttributeType = Slot(uri=CORE.hasAttributeType, name="hasAttributeType", curie=CORE.curie('hasAttributeType'),
                   model_uri=CORE.hasAttributeType, domain=Attribute, range=Union[dict, OntologyClass])

slots.hasQualitativeValue = Slot(uri=CORE.hasQualitativeValue, name="hasQualitativeValue", curie=CORE.curie('hasQualitativeValue'),
                   model_uri=CORE.hasQualitativeValue, domain=Attribute, range=Optional[Union[str, NamedThingId]])

slots.hasQuantitativeValue = Slot(uri=CORE.hasQuantitativeValue, name="hasQuantitativeValue", curie=CORE.curie('hasQuantitativeValue'),
                   model_uri=CORE.hasQuantitativeValue, domain=Attribute, range=Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]])

slots.hasNumericValue = Slot(uri=CORE.hasNumericValue, name="hasNumericValue", curie=CORE.curie('hasNumericValue'),
                   model_uri=CORE.hasNumericValue, domain=QuantityValue, range=Optional[float])

slots.hasUnit = Slot(uri=CORE.hasUnit, name="hasUnit", curie=CORE.curie('hasUnit'),
                   model_uri=CORE.hasUnit, domain=QuantityValue, range=Optional[Union[str, Unit]])

slots.nodeProperty = Slot(uri=CORE.nodeProperty, name="nodeProperty", curie=CORE.curie('nodeProperty'),
                   model_uri=CORE.nodeProperty, domain=NamedThing, range=Optional[str])

slots.id = Slot(uri=CORE.id, name="id", curie=CORE.curie('id'),
                   model_uri=CORE.id, domain=Entity, range=Union[str, EntityId])

slots.iri = Slot(uri=CORE.iri, name="iri", curie=CORE.curie('iri'),
                   model_uri=CORE.iri, domain=None, range=Optional[Union[str, IriType]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=CORE.type, domain=None, range=Optional[str])

slots.category = Slot(uri=CORE.category, name="category", curie=CORE.curie('category'),
                   model_uri=CORE.category, domain=Entity, range=Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=CORE.name, domain=None, range=Optional[Union[str, LabelType]])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=CORE.description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.xref = Slot(uri=CORE.xref, name="xref", curie=CORE.curie('xref'),
                   model_uri=CORE.xref, domain=NamedThing, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.affiliation = Slot(uri=CORE.affiliation, name="affiliation", curie=CORE.curie('affiliation'),
                   model_uri=CORE.affiliation, domain=Agent, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.address = Slot(uri=UCO-IDENTITY.address, name="address", curie=UCO-IDENTITY.curie('address'),
                   model_uri=CORE.address, domain=None, range=Optional[str])

slots.creationDate = Slot(uri=UCO-OBSERVABLE.creationDate, name="creationDate", curie=UCO-OBSERVABLE.curie('creationDate'),
                   model_uri=CORE.creationDate, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.providedBy = Slot(uri=CORE.providedBy, name="providedBy", curie=CORE.curie('providedBy'),
                   model_uri=CORE.providedBy, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.inTaxon = Slot(uri=CORE.inTaxon, name="inTaxon", curie=CORE.curie('inTaxon'),
                   model_uri=CORE.inTaxon, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.taxonOf = Slot(uri=CORE.taxonOf, name="taxonOf", curie=CORE.curie('taxonOf'),
                   model_uri=CORE.taxonOf, domain=NamedThing, range=Optional[Union[Union[dict, "ThingWithTaxon"], List[Union[dict, "ThingWithTaxon"]]]])

slots.associationSlot = Slot(uri=CORE.associationSlot, name="associationSlot", curie=CORE.curie('associationSlot'),
                   model_uri=CORE.associationSlot, domain=Association, range=Optional[str])

slots.relatedTo = Slot(uri=CORE.relatedTo, name="relatedTo", curie=CORE.curie('relatedTo'),
                   model_uri=CORE.relatedTo, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.relatedToAtInstanceLevel = Slot(uri=CORE.relatedToAtInstanceLevel, name="relatedToAtInstanceLevel", curie=CORE.curie('relatedToAtInstanceLevel'),
                   model_uri=CORE.relatedToAtInstanceLevel, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.image = Slot(uri=CORE.image, name="image", curie=CORE.curie('image'),
                   model_uri=CORE.image, domain=None, range=Optional[str])

slots.etc_hosts = Slot(uri=CORE.etc_hosts, name="etc_hosts", curie=CORE.curie('etc_hosts'),
                   model_uri=CORE.etc_hosts, domain=None, range=Optional[str])

slots.container = Slot(uri=CORE.container, name="container", curie=CORE.curie('container'),
                   model_uri=CORE.container, domain=None, range=Optional[str])

slots.build = Slot(uri=CORE.build, name="build", curie=CORE.curie('build'),
                   model_uri=CORE.build, domain=None, range=Optional[str])

slots.data = Slot(uri=UCO-OBSERVABLE.data, name="data", curie=UCO-OBSERVABLE.curie('data'),
                   model_uri=CORE.data, domain=None, range=Optional[str])

slots.executable = Slot(uri=CORE.executable, name="executable", curie=CORE.curie('executable'),
                   model_uri=CORE.executable, domain=None, range=Optional[str])

slots.state = Slot(uri=UCO-OBSERVABLE.state, name="state", curie=UCO-OBSERVABLE.curie('state'),
                   model_uri=CORE.state, domain=Association, range=Optional[str])

slots.annotation = Slot(uri=CORE.annotation, name="annotation", curie=CORE.curie('annotation'),
                   model_uri=CORE.annotation, domain=None, range=Optional[str])

slots.authfile = Slot(uri=CORE.authfile, name="authfile", curie=CORE.curie('authfile'),
                   model_uri=CORE.authfile, domain=None, range=Optional[str])

slots.auth_file = Slot(uri=CORE.auth_file, name="auth_file", curie=CORE.curie('auth_file'),
                   model_uri=CORE.auth_file, domain=None, range=Optional[str])

slots.tag = Slot(uri=CORE.tag, name="tag", curie=CORE.curie('tag'),
                   model_uri=CORE.tag, domain=None, range=Optional[str])

slots.cgroups = Slot(uri=CORE.cgroups, name="cgroups", curie=CORE.curie('cgroups'),
                   model_uri=CORE.cgroups, domain=None, range=Optional[str])

slots.cmd_args = Slot(uri=CORE.cmd_args, name="cmd_args", curie=CORE.curie('cmd_args'),
                   model_uri=CORE.cmd_args, domain=None, range=Optional[Union[str, List[str]]])

slots.command = Slot(uri=CORE.command, name="command", curie=CORE.curie('command'),
                   model_uri=CORE.command, domain=None, range=Optional[str])

slots.cpus = Slot(uri=CORE.cpus, name="cpus", curie=CORE.curie('cpus'),
                   model_uri=CORE.cpus, domain=None, range=Optional[str])

slots.debug = Slot(uri=CORE.debug, name="debug", curie=CORE.curie('debug'),
                   model_uri=CORE.debug, domain=None, range=Optional[str])

slots.device = Slot(uri=CORE.device, name="device", curie=CORE.curie('device'),
                   model_uri=CORE.device, domain=None, range=Optional[str])

slots.dns = Slot(uri=CORE.dns, name="dns", curie=CORE.curie('dns'),
                   model_uri=CORE.dns, domain=None, range=Optional[Union[str, List[str]]])

slots.dns_option = Slot(uri=CORE.dns_option, name="dns_option", curie=CORE.curie('dns_option'),
                   model_uri=CORE.dns_option, domain=None, range=Optional[str])

slots.dns_opt = Slot(uri=CORE.dns_opt, name="dns_opt", curie=CORE.curie('dns_opt'),
                   model_uri=CORE.dns_opt, domain=None, range=Optional[str])

slots.dns_search = Slot(uri=CORE.dns_search, name="dns_search", curie=CORE.curie('dns_search'),
                   model_uri=CORE.dns_search, domain=None, range=Optional[str])

slots.env = Slot(uri=CORE.env, name="env", curie=CORE.curie('env'),
                   model_uri=CORE.env, domain=None, range=Optional[str])

slots.env_file = Slot(uri=CORE.env_file, name="env_file", curie=CORE.curie('env_file'),
                   model_uri=CORE.env_file, domain=None, range=Optional[str])

slots.path = Slot(uri=UCO-OBSERVABLE.path, name="path", curie=UCO-OBSERVABLE.curie('path'),
                   model_uri=CORE.path, domain=None, range=Optional[str])

slots.names = Slot(uri=CORE.names, name="names", curie=CORE.curie('names'),
                   model_uri=CORE.names, domain=None, range=Optional[str])

slots.separator = Slot(uri=CORE.separator, name="separator", curie=CORE.curie('separator'),
                   model_uri=CORE.separator, domain=None, range=Optional[str])

slots.share = Slot(uri=CORE.share, name="share", curie=CORE.curie('share'),
                   model_uri=CORE.share, domain=None, range=Optional[str])

slots.new = Slot(uri=CORE.new, name="new", curie=CORE.curie('new'),
                   model_uri=CORE.new, domain=None, range=Optional[str])

slots.after = Slot(uri=CORE.after, name="after", curie=CORE.curie('after'),
                   model_uri=CORE.after, domain=None, range=Optional[str])

slots.healthcheck = Slot(uri=CORE.healthcheck, name="healthcheck", curie=CORE.curie('healthcheck'),
                   model_uri=CORE.healthcheck, domain=None, range=Optional[str])

slots.healthcheck_interval = Slot(uri=CORE.healthcheck_interval, name="healthcheck_interval", curie=CORE.curie('healthcheck_interval'),
                   model_uri=CORE.healthcheck_interval, domain=None, range=Optional[str])

slots.healthcheck_retries = Slot(uri=CORE.healthcheck_retries, name="healthcheck_retries", curie=CORE.curie('healthcheck_retries'),
                   model_uri=CORE.healthcheck_retries, domain=None, range=Optional[int])

slots.healthcheck_timeout = Slot(uri=CORE.healthcheck_timeout, name="healthcheck_timeout", curie=CORE.curie('healthcheck_timeout'),
                   model_uri=CORE.healthcheck_timeout, domain=None, range=Optional[str])

slots.hostname = Slot(uri=UCO-OBSERVABLE.hostname, name="hostname", curie=UCO-OBSERVABLE.curie('hostname'),
                   model_uri=CORE.hostname, domain=None, range=Optional[str])

slots.http_proxy = Slot(uri=CORE.http_proxy, name="http_proxy", curie=CORE.curie('http_proxy'),
                   model_uri=CORE.http_proxy, domain=None, range=Optional[str])

slots.init = Slot(uri=CORE.init, name="init", curie=CORE.curie('init'),
                   model_uri=CORE.init, domain=None, range=Optional[str])

slots.interactive = Slot(uri=CORE.interactive, name="interactive", curie=CORE.curie('interactive'),
                   model_uri=CORE.interactive, domain=None, range=Optional[Union[bool, Bool]])

slots.ip = Slot(uri=UCO-OBSERVABLE.ip, name="ip", curie=UCO-OBSERVABLE.curie('ip'),
                   model_uri=CORE.ip, domain=None, range=Optional[str])

slots.label = Slot(uri=CORE.label, name="label", curie=CORE.curie('label'),
                   model_uri=CORE.label, domain=None, range=Optional[str])

slots.log_driver = Slot(uri=CORE.log_driver, name="log_driver", curie=CORE.curie('log_driver'),
                   model_uri=CORE.log_driver, domain=None, range=Optional[str])

slots.log_level = Slot(uri=CORE.log_level, name="log_level", curie=CORE.curie('log_level'),
                   model_uri=CORE.log_level, domain=None, range=Optional[str])

slots.max_size = Slot(uri=CORE.max_size, name="max_size", curie=CORE.curie('max_size'),
                   model_uri=CORE.max_size, domain=None, range=Optional[str])

slots.mac_address = Slot(uri=CORE.mac_address, name="mac_address", curie=CORE.curie('mac_address'),
                   model_uri=CORE.mac_address, domain=None, range=Optional[str])

slots.memory = Slot(uri=CORE.memory, name="memory", curie=CORE.curie('memory'),
                   model_uri=CORE.memory, domain=None, range=Optional[str])

slots.mount = Slot(uri=CORE.mount, name="mount", curie=CORE.curie('mount'),
                   model_uri=CORE.mount, domain=None, range=Optional[Union[str, List[str]]])

slots.network = Slot(uri=UCO-OBSERVABLE.network, name="network", curie=UCO-OBSERVABLE.curie('network'),
                   model_uri=CORE.network, domain=None, range=Optional[str])

slots.pid = Slot(uri=UCO-OBSERVABLE.pid, name="pid", curie=UCO-OBSERVABLE.curie('pid'),
                   model_uri=CORE.pid, domain=None, range=Optional[str])

slots.privileged = Slot(uri=CORE.privileged, name="privileged", curie=CORE.curie('privileged'),
                   model_uri=CORE.privileged, domain=None, range=Optional[Union[bool, Bool]])

slots.publish = Slot(uri=CORE.publish, name="publish", curie=CORE.curie('publish'),
                   model_uri=CORE.publish, domain=None, range=Optional[Union[str, List[str]]])

slots.read_only = Slot(uri=CORE.read_only, name="read_only", curie=CORE.curie('read_only'),
                   model_uri=CORE.read_only, domain=None, range=Optional[Union[bool, Bool]])

slots.recreate = Slot(uri=CORE.recreate, name="recreate", curie=CORE.curie('recreate'),
                   model_uri=CORE.recreate, domain=None, range=Optional[Union[bool, Bool]])

slots.rm = Slot(uri=CORE.rm, name="rm", curie=CORE.curie('rm'),
                   model_uri=CORE.rm, domain=None, range=Optional[Union[bool, Bool]])

slots.rootfs = Slot(uri=CORE.rootfs, name="rootfs", curie=CORE.curie('rootfs'),
                   model_uri=CORE.rootfs, domain=None, range=Optional[str])

slots.secrets = Slot(uri=CORE.secrets, name="secrets", curie=CORE.curie('secrets'),
                   model_uri=CORE.secrets, domain=None, range=Optional[Union[str, List[str]]])

slots.sysctl = Slot(uri=CORE.sysctl, name="sysctl", curie=CORE.curie('sysctl'),
                   model_uri=CORE.sysctl, domain=None, range=Optional[str])

slots.systemd = Slot(uri=CORE.systemd, name="systemd", curie=CORE.curie('systemd'),
                   model_uri=CORE.systemd, domain=None, range=Optional[str])

slots.timezone = Slot(uri=CORE.timezone, name="timezone", curie=CORE.curie('timezone'),
                   model_uri=CORE.timezone, domain=None, range=Optional[str])

slots.tmpfs = Slot(uri=CORE.tmpfs, name="tmpfs", curie=CORE.curie('tmpfs'),
                   model_uri=CORE.tmpfs, domain=None, range=Optional[str])

slots.tty = Slot(uri=CORE.tty, name="tty", curie=CORE.curie('tty'),
                   model_uri=CORE.tty, domain=None, range=Optional[str])

slots.ulimit = Slot(uri=CORE.ulimit, name="ulimit", curie=CORE.curie('ulimit'),
                   model_uri=CORE.ulimit, domain=None, range=Optional[str])

slots.user = Slot(uri=CORE.user, name="user", curie=CORE.curie('user'),
                   model_uri=CORE.user, domain=None, range=Optional[str])

slots.uts = Slot(uri=CORE.uts, name="uts", curie=CORE.curie('uts'),
                   model_uri=CORE.uts, domain=None, range=Optional[str])

slots.volume = Slot(uri=UCO-OBSERVABLE.volume, name="volume", curie=UCO-OBSERVABLE.curie('volume'),
                   model_uri=CORE.volume, domain=Publication, range=Optional[str])

slots.workdir = Slot(uri=CORE.workdir, name="workdir", curie=CORE.curie('workdir'),
                   model_uri=CORE.workdir, domain=None, range=Optional[str])

slots.cert_dir = Slot(uri=CORE.cert_dir, name="cert_dir", curie=CORE.curie('cert_dir'),
                   model_uri=CORE.cert_dir, domain=None, range=Optional[str])

slots.force = Slot(uri=CORE.force, name="force", curie=CORE.curie('force'),
                   model_uri=CORE.force, domain=None, range=Optional[str])

slots.cache = Slot(uri=CORE.cache, name="cache", curie=CORE.curie('cache'),
                   model_uri=CORE.cache, domain=None, range=Optional[str])

slots.file = Slot(uri=CORE.file, name="file", curie=CORE.curie('file'),
                   model_uri=CORE.file, domain=Software, range=Optional[str])

slots.format = Slot(uri=UCO-OBSERVABLE.format, name="format", curie=UCO-OBSERVABLE.curie('format'),
                   model_uri=CORE.format, domain=InformationContentEntity, range=Optional[str])

slots.password = Slot(uri=UCO-OBSERVABLE.password, name="password", curie=UCO-OBSERVABLE.curie('password'),
                   model_uri=CORE.password, domain=None, range=Optional[str])

slots.compress = Slot(uri=CORE.compress, name="compress", curie=CORE.curie('compress'),
                   model_uri=CORE.compress, domain=None, range=Optional[str])

slots.dest = Slot(uri=CORE.dest, name="dest", curie=CORE.curie('dest'),
                   model_uri=CORE.dest, domain=None, range=Optional[str])

slots.transport = Slot(uri=CORE.transport, name="transport", curie=CORE.curie('transport'),
                   model_uri=CORE.transport, domain=None, range=Optional[str])

slots.username = Slot(uri=CORE.username, name="username", curie=CORE.curie('username'),
                   model_uri=CORE.username, domain=None, range=Optional[str])

slots.validate_certs = Slot(uri=CORE.validate_certs, name="validate_certs", curie=CORE.curie('validate_certs'),
                   model_uri=CORE.validate_certs, domain=None, range=Optional[str])

slots.change = Slot(uri=CORE.change, name="change", curie=CORE.curie('change'),
                   model_uri=CORE.change, domain=None, range=Optional[str])

slots.commit_message = Slot(uri=CORE.commit_message, name="commit_message", curie=CORE.curie('commit_message'),
                   model_uri=CORE.commit_message, domain=None, range=Optional[str])

slots.src = Slot(uri=UCO-OBSERVABLE.src, name="src", curie=UCO-OBSERVABLE.curie('src'),
                   model_uri=CORE.src, domain=None, range=Optional[str])

slots.input = Slot(uri=CORE.input, name="input", curie=CORE.curie('input'),
                   model_uri=CORE.input, domain=None, range=Optional[str])

slots.certdir = Slot(uri=CORE.certdir, name="certdir", curie=CORE.curie('certdir'),
                   model_uri=CORE.certdir, domain=None, range=Optional[str])

slots.tlsverify = Slot(uri=CORE.tlsverify, name="tlsverify", curie=CORE.curie('tlsverify'),
                   model_uri=CORE.tlsverify, domain=None, range=Optional[str])

slots.tls_verify = Slot(uri=CORE.tls_verify, name="tls_verify", curie=CORE.curie('tls_verify'),
                   model_uri=CORE.tls_verify, domain=None, range=Optional[str])

slots.driver = Slot(uri=CORE.driver, name="driver", curie=CORE.curie('driver'),
                   model_uri=CORE.driver, domain=None, range=Optional[str])

slots.gateway = Slot(uri=CORE.gateway, name="gateway", curie=CORE.curie('gateway'),
                   model_uri=CORE.gateway, domain=None, range=Optional[str])

slots.internal = Slot(uri=CORE.internal, name="internal", curie=CORE.curie('internal'),
                   model_uri=CORE.internal, domain=None, range=Optional[str])

slots.ip_range = Slot(uri=CORE.ip_range, name="ip_range", curie=CORE.curie('ip_range'),
                   model_uri=CORE.ip_range, domain=None, range=Optional[str])

slots.ipv6 = Slot(uri=CORE.ipv6, name="ipv6", curie=CORE.curie('ipv6'),
                   model_uri=CORE.ipv6, domain=None, range=Optional[str])

slots.opt = Slot(uri=CORE.opt, name="opt", curie=CORE.curie('opt'),
                   model_uri=CORE.opt, domain=None, range=Optional[str])

slots.mtu = Slot(uri=CORE.mtu, name="mtu", curie=CORE.curie('mtu'),
                   model_uri=CORE.mtu, domain=None, range=Optional[str])

slots.vlan = Slot(uri=CORE.vlan, name="vlan", curie=CORE.curie('vlan'),
                   model_uri=CORE.vlan, domain=None, range=Optional[str])

slots.subnet = Slot(uri=CORE.subnet, name="subnet", curie=CORE.curie('subnet'),
                   model_uri=CORE.subnet, domain=None, range=Optional[str])

slots.quiet = Slot(uri=CORE.quiet, name="quiet", curie=CORE.curie('quiet'),
                   model_uri=CORE.quiet, domain=None, range=Optional[str])

slots.infra = Slot(uri=CORE.infra, name="infra", curie=CORE.curie('infra'),
                   model_uri=CORE.infra, domain=None, range=Optional[str])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=CORE.subject, domain=Association, range=Union[str, NamedThingId])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=CORE.object, domain=Association, range=Union[str, NamedThingId])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=CORE.predicate, domain=Association, range=Union[str, PredicateType])

slots.negated = Slot(uri=CORE.negated, name="negated", curie=CORE.curie('negated'),
                   model_uri=CORE.negated, domain=Association, range=Optional[Union[bool, Bool]])

slots.qualifiers = Slot(uri=CORE.qualifiers, name="qualifiers", curie=CORE.curie('qualifiers'),
                   model_uri=CORE.qualifiers, domain=Association, range=Optional[Union[Union[dict, OntologyClass], List[Union[dict, OntologyClass]]]])

slots.publications = Slot(uri=CORE.publications, name="publications", curie=CORE.curie('publications'),
                   model_uri=CORE.publications, domain=Association, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.hasEvidence = Slot(uri=CORE.hasEvidence, name="hasEvidence", curie=CORE.curie('hasEvidence'),
                   model_uri=CORE.hasEvidence, domain=Association, range=Optional[Union[Union[str, EvidenceTypeId], List[Union[str, EvidenceTypeId]]]])

slots.license = Slot(uri=CORE.license, name="license", curie=CORE.curie('license'),
                   model_uri=CORE.license, domain=InformationContentEntity, range=Optional[str])

slots.rights = Slot(uri=CORE.rights, name="rights", curie=CORE.curie('rights'),
                   model_uri=CORE.rights, domain=InformationContentEntity, range=Optional[str])

slots.authors = Slot(uri=CORE.authors, name="authors", curie=CORE.curie('authors'),
                   model_uri=CORE.authors, domain=Publication, range=Optional[Union[str, List[str]]])

slots.pages = Slot(uri=CORE.pages, name="pages", curie=CORE.curie('pages'),
                   model_uri=CORE.pages, domain=Publication, range=Optional[Union[str, List[str]]])

slots.summary = Slot(uri=CORE.summary, name="summary", curie=CORE.curie('summary'),
                   model_uri=CORE.summary, domain=Publication, range=Optional[str])

slots.keywords = Slot(uri=CORE.keywords, name="keywords", curie=CORE.curie('keywords'),
                   model_uri=CORE.keywords, domain=Publication, range=Optional[Union[str, List[str]]])

slots.lcshTerms = Slot(uri=CORE.lcshTerms, name="lcshTerms", curie=CORE.curie('lcshTerms'),
                   model_uri=CORE.lcshTerms, domain=Publication, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.driver_opts = Slot(uri=CORE.driver_opts, name="driver_opts", curie=CORE.curie('driver_opts'),
                   model_uri=CORE.driver_opts, domain=None, range=Optional[str])

slots.options = Slot(uri=CORE.options, name="options", curie=CORE.curie('options'),
                   model_uri=CORE.options, domain=None, range=Optional[str])

slots.Attribute_name = Slot(uri=RDFS.label, name="Attribute_name", curie=RDFS.curie('label'),
                   model_uri=CORE.Attribute_name, domain=Attribute, range=Optional[Union[str, LabelType]])

slots.NamedThing_category = Slot(uri=CORE.category, name="NamedThing_category", curie=CORE.curie('category'),
                   model_uri=CORE.NamedThing_category, domain=NamedThing, range=Union[Union[str, CategoryType], List[Union[str, CategoryType]]],
                   pattern=re.compile(r'^ucs-core:[A-Z][A-Za-z]+$'))

slots.Association_type = Slot(uri=RDF.type, name="Association_type", curie=RDF.curie('type'),
                   model_uri=CORE.Association_type, domain=Association, range=Optional[str])

slots.Association_category = Slot(uri=CORE.category, name="Association_category", curie=CORE.curie('category'),
                   model_uri=CORE.Association_category, domain=Association, range=Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]])