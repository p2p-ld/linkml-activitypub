from __future__ import annotations
from datetime import datetime, date
from enum import Enum

from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, ConfigDict,  Field, field_validator
import re
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra = 'forbid',
        arbitrary_types_allowed=True,
        use_enum_values = True)
    pass


class UnitEnum(str, Enum):
    
    
    cm = "cm"
    
    feet = "feet"
    
    inches = "inches"
    
    km = "km"
    
    m = "m"
    
    miles = "miles"
    
    

class Property(ConfiguredBaseModel):
    
    None
    
    

class Statement(ConfiguredBaseModel):
    
    None
    
    

class Object(ConfiguredBaseModel):
    """
    Describes an object of any kind. The Object type serves as the base type for most of the other kinds of objects defined in the Activity Vocabulary, including other Core types such as Activity, IntransitiveActivity, Collection and OrderedCollection.
    """
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Link(ConfiguredBaseModel):
    """
    A Link is an indirect, qualified reference to a resource identified by a URL. The fundamental model for links is established by [ RFC5988]. Many of the properties defined by the Activity Vocabulary allow values that are either instances of Object or Link. When a Link is used, it establishes a qualified relation connecting the subject (the containing object) to the resource identified by the href. Properties of the Link are properties of the reference as opposed to properties of the resource.
    """
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    height: Optional[int] = Field(None, description="""On a Link, specifies a hint as to the rendering height in device-independent pixels of the linked resource.""", ge=0)
    href: Optional[str] = Field(None, description="""The target resource pointed to by a Link.""")
    hreflang: Optional[str] = Field(None, description="""Hints as to the language used by the target resource. Value MUST be a [BCP47] Language-Tag.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    rel: Optional[List[str]] = Field(default_factory=list, description="""A link relation associated with a Link. The value MUST conform to both the [HTML5] and [RFC5988] \"link relation\" definitions.
In the [HTML5], any string not containing the \"space\" U+0020, \"tab\" (U+0009), \"LF\" (U+000A), \"FF\" (U+000C), \"CR\" (U+000D) or \",\" (U+002C) characters can be used as a valid link relation.
""")
    width: Optional[int] = Field(None, description="""On a Link, specifies a hint as to the rendering width in device-independent pixels of the linked resource.""", ge=0)
    
    

class Activity(Object):
    """
    An Activity is a subtype of Object that describes some form of action that may happen, is currently happening, or has already happened. The Activity type itself serves as an abstract base type for all types of activities. It is important to note that the Activity type itself does not carry any specific semantics about the kind of action being taken.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class IntransitiveActivity(Activity):
    """
    ['An Activity that has no direct object@en']
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Collection(Object):
    """
    A Collection is a subtype of Object that represents ordered or unordered sets of Object or Link instances. Refer to the Activity Streams 2.0 Core specification for a complete description of the Collection type.
    """
    current: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, indicates the page that contains the most recently updated member items.""")
    first: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, indicates the furthest preceeding page of items in the collection.""")
    items: Optional[List[str]] = Field(default_factory=list, description="""Identifies the items contained in a collection. The items might be ordered or unordered.""")
    last: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, indicates the furthest proceeding page of the collection.""")
    totalItems: Optional[int] = Field(None, description="""A non-negative integer specifying the total number of objects contained by the logical view of the collection. This number might not reflect the actual number of items serialized within the Collection object instance.""", ge=0)
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class OrderedCollection(Collection):
    """
    A subtype of Collection in which members of the logical collection are assumed to always be strictly ordered.
    """
    current: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, indicates the page that contains the most recently updated member items.""")
    first: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, indicates the furthest preceeding page of items in the collection.""")
    items: Optional[List[str]] = Field(default_factory=list, description="""Identifies the items contained in a collection. The items might be ordered or unordered.""")
    last: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, indicates the furthest proceeding page of the collection.""")
    totalItems: Optional[int] = Field(None, description="""A non-negative integer specifying the total number of objects contained by the logical view of the collection. This number might not reflect the actual number of items serialized within the Collection object instance.""", ge=0)
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class CollectionPage(Collection):
    """
    Used to represent distinct subsets of items from a Collection. Refer to the Activity Streams 2.0 Core for a complete description of the CollectionPage object.
    """
    next: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, indicates the next page of items.""")
    partOf: Optional[Union[Collection, Link]] = Field(None, description="""Identifies the Collection to which a CollectionPage objects items belong.""")
    prev: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, identifies the previous page of items.""")
    current: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, indicates the page that contains the most recently updated member items.""")
    first: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, indicates the furthest preceeding page of items in the collection.""")
    items: Optional[List[str]] = Field(default_factory=list, description="""Identifies the items contained in a collection. The items might be ordered or unordered.""")
    last: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, indicates the furthest proceeding page of the collection.""")
    totalItems: Optional[int] = Field(None, description="""A non-negative integer specifying the total number of objects contained by the logical view of the collection. This number might not reflect the actual number of items serialized within the Collection object instance.""", ge=0)
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class OrderedCollectionPage(OrderedCollection):
    """
    Used to represent ordered subsets of items from an OrderedCollection. Refer to the Activity Streams 2.0 Core for a complete description of the OrderedCollectionPage object.
    """
    startIndex: Optional[int] = Field(None, description="""A non-negative integer value identifying the relative position within the logical view of a strictly ordered collection.""", ge=0)
    next: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, indicates the next page of items.""")
    partOf: Optional[Union[Collection, Link]] = Field(None, description="""Identifies the Collection to which a CollectionPage objects items belong.""")
    prev: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, identifies the previous page of items.""")
    current: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, indicates the page that contains the most recently updated member items.""")
    first: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, indicates the furthest preceeding page of items in the collection.""")
    items: Optional[List[str]] = Field(default_factory=list, description="""Identifies the items contained in a collection. The items might be ordered or unordered.""")
    last: Optional[Union[CollectionPage, Link, OrderedCollectionPage]] = Field(None, description="""In a paged Collection, indicates the furthest proceeding page of the collection.""")
    totalItems: Optional[int] = Field(None, description="""A non-negative integer specifying the total number of objects contained by the logical view of the collection. This number might not reflect the actual number of items serialized within the Collection object instance.""", ge=0)
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Accept(Activity):
    """
    Indicates that the actor accepts the object. The target property can be used in certain circumstances to indicate the context into which the object has been accepted.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class TentativeAccept(Accept):
    """
    A specialization of Accept indicating that the acceptance is tentative.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Add(Activity):
    """
    Indicates that the actor has added the object to the target. If the target property is not explicitly specified, the target would need to be determined implicitly by context. The origin can be used to identify the context from which the object originated.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Arrive(IntransitiveActivity):
    """
    An IntransitiveActivity that indicates that the actor has arrived at the location. The origin can be used to identify the context from which the actor originated. The target typically has no defined meaning.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Create(Activity):
    """
    Indicates that the actor has created the object.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Delete(Activity):
    """
    Indicates that the actor has deleted the object. If specified, the origin indicates the context from which the object was deleted.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Follow(Activity):
    """
    Indicates that the actor is \"following\" the object. Following is defined in the sense typically used within Social systems in which the actor is interested in any activity performed by or on the object. The target and origin typically have no defined meaning.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Ignore(Activity):
    """
    Indicates that the actor is ignoring the object. The target and origin typically have no defined meaning.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Join(Activity):
    """
    Indicates that the actor has joined the object. The target and origin typically have no defined meaning.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Leave(Activity):
    """
    Indicates that the actor has left the object. The target and origin typically have no meaning.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Like(Activity):
    """
    Indicates that the actor likes, recommends or endorses the object. The target and origin typically have no defined meaning.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Offer(Activity):
    """
    Indicates that the actor is offering the object. If specified, the target indicates the entity to which the object is being offered.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Invite(Offer):
    """
    A specialization of Offer in which the actor is extending an invitation for the object to the target.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Reject(Activity):
    """
    Indicates that the actor is rejecting the object. The target and origin typically have no defined meaning.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class TentativeReject(Reject):
    """
    A specialization of Reject in which the rejection is considered tentative.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Remove(Activity):
    """
    Indicates that the actor is removing the object. If specified, the origin indicates the context from which the object is being removed.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Undo(Activity):
    """
    Indicates that the actor is undoing the object. In most cases, the object will be an Activity describing some previously performed action (for instance, a person may have previously \"liked\" an article but, for whatever reason, might choose to undo that like at some later point in time). The target and origin typically have no defined meaning.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Update(Activity):
    """
    Indicates that the actor has updated the object. Note, however, that this vocabulary does not define a mechanism for describing the actual set of modifications made to object. The target and origin typically have no defined meaning.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class View(Activity):
    """
    Indicates that the actor has viewed the object.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Listen(Activity):
    """
    Indicates that the actor has listened to the object.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Read(Activity):
    """
    Indicates that the actor has read the object.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Move(Activity):
    """
    Indicates that the actor has moved object from origin to target. If the origin or target are not specified, either can be determined by context.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Travel(IntransitiveActivity):
    """
    Indicates that the actor is traveling to target from origin. Travel is an IntransitiveObject whose actor specifies the direct object. If the target or origin are not specified, either can be determined by context.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Announce(Activity):
    """
    Indicates that the actor is calling the target's attention the object. The origin typically has no defined meaning.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Block(Ignore):
    """
    Indicates that the actor is blocking the object. Blocking is a stronger form of Ignore. The typical use is to support social systems that allow one user to block activities or content of other users. The target and origin typically have no defined meaning.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Flag(Activity):
    """
    Indicates that the actor is \"flagging\" the object. Flagging is defined in the sense common to many social platforms as reporting content as being inappropriate for any number of reasons.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Dislike(Activity):
    """
    Indicates that the actor dislikes the object.
    """
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Question(IntransitiveActivity):
    """
    Represents a question being asked. Question objects are an extension of IntransitiveActivity. That is, the Question object is an Activity, but the direct object is the question itself and therefore it would not contain an object property.
Either of the anyOf and oneOf properties MAY be used to express possible answers, but a Question object MUST NOT have both properties.

    """
    anyOf: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an inclusive option for a Question. Use of anyOf implies that the Question can have multiple answers. To indicate that a Question can have only one answer, use oneOf.""")
    oneOf: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an exclusive option for a Question. Use of oneOf implies that the Question can have only a single answer. To indicate that a Question can have multiple answers, use anyOf.""")
    actor: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.""")
    instrument: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more objects used (or to be used) in the completion of an Activity.""")
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    origin: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition \"from\". For instance, in the activity \"John moved an item to List B from List A\", the origin of the activity is \"List A\".""")
    result: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.""")
    target: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition \"to\". For instance, in the activity \"John added a movie to his wishlist\", the target of the activity is John's wishlist. An activity can have more than one target.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Application(Object):
    """
    Describes a software application.
    """
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Group(Object):
    """
    Represents a formal or informal collective of Actors.
    """
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Organization(Object):
    """
    Represents an organization.
    """
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Person(Object):
    """
    Represents an individual person.
    """
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Service(Object):
    """
    Represents a service of any kind.
    """
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Relationship(Object):
    """
    Describes a relationship between two individuals. The subject and object properties are used to identify the connected individuals.
See 5.2 Representing Relationships Between Entities for additional information.

    """
    object: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""When used within an Activity, describes the direct object of the activity. For instance, in the activity \"John added a movie to his wishlist\", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.
""")
    relationship: Optional[List[Object]] = Field(default_factory=list, description="""On a Relationship object, the relationship property identifies the kind of relationship that exists between subject and object.""")
    subject: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""On a Relationship object, the subject property identifies one of the connected individuals. For instance, for a Relationship object describing \"John is related to Sally\", subject would refer to John.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Document(Object):
    """
    Represents a document of any kind.
    """
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Article(Object):
    
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Audio(Document):
    """
    Represents an audio document of any kind.
    """
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Image(Document):
    """
    An image document of any kind
    """
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Video(Document):
    """
    Represents a video document of any kind.
    """
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Note(Object):
    """
    Represents a short written work typically less than a single paragraph in length.
    """
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Page(Object):
    """
    Represents a Web Page.
    """
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Event(Object):
    """
    Represents any kind of event.
    """
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Place(Object):
    """
    Represents a logical or physical location. See 5.3 Representing Places for additional information.
    """
    accuracy: Optional[float] = Field(None, description="""Indicates the accuracy of position coordinates on a Place objects. Expressed in properties of percentage. e.g. \"94.0\" means \"94.0% accurate\".""", ge=0, le=100)
    altitude: Optional[float] = Field(None, description="""Indicates the altitude of a place. The measurement units is indicated using the units property. If units is not specified, the default is assumed to be \"m\" indicating meters.""")
    latitude: Optional[float] = Field(None, description="""The latitude of a place""")
    longitude: Optional[float] = Field(None, description="""The longitude of a place""")
    radius: Optional[float] = Field(None, description="""The radius from the given latitude and longitude for a Place. The units is expressed by the units property. If units is not specified, the default is assumed to be \"m\" indicating \"meters\".""", ge=0)
    units: Optional[Union[UnitEnum, str]] = Field(None, description="""Specifies the measurement units for the radius and altitude properties on a Place object. If not specified, the default is assumed to be \"m\" for \"meters\".""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Mention(Link):
    """
    A specialized Link that represents an @mention.
    """
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    height: Optional[int] = Field(None, description="""On a Link, specifies a hint as to the rendering height in device-independent pixels of the linked resource.""", ge=0)
    href: Optional[str] = Field(None, description="""The target resource pointed to by a Link.""")
    hreflang: Optional[str] = Field(None, description="""Hints as to the language used by the target resource. Value MUST be a [BCP47] Language-Tag.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    rel: Optional[List[str]] = Field(default_factory=list, description="""A link relation associated with a Link. The value MUST conform to both the [HTML5] and [RFC5988] \"link relation\" definitions.
In the [HTML5], any string not containing the \"space\" U+0020, \"tab\" (U+0009), \"LF\" (U+000A), \"FF\" (U+000C), \"CR\" (U+000D) or \",\" (U+002C) characters can be used as a valid link relation.
""")
    width: Optional[int] = Field(None, description="""On a Link, specifies a hint as to the rendering width in device-independent pixels of the linked resource.""", ge=0)
    
    

class Profile(Object):
    """
    A Profile is a content object that describes another Object, typically used to describe Actor Type objects. The describes property is used to reference the object being described by the profile.
    """
    describes: Optional[Object] = Field(None, description="""On a Profile object, the describes property identifies the object described by the Profile.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class Tombstone(Object):
    """
    A Tombstone represents a content object that has been deleted. It can be used in Collections to signify that there used to be an object at this position, but it has been deleted.
    """
    formerType: Optional[List[Object]] = Field(default_factory=list, description="""On a Tombstone object, the formerType property identifies the type of the object that was deleted.""")
    deleted: Optional[datetime ] = Field(None, description="""On a Tombstone object, the deleted property is a timestamp for when the object was deleted.""")
    attachment: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.""")
    attributedTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.""")
    audience: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.""")
    bcc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies one or more Objects that are part of the private secondary audience of this Object.""")
    bto: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the private primary audience of this Object.""")
    cc: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an Object that is part of the public secondary audience of this Object.""")
    content: Optional[List[str]] = Field(default_factory=list, description="""The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.""")
    context: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the context within which the object exists or an activity was performed.
The notion of \"context\" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.
""")
    generator: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies the entity (e.g. an application) that generated the object.""")
    icon: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.""")
    image: Optional[List[Union[Image, Link]]] = Field(default_factory=list, description="""Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.""")
    inReplyTo: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more entities for which this object is considered a response.""")
    location: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Indicates one or more physical or logical locations associated with the object.""")
    name: Optional[List[str]] = Field(default_factory=list, description="""A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.""")
    preview: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity that provides a preview of this object.""")
    replies: Optional[Collection] = Field(None, description="""Identifies a Collection containing objects considered to be responses to this object.""")
    summary: Optional[List[str]] = Field(default_factory=list, description="""A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.""")
    tag: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""One or more \"tags\" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.""")
    to: Optional[List[Union[Link, Object]]] = Field(default_factory=list, description="""Identifies an entity considered to be part of the public primary audience of an Object""")
    url: Optional[List[Union[Link, str]]] = Field(default_factory=list, description="""Identifies one or more links to representations of the object""")
    duration: Optional[str] = Field(None, description="""When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as \"PT5S\").""")
    endTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.""")
    id: Optional[str] = Field(None, description="""Provides the globally unique identifier for an Object or Link.""")
    mediaType: Optional[str] = Field(None, description="""When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.
""")
    published: Optional[datetime ] = Field(None, description="""The date and time at which the object was published""")
    startTime: Optional[datetime ] = Field(None, description="""The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.""")
    updated: Optional[datetime ] = Field(None, description="""The date and time at which the object was updated""")
    
    

class OrderedItems(ConfiguredBaseModel):
    """
    OrderedItems is not a real class in the ActivityStreams specification, but it is used as the container of the items in `OrderedCollections`

    """
    None
    
    


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Property.model_rebuild()
Statement.model_rebuild()
Object.model_rebuild()
Link.model_rebuild()
Activity.model_rebuild()
IntransitiveActivity.model_rebuild()
Collection.model_rebuild()
OrderedCollection.model_rebuild()
CollectionPage.model_rebuild()
OrderedCollectionPage.model_rebuild()
Accept.model_rebuild()
TentativeAccept.model_rebuild()
Add.model_rebuild()
Arrive.model_rebuild()
Create.model_rebuild()
Delete.model_rebuild()
Follow.model_rebuild()
Ignore.model_rebuild()
Join.model_rebuild()
Leave.model_rebuild()
Like.model_rebuild()
Offer.model_rebuild()
Invite.model_rebuild()
Reject.model_rebuild()
TentativeReject.model_rebuild()
Remove.model_rebuild()
Undo.model_rebuild()
Update.model_rebuild()
View.model_rebuild()
Listen.model_rebuild()
Read.model_rebuild()
Move.model_rebuild()
Travel.model_rebuild()
Announce.model_rebuild()
Block.model_rebuild()
Flag.model_rebuild()
Dislike.model_rebuild()
Question.model_rebuild()
Application.model_rebuild()
Group.model_rebuild()
Organization.model_rebuild()
Person.model_rebuild()
Service.model_rebuild()
Relationship.model_rebuild()
Document.model_rebuild()
Article.model_rebuild()
Audio.model_rebuild()
Image.model_rebuild()
Video.model_rebuild()
Note.model_rebuild()
Page.model_rebuild()
Event.model_rebuild()
Place.model_rebuild()
Mention.model_rebuild()
Profile.model_rebuild()
Tombstone.model_rebuild()
OrderedItems.model_rebuild()

