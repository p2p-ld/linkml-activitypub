# Auto generated from activitystreams.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-01-14T21:50:38
# Schema: linkml-activitystreams
#
# id: https://github.com/p2p_ld/linkml-activitypub
# description: LinkML representation of ActivityStreams 2 Schema.
# license: GNU GPL v3.0

import dataclasses
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
from linkml_runtime.linkml_model.types import Datetime, Float, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
AS = CurieNamespace('as', 'http://www.w3.org/ns/activitystreams#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
UNIT = CurieNamespace('unit', 'http://qudt.org/2.1/vocab/unit/')
XML = CurieNamespace('xml', 'http://www.w3.org/XML/1998/namespace')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = AS


# Types
class AnyURI(String):
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "anyURI"
    type_model_uri = AS.AnyURI


class DurationType(String):
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "durationType"
    type_model_uri = AS.DurationType


class NonNegativeInteger(Integer):
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "nonNegativeInteger"
    type_model_uri = AS.NonNegativeInteger


class LangString(String):
    type_class_uri = RDF["langString"]
    type_class_curie = "rdf:langString"
    type_name = "langString"
    type_model_uri = AS.LangString


# Class references



class Property(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF["Property"]
    class_class_curie: ClassVar[str] = "rdf:Property"
    class_name: ClassVar[str] = "Property"
    class_model_uri: ClassVar[URIRef] = AS.Property


class Statement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF["Statement"]
    class_class_curie: ClassVar[str] = "rdf:Statement"
    class_name: ClassVar[str] = "Statement"
    class_model_uri: ClassVar[URIRef] = AS.Statement


@dataclass
class Object(YAMLRoot):
    """
    Describes an object of any kind. The Object type serves as the base type for most of the other kinds of objects
    defined in the Activity Vocabulary, including other Core types such as Activity, IntransitiveActivity, Collection
    and OrderedCollection.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Object"]
    class_class_curie: ClassVar[str] = "as:Object"
    class_name: ClassVar[str] = "Object"
    class_model_uri: ClassVar[URIRef] = AS.Object

    attachment: Optional[Union[str, List[str]]] = empty_list()
    attributedTo: Optional[Union[str, List[str]]] = empty_list()
    audience: Optional[Union[str, List[str]]] = empty_list()
    bcc: Optional[Union[str, List[str]]] = empty_list()
    bto: Optional[Union[str, List[str]]] = empty_list()
    cc: Optional[Union[str, List[str]]] = empty_list()
    content: Optional[Union[str, List[str]]] = empty_list()
    context: Optional[Union[str, List[str]]] = empty_list()
    generator: Optional[Union[str, List[str]]] = empty_list()
    icon: Optional[Union[str, List[str]]] = empty_list()
    image: Optional[Union[str, List[str]]] = empty_list()
    inReplyTo: Optional[Union[str, List[str]]] = empty_list()
    location: Optional[Union[str, List[str]]] = empty_list()
    name: Optional[Union[str, List[str]]] = empty_list()
    preview: Optional[Union[str, List[str]]] = empty_list()
    replies: Optional[Union[dict, "Collection"]] = None
    summary: Optional[Union[str, List[str]]] = empty_list()
    tag: Optional[Union[str, List[str]]] = empty_list()
    to: Optional[Union[str, List[str]]] = empty_list()
    url: Optional[Union[str, List[str]]] = empty_list()
    duration: Optional[Union[str, DurationType]] = None
    endTime: Optional[Union[str, XSDDateTime]] = None
    id: Optional[Union[str, AnyURI]] = None
    mediaType: Optional[str] = None
    published: Optional[Union[str, XSDDateTime]] = None
    startTime: Optional[Union[str, XSDDateTime]] = None
    updated: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.attachment, list):
            self.attachment = [self.attachment] if self.attachment is not None else []
        self.attachment = [v if isinstance(v, str) else str(v) for v in self.attachment]

        if not isinstance(self.attributedTo, list):
            self.attributedTo = [self.attributedTo] if self.attributedTo is not None else []
        self.attributedTo = [v if isinstance(v, str) else str(v) for v in self.attributedTo]

        if not isinstance(self.audience, list):
            self.audience = [self.audience] if self.audience is not None else []
        self.audience = [v if isinstance(v, str) else str(v) for v in self.audience]

        if not isinstance(self.bcc, list):
            self.bcc = [self.bcc] if self.bcc is not None else []
        self.bcc = [v if isinstance(v, str) else str(v) for v in self.bcc]

        if not isinstance(self.bto, list):
            self.bto = [self.bto] if self.bto is not None else []
        self.bto = [v if isinstance(v, str) else str(v) for v in self.bto]

        if not isinstance(self.cc, list):
            self.cc = [self.cc] if self.cc is not None else []
        self.cc = [v if isinstance(v, str) else str(v) for v in self.cc]

        if not isinstance(self.content, list):
            self.content = [self.content] if self.content is not None else []
        self.content = [v if isinstance(v, str) else str(v) for v in self.content]

        if not isinstance(self.context, list):
            self.context = [self.context] if self.context is not None else []
        self.context = [v if isinstance(v, str) else str(v) for v in self.context]

        if not isinstance(self.generator, list):
            self.generator = [self.generator] if self.generator is not None else []
        self.generator = [v if isinstance(v, str) else str(v) for v in self.generator]

        if not isinstance(self.icon, list):
            self.icon = [self.icon] if self.icon is not None else []
        self.icon = [v if isinstance(v, str) else str(v) for v in self.icon]

        if not isinstance(self.image, list):
            self.image = [self.image] if self.image is not None else []
        self.image = [v if isinstance(v, str) else str(v) for v in self.image]

        if not isinstance(self.inReplyTo, list):
            self.inReplyTo = [self.inReplyTo] if self.inReplyTo is not None else []
        self.inReplyTo = [v if isinstance(v, str) else str(v) for v in self.inReplyTo]

        if not isinstance(self.location, list):
            self.location = [self.location] if self.location is not None else []
        self.location = [v if isinstance(v, str) else str(v) for v in self.location]

        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if not isinstance(self.preview, list):
            self.preview = [self.preview] if self.preview is not None else []
        self.preview = [v if isinstance(v, str) else str(v) for v in self.preview]

        if self.replies is not None and not isinstance(self.replies, Collection):
            self.replies = Collection(**as_dict(self.replies))

        if not isinstance(self.summary, list):
            self.summary = [self.summary] if self.summary is not None else []
        self.summary = [v if isinstance(v, str) else str(v) for v in self.summary]

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, str) else str(v) for v in self.tag]

        if not isinstance(self.to, list):
            self.to = [self.to] if self.to is not None else []
        self.to = [v if isinstance(v, str) else str(v) for v in self.to]

        if not isinstance(self.url, list):
            self.url = [self.url] if self.url is not None else []
        self.url = [v if isinstance(v, str) else str(v) for v in self.url]

        if self.duration is not None and not isinstance(self.duration, DurationType):
            self.duration = DurationType(self.duration)

        if self.endTime is not None and not isinstance(self.endTime, XSDDateTime):
            self.endTime = XSDDateTime(self.endTime)

        if self.id is not None and not isinstance(self.id, AnyURI):
            self.id = AnyURI(self.id)

        if self.mediaType is not None and not isinstance(self.mediaType, str):
            self.mediaType = str(self.mediaType)

        if self.published is not None and not isinstance(self.published, XSDDateTime):
            self.published = XSDDateTime(self.published)

        if self.startTime is not None and not isinstance(self.startTime, XSDDateTime):
            self.startTime = XSDDateTime(self.startTime)

        if self.updated is not None and not isinstance(self.updated, XSDDateTime):
            self.updated = XSDDateTime(self.updated)

        super().__post_init__(**kwargs)


@dataclass
class Link(YAMLRoot):
    """
    A Link is an indirect, qualified reference to a resource identified by a URL. The fundamental model for links is
    established by [ RFC5988]. Many of the properties defined by the Activity Vocabulary allow values that are either
    instances of Object or Link. When a Link is used, it establishes a qualified relation connecting the subject (the
    containing object) to the resource identified by the href. Properties of the Link are properties of the reference
    as opposed to properties of the resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Link"]
    class_class_curie: ClassVar[str] = "as:Link"
    class_name: ClassVar[str] = "Link"
    class_model_uri: ClassVar[URIRef] = AS.Link

    name: Optional[Union[str, List[str]]] = empty_list()
    preview: Optional[Union[str, List[str]]] = empty_list()
    height: Optional[Union[int, NonNegativeInteger]] = None
    href: Optional[Union[str, AnyURI]] = None
    hreflang: Optional[str] = None
    id: Optional[Union[str, AnyURI]] = None
    mediaType: Optional[str] = None
    rel: Optional[Union[str, List[str]]] = empty_list()
    width: Optional[Union[int, NonNegativeInteger]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if not isinstance(self.preview, list):
            self.preview = [self.preview] if self.preview is not None else []
        self.preview = [v if isinstance(v, str) else str(v) for v in self.preview]

        if self.height is not None and not isinstance(self.height, NonNegativeInteger):
            self.height = NonNegativeInteger(self.height)

        if self.href is not None and not isinstance(self.href, AnyURI):
            self.href = AnyURI(self.href)

        if self.hreflang is not None and not isinstance(self.hreflang, str):
            self.hreflang = str(self.hreflang)

        if self.id is not None and not isinstance(self.id, AnyURI):
            self.id = AnyURI(self.id)

        if self.mediaType is not None and not isinstance(self.mediaType, str):
            self.mediaType = str(self.mediaType)

        if not isinstance(self.rel, list):
            self.rel = [self.rel] if self.rel is not None else []
        self.rel = [v if isinstance(v, str) else str(v) for v in self.rel]

        if self.width is not None and not isinstance(self.width, NonNegativeInteger):
            self.width = NonNegativeInteger(self.width)

        super().__post_init__(**kwargs)


@dataclass
class Activity(Object):
    """
    An Activity is a subtype of Object that describes some form of action that may happen, is currently happening, or
    has already happened. The Activity type itself serves as an abstract base type for all types of activities. It is
    important to note that the Activity type itself does not carry any specific semantics about the kind of action
    being taken.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Activity"]
    class_class_curie: ClassVar[str] = "as:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = AS.Activity

    actor: Optional[Union[str, List[str]]] = empty_list()
    instrument: Optional[Union[str, List[str]]] = empty_list()
    object: Optional[Union[str, List[str]]] = empty_list()
    origin: Optional[Union[str, List[str]]] = empty_list()
    result: Optional[Union[str, List[str]]] = empty_list()
    target: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.actor, list):
            self.actor = [self.actor] if self.actor is not None else []
        self.actor = [v if isinstance(v, str) else str(v) for v in self.actor]

        if not isinstance(self.instrument, list):
            self.instrument = [self.instrument] if self.instrument is not None else []
        self.instrument = [v if isinstance(v, str) else str(v) for v in self.instrument]

        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, str) else str(v) for v in self.object]

        if not isinstance(self.origin, list):
            self.origin = [self.origin] if self.origin is not None else []
        self.origin = [v if isinstance(v, str) else str(v) for v in self.origin]

        if not isinstance(self.result, list):
            self.result = [self.result] if self.result is not None else []
        self.result = [v if isinstance(v, str) else str(v) for v in self.result]

        if not isinstance(self.target, list):
            self.target = [self.target] if self.target is not None else []
        self.target = [v if isinstance(v, str) else str(v) for v in self.target]

        super().__post_init__(**kwargs)


class IntransitiveActivity(Activity):
    """
    ['An Activity that has no direct object@en']
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["IntransitiveActivity"]
    class_class_curie: ClassVar[str] = "as:IntransitiveActivity"
    class_name: ClassVar[str] = "IntransitiveActivity"
    class_model_uri: ClassVar[URIRef] = AS.IntransitiveActivity


@dataclass
class Collection(Object):
    """
    A Collection is a subtype of Object that represents ordered or unordered sets of Object or Link instances. Refer
    to the Activity Streams 2.0 Core specification for a complete description of the Collection type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Collection"]
    class_class_curie: ClassVar[str] = "as:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = AS.Collection

    current: Optional[str] = None
    first: Optional[str] = None
    items: Optional[Union[str, List[str]]] = empty_list()
    last: Optional[str] = None
    totalItems: Optional[Union[int, NonNegativeInteger]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.current is not None and not isinstance(self.current, str):
            self.current = str(self.current)

        if self.first is not None and not isinstance(self.first, str):
            self.first = str(self.first)

        if not isinstance(self.items, list):
            self.items = [self.items] if self.items is not None else []
        self.items = [v if isinstance(v, str) else str(v) for v in self.items]

        if self.last is not None and not isinstance(self.last, str):
            self.last = str(self.last)

        if self.totalItems is not None and not isinstance(self.totalItems, NonNegativeInteger):
            self.totalItems = NonNegativeInteger(self.totalItems)

        super().__post_init__(**kwargs)


@dataclass
class OrderedCollection(Collection):
    """
    A subtype of Collection in which members of the logical collection are assumed to always be strictly ordered.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["OrderedCollection"]
    class_class_curie: ClassVar[str] = "as:OrderedCollection"
    class_name: ClassVar[str] = "OrderedCollection"
    class_model_uri: ClassVar[URIRef] = AS.OrderedCollection

    items: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.items, list):
            self.items = [self.items] if self.items is not None else []
        self.items = [v if isinstance(v, str) else str(v) for v in self.items]

        super().__post_init__(**kwargs)


@dataclass
class CollectionPage(Collection):
    """
    Used to represent distinct subsets of items from a Collection. Refer to the Activity Streams 2.0 Core for a
    complete description of the CollectionPage object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["CollectionPage"]
    class_class_curie: ClassVar[str] = "as:CollectionPage"
    class_name: ClassVar[str] = "CollectionPage"
    class_model_uri: ClassVar[URIRef] = AS.CollectionPage

    next: Optional[str] = None
    partOf: Optional[str] = None
    prev: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.next is not None and not isinstance(self.next, str):
            self.next = str(self.next)

        if self.partOf is not None and not isinstance(self.partOf, str):
            self.partOf = str(self.partOf)

        if self.prev is not None and not isinstance(self.prev, str):
            self.prev = str(self.prev)

        super().__post_init__(**kwargs)


@dataclass
class OrderedCollectionPage(OrderedCollection):
    """
    Used to represent ordered subsets of items from an OrderedCollection. Refer to the Activity Streams 2.0 Core for a
    complete description of the OrderedCollectionPage object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["OrderedCollectionPage"]
    class_class_curie: ClassVar[str] = "as:OrderedCollectionPage"
    class_name: ClassVar[str] = "OrderedCollectionPage"
    class_model_uri: ClassVar[URIRef] = AS.OrderedCollectionPage

    startIndex: Optional[Union[int, NonNegativeInteger]] = None
    next: Optional[str] = None
    partOf: Optional[str] = None
    prev: Optional[str] = None
    items: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.startIndex is not None and not isinstance(self.startIndex, NonNegativeInteger):
            self.startIndex = NonNegativeInteger(self.startIndex)

        if self.next is not None and not isinstance(self.next, str):
            self.next = str(self.next)

        if self.partOf is not None and not isinstance(self.partOf, str):
            self.partOf = str(self.partOf)

        if self.prev is not None and not isinstance(self.prev, str):
            self.prev = str(self.prev)

        if not isinstance(self.items, list):
            self.items = [self.items] if self.items is not None else []
        self.items = [v if isinstance(v, str) else str(v) for v in self.items]

        super().__post_init__(**kwargs)


class Accept(Activity):
    """
    Indicates that the actor accepts the object. The target property can be used in certain circumstances to indicate
    the context into which the object has been accepted.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Accept"]
    class_class_curie: ClassVar[str] = "as:Accept"
    class_name: ClassVar[str] = "Accept"
    class_model_uri: ClassVar[URIRef] = AS.Accept


class TentativeAccept(Accept):
    """
    A specialization of Accept indicating that the acceptance is tentative.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["TentativeAccept"]
    class_class_curie: ClassVar[str] = "as:TentativeAccept"
    class_name: ClassVar[str] = "TentativeAccept"
    class_model_uri: ClassVar[URIRef] = AS.TentativeAccept


class Add(Activity):
    """
    Indicates that the actor has added the object to the target. If the target property is not explicitly specified,
    the target would need to be determined implicitly by context. The origin can be used to identify the context from
    which the object originated.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Add"]
    class_class_curie: ClassVar[str] = "as:Add"
    class_name: ClassVar[str] = "Add"
    class_model_uri: ClassVar[URIRef] = AS.Add


class Arrive(IntransitiveActivity):
    """
    An IntransitiveActivity that indicates that the actor has arrived at the location. The origin can be used to
    identify the context from which the actor originated. The target typically has no defined meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Arrive"]
    class_class_curie: ClassVar[str] = "as:Arrive"
    class_name: ClassVar[str] = "Arrive"
    class_model_uri: ClassVar[URIRef] = AS.Arrive


class Create(Activity):
    """
    Indicates that the actor has created the object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Create"]
    class_class_curie: ClassVar[str] = "as:Create"
    class_name: ClassVar[str] = "Create"
    class_model_uri: ClassVar[URIRef] = AS.Create


class Delete(Activity):
    """
    Indicates that the actor has deleted the object. If specified, the origin indicates the context from which the
    object was deleted.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Delete"]
    class_class_curie: ClassVar[str] = "as:Delete"
    class_name: ClassVar[str] = "Delete"
    class_model_uri: ClassVar[URIRef] = AS.Delete


class Follow(Activity):
    """
    Indicates that the actor is "following" the object. Following is defined in the sense typically used within Social
    systems in which the actor is interested in any activity performed by or on the object. The target and origin
    typically have no defined meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Follow"]
    class_class_curie: ClassVar[str] = "as:Follow"
    class_name: ClassVar[str] = "Follow"
    class_model_uri: ClassVar[URIRef] = AS.Follow


class Ignore(Activity):
    """
    Indicates that the actor is ignoring the object. The target and origin typically have no defined meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Ignore"]
    class_class_curie: ClassVar[str] = "as:Ignore"
    class_name: ClassVar[str] = "Ignore"
    class_model_uri: ClassVar[URIRef] = AS.Ignore


class Join(Activity):
    """
    Indicates that the actor has joined the object. The target and origin typically have no defined meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Join"]
    class_class_curie: ClassVar[str] = "as:Join"
    class_name: ClassVar[str] = "Join"
    class_model_uri: ClassVar[URIRef] = AS.Join


class Leave(Activity):
    """
    Indicates that the actor has left the object. The target and origin typically have no meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Leave"]
    class_class_curie: ClassVar[str] = "as:Leave"
    class_name: ClassVar[str] = "Leave"
    class_model_uri: ClassVar[URIRef] = AS.Leave


class Like(Activity):
    """
    Indicates that the actor likes, recommends or endorses the object. The target and origin typically have no defined
    meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Like"]
    class_class_curie: ClassVar[str] = "as:Like"
    class_name: ClassVar[str] = "Like"
    class_model_uri: ClassVar[URIRef] = AS.Like


class Offer(Activity):
    """
    Indicates that the actor is offering the object. If specified, the target indicates the entity to which the object
    is being offered.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Offer"]
    class_class_curie: ClassVar[str] = "as:Offer"
    class_name: ClassVar[str] = "Offer"
    class_model_uri: ClassVar[URIRef] = AS.Offer


class Invite(Offer):
    """
    A specialization of Offer in which the actor is extending an invitation for the object to the target.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Invite"]
    class_class_curie: ClassVar[str] = "as:Invite"
    class_name: ClassVar[str] = "Invite"
    class_model_uri: ClassVar[URIRef] = AS.Invite


class Reject(Activity):
    """
    Indicates that the actor is rejecting the object. The target and origin typically have no defined meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Reject"]
    class_class_curie: ClassVar[str] = "as:Reject"
    class_name: ClassVar[str] = "Reject"
    class_model_uri: ClassVar[URIRef] = AS.Reject


class TentativeReject(Reject):
    """
    A specialization of Reject in which the rejection is considered tentative.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["TentativeReject"]
    class_class_curie: ClassVar[str] = "as:TentativeReject"
    class_name: ClassVar[str] = "TentativeReject"
    class_model_uri: ClassVar[URIRef] = AS.TentativeReject


class Remove(Activity):
    """
    Indicates that the actor is removing the object. If specified, the origin indicates the context from which the
    object is being removed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Remove"]
    class_class_curie: ClassVar[str] = "as:Remove"
    class_name: ClassVar[str] = "Remove"
    class_model_uri: ClassVar[URIRef] = AS.Remove


class Undo(Activity):
    """
    Indicates that the actor is undoing the object. In most cases, the object will be an Activity describing some
    previously performed action (for instance, a person may have previously "liked" an article but, for whatever
    reason, might choose to undo that like at some later point in time). The target and origin typically have no
    defined meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Undo"]
    class_class_curie: ClassVar[str] = "as:Undo"
    class_name: ClassVar[str] = "Undo"
    class_model_uri: ClassVar[URIRef] = AS.Undo


class Update(Activity):
    """
    Indicates that the actor has updated the object. Note, however, that this vocabulary does not define a mechanism
    for describing the actual set of modifications made to object. The target and origin typically have no defined
    meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Update"]
    class_class_curie: ClassVar[str] = "as:Update"
    class_name: ClassVar[str] = "Update"
    class_model_uri: ClassVar[URIRef] = AS.Update


class View(Activity):
    """
    Indicates that the actor has viewed the object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["View"]
    class_class_curie: ClassVar[str] = "as:View"
    class_name: ClassVar[str] = "View"
    class_model_uri: ClassVar[URIRef] = AS.View


class Listen(Activity):
    """
    Indicates that the actor has listened to the object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Listen"]
    class_class_curie: ClassVar[str] = "as:Listen"
    class_name: ClassVar[str] = "Listen"
    class_model_uri: ClassVar[URIRef] = AS.Listen


class Read(Activity):
    """
    Indicates that the actor has read the object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Read"]
    class_class_curie: ClassVar[str] = "as:Read"
    class_name: ClassVar[str] = "Read"
    class_model_uri: ClassVar[URIRef] = AS.Read


class Move(Activity):
    """
    Indicates that the actor has moved object from origin to target. If the origin or target are not specified, either
    can be determined by context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Move"]
    class_class_curie: ClassVar[str] = "as:Move"
    class_name: ClassVar[str] = "Move"
    class_model_uri: ClassVar[URIRef] = AS.Move


class Travel(IntransitiveActivity):
    """
    Indicates that the actor is traveling to target from origin. Travel is an IntransitiveObject whose actor specifies
    the direct object. If the target or origin are not specified, either can be determined by context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Travel"]
    class_class_curie: ClassVar[str] = "as:Travel"
    class_name: ClassVar[str] = "Travel"
    class_model_uri: ClassVar[URIRef] = AS.Travel


class Announce(Activity):
    """
    Indicates that the actor is calling the target's attention the object. The origin typically has no defined meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Announce"]
    class_class_curie: ClassVar[str] = "as:Announce"
    class_name: ClassVar[str] = "Announce"
    class_model_uri: ClassVar[URIRef] = AS.Announce


class Block(Ignore):
    """
    Indicates that the actor is blocking the object. Blocking is a stronger form of Ignore. The typical use is to
    support social systems that allow one user to block activities or content of other users. The target and origin
    typically have no defined meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Block"]
    class_class_curie: ClassVar[str] = "as:Block"
    class_name: ClassVar[str] = "Block"
    class_model_uri: ClassVar[URIRef] = AS.Block


class Flag(Activity):
    """
    Indicates that the actor is "flagging" the object. Flagging is defined in the sense common to many social
    platforms as reporting content as being inappropriate for any number of reasons.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Flag"]
    class_class_curie: ClassVar[str] = "as:Flag"
    class_name: ClassVar[str] = "Flag"
    class_model_uri: ClassVar[URIRef] = AS.Flag


class Dislike(Activity):
    """
    Indicates that the actor dislikes the object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Dislike"]
    class_class_curie: ClassVar[str] = "as:Dislike"
    class_name: ClassVar[str] = "Dislike"
    class_model_uri: ClassVar[URIRef] = AS.Dislike


@dataclass
class Question(IntransitiveActivity):
    """
    Represents a question being asked. Question objects are an extension of IntransitiveActivity. That is, the
    Question object is an Activity, but the direct object is the question itself and therefore it would not contain an
    object property.
    Either of the anyOf and oneOf properties MAY be used to express possible answers, but a Question object MUST NOT
    have both properties.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Question"]
    class_class_curie: ClassVar[str] = "as:Question"
    class_name: ClassVar[str] = "Question"
    class_model_uri: ClassVar[URIRef] = AS.Question

    anyOf: Optional[Union[str, List[str]]] = empty_list()
    oneOf: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.anyOf, list):
            self.anyOf = [self.anyOf] if self.anyOf is not None else []
        self.anyOf = [v if isinstance(v, str) else str(v) for v in self.anyOf]

        if not isinstance(self.oneOf, list):
            self.oneOf = [self.oneOf] if self.oneOf is not None else []
        self.oneOf = [v if isinstance(v, str) else str(v) for v in self.oneOf]

        super().__post_init__(**kwargs)


class Application(Object):
    """
    Describes a software application.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Application"]
    class_class_curie: ClassVar[str] = "as:Application"
    class_name: ClassVar[str] = "Application"
    class_model_uri: ClassVar[URIRef] = AS.Application


class Group(Object):
    """
    Represents a formal or informal collective of Actors.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Group"]
    class_class_curie: ClassVar[str] = "as:Group"
    class_name: ClassVar[str] = "Group"
    class_model_uri: ClassVar[URIRef] = AS.Group


class Organization(Object):
    """
    Represents an organization.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Organization"]
    class_class_curie: ClassVar[str] = "as:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = AS.Organization


class Person(Object):
    """
    Represents an individual person.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Person"]
    class_class_curie: ClassVar[str] = "as:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = AS.Person


class Service(Object):
    """
    Represents a service of any kind.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Service"]
    class_class_curie: ClassVar[str] = "as:Service"
    class_name: ClassVar[str] = "Service"
    class_model_uri: ClassVar[URIRef] = AS.Service


@dataclass
class Relationship(Object):
    """
    Describes a relationship between two individuals. The subject and object properties are used to identify the
    connected individuals.
    See 5.2 Representing Relationships Between Entities for additional information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Relationship"]
    class_class_curie: ClassVar[str] = "as:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = AS.Relationship

    object: Optional[Union[str, List[str]]] = empty_list()
    relationship: Optional[Union[Union[dict, Object], List[Union[dict, Object]]]] = empty_list()
    subject: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, str) else str(v) for v in self.object]

        if not isinstance(self.relationship, list):
            self.relationship = [self.relationship] if self.relationship is not None else []
        self.relationship = [v if isinstance(v, Object) else Object(**as_dict(v)) for v in self.relationship]

        if not isinstance(self.subject, list):
            self.subject = [self.subject] if self.subject is not None else []
        self.subject = [v if isinstance(v, str) else str(v) for v in self.subject]

        super().__post_init__(**kwargs)


class Document(Object):
    """
    Represents a document of any kind.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Document"]
    class_class_curie: ClassVar[str] = "as:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = AS.Document


class Article(Object):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Article"]
    class_class_curie: ClassVar[str] = "as:Article"
    class_name: ClassVar[str] = "Article"
    class_model_uri: ClassVar[URIRef] = AS.Article


class Audio(Document):
    """
    Represents an audio document of any kind.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Audio"]
    class_class_curie: ClassVar[str] = "as:Audio"
    class_name: ClassVar[str] = "Audio"
    class_model_uri: ClassVar[URIRef] = AS.Audio


class Image(Document):
    """
    An image document of any kind
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Image"]
    class_class_curie: ClassVar[str] = "as:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = AS.Image


class Video(Document):
    """
    Represents a video document of any kind.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Video"]
    class_class_curie: ClassVar[str] = "as:Video"
    class_name: ClassVar[str] = "Video"
    class_model_uri: ClassVar[URIRef] = AS.Video


class Note(Object):
    """
    Represents a short written work typically less than a single paragraph in length.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Note"]
    class_class_curie: ClassVar[str] = "as:Note"
    class_name: ClassVar[str] = "Note"
    class_model_uri: ClassVar[URIRef] = AS.Note


class Page(Object):
    """
    Represents a Web Page.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Page"]
    class_class_curie: ClassVar[str] = "as:Page"
    class_name: ClassVar[str] = "Page"
    class_model_uri: ClassVar[URIRef] = AS.Page


class Event(Object):
    """
    Represents any kind of event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Event"]
    class_class_curie: ClassVar[str] = "as:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = AS.Event


@dataclass
class Place(Object):
    """
    Represents a logical or physical location. See 5.3 Representing Places for additional information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Place"]
    class_class_curie: ClassVar[str] = "as:Place"
    class_name: ClassVar[str] = "Place"
    class_model_uri: ClassVar[URIRef] = AS.Place

    accuracy: Optional[float] = None
    altitude: Optional[float] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    radius: Optional[float] = None
    units: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.accuracy is not None and not isinstance(self.accuracy, float):
            self.accuracy = float(self.accuracy)

        if self.altitude is not None and not isinstance(self.altitude, float):
            self.altitude = float(self.altitude)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.radius is not None and not isinstance(self.radius, float):
            self.radius = float(self.radius)

        if self.units is not None and not isinstance(self.units, str):
            self.units = str(self.units)

        super().__post_init__(**kwargs)


class Mention(Link):
    """
    A specialized Link that represents an @mention.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Mention"]
    class_class_curie: ClassVar[str] = "as:Mention"
    class_name: ClassVar[str] = "Mention"
    class_model_uri: ClassVar[URIRef] = AS.Mention


@dataclass
class Profile(Object):
    """
    A Profile is a content object that describes another Object, typically used to describe Actor Type objects. The
    describes property is used to reference the object being described by the profile.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Profile"]
    class_class_curie: ClassVar[str] = "as:Profile"
    class_name: ClassVar[str] = "Profile"
    class_model_uri: ClassVar[URIRef] = AS.Profile

    describes: Optional[Union[dict, Object]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.describes is not None and not isinstance(self.describes, Object):
            self.describes = Object(**as_dict(self.describes))

        super().__post_init__(**kwargs)


@dataclass
class Tombstone(Object):
    """
    A Tombstone represents a content object that has been deleted. It can be used in Collections to signify that there
    used to be an object at this position, but it has been deleted.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Tombstone"]
    class_class_curie: ClassVar[str] = "as:Tombstone"
    class_name: ClassVar[str] = "Tombstone"
    class_model_uri: ClassVar[URIRef] = AS.Tombstone

    formerType: Optional[Union[Union[dict, Object], List[Union[dict, Object]]]] = empty_list()
    deleted: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.formerType, list):
            self.formerType = [self.formerType] if self.formerType is not None else []
        self.formerType = [v if isinstance(v, Object) else Object(**as_dict(v)) for v in self.formerType]

        if self.deleted is not None and not isinstance(self.deleted, XSDDateTime):
            self.deleted = XSDDateTime(self.deleted)

        super().__post_init__(**kwargs)


class OrderedItems(YAMLRoot):
    """
    OrderedItems is not a real class in the ActivityStreams specification, but it is used as the container of the
    items in `OrderedCollections`
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["OrderedItems"]
    class_class_curie: ClassVar[str] = "as:OrderedItems"
    class_name: ClassVar[str] = "OrderedItems"
    class_model_uri: ClassVar[URIRef] = AS.OrderedItems


# Enumerations
class UnitEnum(EnumDefinitionImpl):

    cm = PermissibleValue(
        text="cm",
        meaning=UNIT["CM"])
    feet = PermissibleValue(
        text="feet",
        meaning=UNIT["FT"])
    inches = PermissibleValue(
        text="inches",
        meaning=UNIT["IN"])
    km = PermissibleValue(
        text="km",
        meaning=UNIT["KiloM"])
    m = PermissibleValue(
        text="m",
        meaning=UNIT["M"])
    miles = PermissibleValue(
        text="miles",
        meaning=UNIT["MI"])

    _defn = EnumDefinition(
        name="UnitEnum",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=AS.id, name="id", curie=AS.curie('id'),
                   model_uri=AS.id, domain=None, range=Optional[Union[str, AnyURI]])

slots.type = Slot(uri=AS.type, name="type", curie=AS.curie('type'),
                   model_uri=AS.type, domain=None, range=Optional[Union[Union[str, AnyURI], List[Union[str, AnyURI]]]])

slots.actor = Slot(uri=AS.actor, name="actor", curie=AS.curie('actor'),
                   model_uri=AS.actor, domain=None, range=Optional[Union[str, List[str]]])

slots.attachment = Slot(uri=AS.attachment, name="attachment", curie=AS.curie('attachment'),
                   model_uri=AS.attachment, domain=None, range=Optional[Union[str, List[str]]])

slots.attributedTo = Slot(uri=AS.attributedTo, name="attributedTo", curie=AS.curie('attributedTo'),
                   model_uri=AS.attributedTo, domain=None, range=Optional[Union[str, List[str]]])

slots.audience = Slot(uri=AS.audience, name="audience", curie=AS.curie('audience'),
                   model_uri=AS.audience, domain=None, range=Optional[Union[str, List[str]]])

slots.bcc = Slot(uri=AS.bcc, name="bcc", curie=AS.curie('bcc'),
                   model_uri=AS.bcc, domain=None, range=Optional[Union[str, List[str]]])

slots.bto = Slot(uri=AS.bto, name="bto", curie=AS.curie('bto'),
                   model_uri=AS.bto, domain=None, range=Optional[Union[str, List[str]]])

slots.cc = Slot(uri=AS.cc, name="cc", curie=AS.curie('cc'),
                   model_uri=AS.cc, domain=None, range=Optional[Union[str, List[str]]])

slots.context = Slot(uri=AS.context, name="context", curie=AS.curie('context'),
                   model_uri=AS.context, domain=None, range=Optional[Union[str, List[str]]])

slots.current = Slot(uri=AS.current, name="current", curie=AS.curie('current'),
                   model_uri=AS.current, domain=None, range=Optional[str])

slots.first = Slot(uri=AS.first, name="first", curie=AS.curie('first'),
                   model_uri=AS.first, domain=None, range=Optional[str])

slots.generator = Slot(uri=AS.generator, name="generator", curie=AS.curie('generator'),
                   model_uri=AS.generator, domain=None, range=Optional[Union[str, List[str]]])

slots.icon = Slot(uri=AS.icon, name="icon", curie=AS.curie('icon'),
                   model_uri=AS.icon, domain=None, range=Optional[Union[str, List[str]]])

slots.image = Slot(uri=AS.image, name="image", curie=AS.curie('image'),
                   model_uri=AS.image, domain=None, range=Optional[Union[str, List[str]]])

slots.inReplyTo = Slot(uri=AS.inReplyTo, name="inReplyTo", curie=AS.curie('inReplyTo'),
                   model_uri=AS.inReplyTo, domain=None, range=Optional[Union[str, List[str]]])

slots.instrument = Slot(uri=AS.instrument, name="instrument", curie=AS.curie('instrument'),
                   model_uri=AS.instrument, domain=None, range=Optional[Union[str, List[str]]])

slots.last = Slot(uri=AS.last, name="last", curie=AS.curie('last'),
                   model_uri=AS.last, domain=None, range=Optional[str])

slots.location = Slot(uri=AS.location, name="location", curie=AS.curie('location'),
                   model_uri=AS.location, domain=None, range=Optional[Union[str, List[str]]])

slots.items = Slot(uri=AS.items, name="items", curie=AS.curie('items'),
                   model_uri=AS.items, domain=None, range=Optional[Union[str, List[str]]])

slots.oneOf = Slot(uri=AS.oneOf, name="oneOf", curie=AS.curie('oneOf'),
                   model_uri=AS.oneOf, domain=None, range=Optional[Union[str, List[str]]])

slots.anyOf = Slot(uri=AS.anyOf, name="anyOf", curie=AS.curie('anyOf'),
                   model_uri=AS.anyOf, domain=None, range=Optional[Union[str, List[str]]])

slots.closed = Slot(uri=AS.closed, name="closed", curie=AS.curie('closed'),
                   model_uri=AS.closed, domain=None, range=Optional[str])

slots.origin = Slot(uri=AS.origin, name="origin", curie=AS.curie('origin'),
                   model_uri=AS.origin, domain=None, range=Optional[Union[str, List[str]]])

slots.next = Slot(uri=AS.next, name="next", curie=AS.curie('next'),
                   model_uri=AS.next, domain=None, range=Optional[str])

slots.object = Slot(uri=AS.object, name="object", curie=AS.curie('object'),
                   model_uri=AS.object, domain=None, range=Optional[Union[str, List[str]]])

slots.prev = Slot(uri=AS.prev, name="prev", curie=AS.curie('prev'),
                   model_uri=AS.prev, domain=None, range=Optional[str])

slots.preview = Slot(uri=AS.preview, name="preview", curie=AS.curie('preview'),
                   model_uri=AS.preview, domain=None, range=Optional[Union[str, List[str]]])

slots.result = Slot(uri=AS.result, name="result", curie=AS.curie('result'),
                   model_uri=AS.result, domain=None, range=Optional[Union[str, List[str]]])

slots.replies = Slot(uri=AS.replies, name="replies", curie=AS.curie('replies'),
                   model_uri=AS.replies, domain=None, range=Optional[Union[dict, Collection]])

slots.tag = Slot(uri=AS.tag, name="tag", curie=AS.curie('tag'),
                   model_uri=AS.tag, domain=None, range=Optional[Union[str, List[str]]])

slots.target = Slot(uri=AS.target, name="target", curie=AS.curie('target'),
                   model_uri=AS.target, domain=None, range=Optional[Union[str, List[str]]])

slots.to = Slot(uri=AS.to, name="to", curie=AS.curie('to'),
                   model_uri=AS.to, domain=None, range=Optional[Union[str, List[str]]])

slots.url = Slot(uri=AS.url, name="url", curie=AS.curie('url'),
                   model_uri=AS.url, domain=None, range=Optional[Union[str, List[str]]])

slots.accuracy = Slot(uri=AS.accuracy, name="accuracy", curie=AS.curie('accuracy'),
                   model_uri=AS.accuracy, domain=None, range=Optional[float])

slots.altitude = Slot(uri=AS.altitude, name="altitude", curie=AS.curie('altitude'),
                   model_uri=AS.altitude, domain=None, range=Optional[float])

slots.content = Slot(uri=AS.content, name="content", curie=AS.curie('content'),
                   model_uri=AS.content, domain=None, range=Optional[Union[str, List[str]]])

slots.name = Slot(uri=RDFS.name, name="name", curie=RDFS.curie('name'),
                   model_uri=AS.name, domain=None, range=Optional[Union[str, List[str]]])

slots.duration = Slot(uri=AS.duration, name="duration", curie=AS.curie('duration'),
                   model_uri=AS.duration, domain=None, range=Optional[Union[str, DurationType]])

slots.height = Slot(uri=AS.height, name="height", curie=AS.curie('height'),
                   model_uri=AS.height, domain=None, range=Optional[Union[int, NonNegativeInteger]])

slots.href = Slot(uri=AS.href, name="href", curie=AS.curie('href'),
                   model_uri=AS.href, domain=None, range=Optional[Union[str, AnyURI]])

slots.hreflang = Slot(uri=AS.hreflang, name="hreflang", curie=AS.curie('hreflang'),
                   model_uri=AS.hreflang, domain=None, range=Optional[str])

slots.partOf = Slot(uri=AS.partOf, name="partOf", curie=AS.curie('partOf'),
                   model_uri=AS.partOf, domain=None, range=Optional[str])

slots.latitude = Slot(uri=AS.latitude, name="latitude", curie=AS.curie('latitude'),
                   model_uri=AS.latitude, domain=None, range=Optional[float])

slots.longitude = Slot(uri=AS.longitude, name="longitude", curie=AS.curie('longitude'),
                   model_uri=AS.longitude, domain=None, range=Optional[float])

slots.mediaType = Slot(uri=AS.mediaType, name="mediaType", curie=AS.curie('mediaType'),
                   model_uri=AS.mediaType, domain=None, range=Optional[str])

slots.endTime = Slot(uri=AS.endTime, name="endTime", curie=AS.curie('endTime'),
                   model_uri=AS.endTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.published = Slot(uri=AS.published, name="published", curie=AS.curie('published'),
                   model_uri=AS.published, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.startTime = Slot(uri=AS.startTime, name="startTime", curie=AS.curie('startTime'),
                   model_uri=AS.startTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.radius = Slot(uri=AS.radius, name="radius", curie=AS.curie('radius'),
                   model_uri=AS.radius, domain=None, range=Optional[float])

slots.rel = Slot(uri=AS.rel, name="rel", curie=AS.curie('rel'),
                   model_uri=AS.rel, domain=None, range=Optional[Union[str, List[str]]])

slots.startIndex = Slot(uri=AS.startIndex, name="startIndex", curie=AS.curie('startIndex'),
                   model_uri=AS.startIndex, domain=None, range=Optional[Union[int, NonNegativeInteger]])

slots.summary = Slot(uri=AS.summary, name="summary", curie=AS.curie('summary'),
                   model_uri=AS.summary, domain=None, range=Optional[Union[str, List[str]]])

slots.totalItems = Slot(uri=AS.totalItems, name="totalItems", curie=AS.curie('totalItems'),
                   model_uri=AS.totalItems, domain=None, range=Optional[Union[int, NonNegativeInteger]])

slots.units = Slot(uri=AS.units, name="units", curie=AS.curie('units'),
                   model_uri=AS.units, domain=None, range=Optional[str])

slots.updated = Slot(uri=AS.updated, name="updated", curie=AS.curie('updated'),
                   model_uri=AS.updated, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.width = Slot(uri=AS.width, name="width", curie=AS.curie('width'),
                   model_uri=AS.width, domain=None, range=Optional[Union[int, NonNegativeInteger]])

slots.subject = Slot(uri=AS.subject, name="subject", curie=AS.curie('subject'),
                   model_uri=AS.subject, domain=None, range=Optional[Union[str, List[str]]])

slots.relationship = Slot(uri=AS.relationship, name="relationship", curie=AS.curie('relationship'),
                   model_uri=AS.relationship, domain=None, range=Optional[Union[Union[dict, Object], List[Union[dict, Object]]]])

slots.describes = Slot(uri=AS.describes, name="describes", curie=AS.curie('describes'),
                   model_uri=AS.describes, domain=None, range=Optional[Union[dict, Object]])

slots.formerType = Slot(uri=AS.formerType, name="formerType", curie=AS.curie('formerType'),
                   model_uri=AS.formerType, domain=None, range=Optional[Union[Union[dict, Object], List[Union[dict, Object]]]])

slots.deleted = Slot(uri=AS.deleted, name="deleted", curie=AS.curie('deleted'),
                   model_uri=AS.deleted, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.Collection_items = Slot(uri=AS.items, name="Collection_items", curie=AS.curie('items'),
                   model_uri=AS.Collection_items, domain=Collection, range=Optional[Union[str, List[str]]])

slots.OrderedCollection_items = Slot(uri=AS.items, name="OrderedCollection_items", curie=AS.curie('items'),
                   model_uri=AS.OrderedCollection_items, domain=OrderedCollection, range=Optional[Union[str, List[str]]])

slots.OrderedCollectionPage_items = Slot(uri=AS.items, name="OrderedCollectionPage_items", curie=AS.curie('items'),
                   model_uri=AS.OrderedCollectionPage_items, domain=OrderedCollectionPage, range=Optional[Union[str, List[str]]])