
# linkml-activitystreams


**metamodel version:** 1.7.0

**version:** None


LinkML representation of ActivityStreams 2 Schema.


### Classes

 * [Link](Link.md) - A Link is an indirect, qualified reference to a resource identified by a URL. The fundamental model for links is established by [ RFC5988]. Many of the properties defined by the Activity Vocabulary allow values that are either instances of Object or Link. When a Link is used, it establishes a qualified relation connecting the subject (the containing object) to the resource identified by the href. Properties of the Link are properties of the reference as opposed to properties of the resource.
     * [Mention](Mention.md) - A specialized Link that represents an @mention.
 * [Object](Object.md) - Describes an object of any kind. The Object type serves as the base type for most of the other kinds of objects defined in the Activity Vocabulary, including other Core types such as Activity, IntransitiveActivity, Collection and OrderedCollection.
     * [Activity](Activity.md) - An Activity is a subtype of Object that describes some form of action that may happen, is currently happening, or has already happened. The Activity type itself serves as an abstract base type for all types of activities. It is important to note that the Activity type itself does not carry any specific semantics about the kind of action being taken.
         * [Accept](Accept.md) - Indicates that the actor accepts the object. The target property can be used in certain circumstances to indicate the context into which the object has been accepted.
             * [TentativeAccept](TentativeAccept.md) - A specialization of Accept indicating that the acceptance is tentative.
         * [Add](Add.md) - Indicates that the actor has added the object to the target. If the target property is not explicitly specified, the target would need to be determined implicitly by context. The origin can be used to identify the context from which the object originated.
         * [Announce](Announce.md) - Indicates that the actor is calling the target's attention the object. The origin typically has no defined meaning.
         * [Create](Create.md) - Indicates that the actor has created the object.
         * [Delete](Delete.md) - Indicates that the actor has deleted the object. If specified, the origin indicates the context from which the object was deleted.
         * [Dislike](Dislike.md) - Indicates that the actor dislikes the object.
         * [Flag](Flag.md) - Indicates that the actor is "flagging" the object. Flagging is defined in the sense common to many social platforms as reporting content as being inappropriate for any number of reasons.
         * [Follow](Follow.md) - Indicates that the actor is "following" the object. Following is defined in the sense typically used within Social systems in which the actor is interested in any activity performed by or on the object. The target and origin typically have no defined meaning.
         * [Ignore](Ignore.md) - Indicates that the actor is ignoring the object. The target and origin typically have no defined meaning.
             * [Block](Block.md) - Indicates that the actor is blocking the object. Blocking is a stronger form of Ignore. The typical use is to support social systems that allow one user to block activities or content of other users. The target and origin typically have no defined meaning.
         * [IntransitiveActivity](IntransitiveActivity.md) - ['An Activity that has no direct object@en']
             * [Arrive](Arrive.md) - An IntransitiveActivity that indicates that the actor has arrived at the location. The origin can be used to identify the context from which the actor originated. The target typically has no defined meaning.
             * [Question](Question.md) - Represents a question being asked. Question objects are an extension of IntransitiveActivity. That is, the Question object is an Activity, but the direct object is the question itself and therefore it would not contain an object property.
             * [Travel](Travel.md) - Indicates that the actor is traveling to target from origin. Travel is an IntransitiveObject whose actor specifies the direct object. If the target or origin are not specified, either can be determined by context.
         * [Join](Join.md) - Indicates that the actor has joined the object. The target and origin typically have no defined meaning.
         * [Leave](Leave.md) - Indicates that the actor has left the object. The target and origin typically have no meaning.
         * [Like](Like.md) - Indicates that the actor likes, recommends or endorses the object. The target and origin typically have no defined meaning.
         * [Listen](Listen.md) - Indicates that the actor has listened to the object.
         * [Move](Move.md) - Indicates that the actor has moved object from origin to target. If the origin or target are not specified, either can be determined by context.
         * [Offer](Offer.md) - Indicates that the actor is offering the object. If specified, the target indicates the entity to which the object is being offered.
             * [Invite](Invite.md) - A specialization of Offer in which the actor is extending an invitation for the object to the target.
         * [Read](Read.md) - Indicates that the actor has read the object.
         * [Reject](Reject.md) - Indicates that the actor is rejecting the object. The target and origin typically have no defined meaning.
             * [TentativeReject](TentativeReject.md) - A specialization of Reject in which the rejection is considered tentative.
         * [Remove](Remove.md) - Indicates that the actor is removing the object. If specified, the origin indicates the context from which the object is being removed.
         * [Undo](Undo.md) - Indicates that the actor is undoing the object. In most cases, the object will be an Activity describing some previously performed action (for instance, a person may have previously "liked" an article but, for whatever reason, might choose to undo that like at some later point in time). The target and origin typically have no defined meaning.
         * [Update](Update.md) - Indicates that the actor has updated the object. Note, however, that this vocabulary does not define a mechanism for describing the actual set of modifications made to object. The target and origin typically have no defined meaning.
         * [View](View.md) - Indicates that the actor has viewed the object.
     * [Application](Application.md) - Describes a software application.
     * [Article](Article.md)
     * [Collection](Collection.md) - A Collection is a subtype of Object that represents ordered or unordered sets of Object or Link instances. Refer to the Activity Streams 2.0 Core specification for a complete description of the Collection type.
         * [CollectionPage](CollectionPage.md) - Used to represent distinct subsets of items from a Collection. Refer to the Activity Streams 2.0 Core for a complete description of the CollectionPage object.
         * [OrderedCollection](OrderedCollection.md) - A subtype of Collection in which members of the logical collection are assumed to always be strictly ordered.
             * [OrderedCollectionPage](OrderedCollectionPage.md) - Used to represent ordered subsets of items from an OrderedCollection. Refer to the Activity Streams 2.0 Core for a complete description of the OrderedCollectionPage object.
     * [Document](Document.md) - Represents a document of any kind.
         * [Audio](Audio.md) - Represents an audio document of any kind.
         * [Image](Image.md) - An image document of any kind
         * [Video](Video.md) - Represents a video document of any kind.
     * [Event](Event.md) - Represents any kind of event.
     * [Group](Group.md) - Represents a formal or informal collective of Actors.
     * [Note](Note.md) - Represents a short written work typically less than a single paragraph in length.
     * [Organization](Organization.md) - Represents an organization.
     * [Page](Page.md) - Represents a Web Page.
     * [Person](Person.md) - Represents an individual person.
     * [Place](Place.md) - Represents a logical or physical location. See 5.3 Representing Places for additional information.
     * [Profile](Profile.md) - A Profile is a content object that describes another Object, typically used to describe Actor Type objects. The describes property is used to reference the object being described by the profile.
     * [Relationship](Relationship.md) - Describes a relationship between two individuals. The subject and object properties are used to identify the connected individuals.
     * [Service](Service.md) - Represents a service of any kind.
     * [Tombstone](Tombstone.md) - A Tombstone represents a content object that has been deleted. It can be used in Collections to signify that there used to be an object at this position, but it has been deleted.
 * [OrderedItems](OrderedItems.md) - OrderedItems is not a real class in the ActivityStreams specification, but it is used as the container of the items in `OrderedCollections`
 * [Property](Property.md)
 * [Statement](Statement.md)

### Mixins


### Slots

 * [accuracy](accuracy.md) - Indicates the accuracy of position coordinates on a Place objects. Expressed in properties of percentage. e.g. "94.0" means "94.0% accurate".
 * [altitude](altitude.md) - Indicates the altitude of a place. The measurement units is indicated using the units property. If units is not specified, the default is assumed to be "m" indicating meters.
 * [anyOf](anyOf.md) - Identifies an inclusive option for a Question. Use of anyOf implies that the Question can have multiple answers. To indicate that a Question can have only one answer, use oneOf.
 * [attachment](attachment.md) - Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.
 * [attributedTo](attributedTo.md) - Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.
     * [actor](actor.md) - Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.
 * [audience](audience.md) - Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.
 * [bcc](bcc.md) - Identifies one or more Objects that are part of the private secondary audience of this Object.
 * [bto](bto.md) - Identifies an Object that is part of the private primary audience of this Object.
 * [cc](cc.md) - Identifies an Object that is part of the public secondary audience of this Object.
 * [closed](closed.md) - Indicates that a question has been closed, and answers are no longer accepted.
 * [content](content.md) - The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.
 * [context](context.md) - Identifies the context within which the object exists or an activity was performed.
 * [current](current.md) - In a paged Collection, indicates the page that contains the most recently updated member items.
 * [deleted](deleted.md) - On a Tombstone object, the deleted property is a timestamp for when the object was deleted.
 * [describes](describes.md) - On a Profile object, the describes property identifies the object described by the Profile.
 * [duration](duration.md) - When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as "PT5S").
 * [endTime](endTime.md) - The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.
 * [first](first.md) - In a paged Collection, indicates the furthest preceeding page of items in the collection.
 * [formerType](formerType.md) - On a Tombstone object, the formerType property identifies the type of the object that was deleted.
 * [generator](generator.md) - Identifies the entity (e.g. an application) that generated the object.
 * [height](height.md) - On a Link, specifies a hint as to the rendering height in device-independent pixels of the linked resource.
 * [href](href.md) - The target resource pointed to by a Link.
 * [hreflang](hreflang.md) - Hints as to the language used by the target resource. Value MUST be a [BCP47] Language-Tag.
 * [icon](icon.md) - Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.
 * [id](id.md) - Provides the globally unique identifier for an Object or Link.
 * [image](image.md) - Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.
 * [inReplyTo](inReplyTo.md) - Indicates one or more entities for which this object is considered a response.
 * [instrument](instrument.md) - Identifies one or more objects used (or to be used) in the completion of an Activity.
 * [items](items.md) - Identifies the items contained in a collection. The items might be ordered or unordered.
     * [Collection➞items](Collection_items.md)
         * [OrderedCollection➞items](OrderedCollection_items.md)
             * [OrderedCollectionPage➞items](OrderedCollectionPage_items.md)
 * [last](last.md) - In a paged Collection, indicates the furthest proceeding page of the collection.
 * [latitude](latitude.md) - The latitude of a place
 * [location](location.md) - Indicates one or more physical or logical locations associated with the object.
 * [longitude](longitude.md) - The longitude of a place
 * [mediaType](mediaType.md) - When used on a Link, identifies the MIME media type of the referenced resource.
 * [name](name.md) - A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.
 * [next](next.md) - In a paged Collection, indicates the next page of items.
 * [object](object.md) - When used within an Activity, describes the direct object of the activity. For instance, in the activity "John added a movie to his wishlist", the object of the activity is the movie added.
 * [oneOf](oneOf.md) - Identifies an exclusive option for a Question. Use of oneOf implies that the Question can have only a single answer. To indicate that a Question can have multiple answers, use anyOf.
 * [origin](origin.md) - Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition "from". For instance, in the activity "John moved an item to List B from List A", the origin of the activity is "List A".
 * [partOf](partOf.md) - Identifies the Collection to which a CollectionPage objects items belong.
 * [prev](prev.md) - In a paged Collection, identifies the previous page of items.
 * [preview](preview.md) - Identifies an entity that provides a preview of this object.
 * [published](published.md) - The date and time at which the object was published
 * [radius](radius.md) - The radius from the given latitude and longitude for a Place. The units is expressed by the units property. If units is not specified, the default is assumed to be "m" indicating "meters".
 * [rel](rel.md) - A link relation associated with a Link. The value MUST conform to both the [HTML5] and [RFC5988] "link relation" definitions.
 * [relationship](relationship.md) - On a Relationship object, the relationship property identifies the kind of relationship that exists between subject and object.
 * [replies](replies.md) - Identifies a Collection containing objects considered to be responses to this object.
 * [result](result.md) - Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.
 * [startIndex](startIndex.md) - A non-negative integer value identifying the relative position within the logical view of a strictly ordered collection.
 * [startTime](startTime.md) - The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.
 * [subject](subject.md) - On a Relationship object, the subject property identifies one of the connected individuals. For instance, for a Relationship object describing "John is related to Sally", subject would refer to John.
 * [summary](summary.md) - A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.
 * [tag](tag.md) - One or more "tags" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.
 * [target](target.md) - Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition "to". For instance, in the activity "John added a movie to his wishlist", the target of the activity is John's wishlist. An activity can have more than one target.
 * [to](to.md) - Identifies an entity considered to be part of the public primary audience of an Object
 * [totalItems](totalItems.md) - A non-negative integer specifying the total number of objects contained by the logical view of the collection. This number might not reflect the actual number of items serialized within the Collection object instance.
 * [type](type.md) - Identifies the Object or Link type. Multiple values may be specified.
 * [units](units.md) - Specifies the measurement units for the radius and altitude properties on a Place object. If not specified, the default is assumed to be "m" for "meters".
 * [updated](updated.md) - The date and time at which the object was updated
 * [url](url.md) - Identifies one or more links to representations of the object
 * [width](width.md) - On a Link, specifies a hint as to the rendering width in device-independent pixels of the linked resource.

### Enums

 * [unitEnum](unitEnum.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [AnyURI](types/AnyURI.md)  ([String](types/String.md)) 
 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [DurationType](types/DurationType.md)  ([String](types/String.md)) 
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [LangString](types/LangString.md)  ([String](types/String.md)) 
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [NonNegativeInteger](types/NonNegativeInteger.md)  ([Integer](types/Integer.md)) 
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
