
# Class: Move


Indicates that the actor has moved object from origin to target. If the origin or target are not specified, either can be determined by context.

URI: [as:Move](http://www.w3.org/ns/activitystreams#Move)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Activity]^-[Move&#124;actor(i):string%20*;instrument(i):string%20*;object(i):string%20*;origin(i):string%20*;result(i):string%20*;target(i):string%20*;attachment(i):string%20*;attributedTo(i):string%20*;audience(i):string%20*;bcc(i):string%20*;bto(i):string%20*;cc(i):string%20*;content(i):string%20*;context(i):string%20*;generator(i):string%20*;icon(i):string%20*;image(i):string%20*;inReplyTo(i):string%20*;location(i):string%20*;name(i):string%20*;preview(i):string%20*;summary(i):string%20*;tag(i):string%20*;to(i):string%20*;url(i):string%20*;duration(i):durationType%20%3F;endTime(i):datetime%20%3F;id(i):anyURI%20%3F;mediaType(i):string%20%3F;published(i):datetime%20%3F;startTime(i):datetime%20%3F;updated(i):datetime%20%3F],[Collection],[Activity])](https://yuml.me/diagram/nofunky;dir:TB/class/[Activity]^-[Move&#124;actor(i):string%20*;instrument(i):string%20*;object(i):string%20*;origin(i):string%20*;result(i):string%20*;target(i):string%20*;attachment(i):string%20*;attributedTo(i):string%20*;audience(i):string%20*;bcc(i):string%20*;bto(i):string%20*;cc(i):string%20*;content(i):string%20*;context(i):string%20*;generator(i):string%20*;icon(i):string%20*;image(i):string%20*;inReplyTo(i):string%20*;location(i):string%20*;name(i):string%20*;preview(i):string%20*;summary(i):string%20*;tag(i):string%20*;to(i):string%20*;url(i):string%20*;duration(i):durationType%20%3F;endTime(i):datetime%20%3F;id(i):anyURI%20%3F;mediaType(i):string%20%3F;published(i):datetime%20%3F;startTime(i):datetime%20%3F;updated(i):datetime%20%3F],[Collection],[Activity])

## Parents

 *  is_a: [Activity](Activity.md) - An Activity is a subtype of Object that describes some form of action that may happen, is currently happening, or has already happened. The Activity type itself serves as an abstract base type for all types of activities. It is important to note that the Activity type itself does not carry any specific semantics about the kind of action being taken.

## Attributes


### Inherited from Activity:

 * [attachment](attachment.md)  <sub>0..\*</sub>
     * Description: Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email.
     * Range: [String](types/String.md)
 * [attributedTo](attributedTo.md)  <sub>0..\*</sub>
     * Description: Identifies one or more entities to which this object is attributed. The attributed entities might not be Actors. For instance, an object might be attributed to the completion of another activity.
     * Range: [String](types/String.md)
 * [audience](audience.md)  <sub>0..\*</sub>
     * Description: Identifies one or more entities that represent the total population of entities for which the object can considered to be relevant.
     * Range: [String](types/String.md)
 * [bcc](bcc.md)  <sub>0..\*</sub>
     * Description: Identifies one or more Objects that are part of the private secondary audience of this Object.
     * Range: [String](types/String.md)
 * [bto](bto.md)  <sub>0..\*</sub>
     * Description: Identifies an Object that is part of the private primary audience of this Object.
     * Range: [String](types/String.md)
 * [cc](cc.md)  <sub>0..\*</sub>
     * Description: Identifies an Object that is part of the public secondary audience of this Object.
     * Range: [String](types/String.md)
 * [content](content.md)  <sub>0..\*</sub>
     * Description: The content or textual representation of the Object encoded as a JSON string. By default, the value of content is HTML. The mediaType property can be used in the object to indicate a different content type. The content MAY be expressed using multiple language-tagged values.
     * Range: [String](types/String.md)
 * [context](context.md)  <sub>0..\*</sub>
     * Description: Identifies the context within which the object exists or an activity was performed.
The notion of "context" used is intentionally vague. The intended function is to serve as a means of grouping objects and activities that share a common originating context or purpose. An example could be all activities relating to a common project or event.

     * Range: [String](types/String.md)
 * [generator](generator.md)  <sub>0..\*</sub>
     * Description: Identifies the entity (e.g. an application) that generated the object.
     * Range: [String](types/String.md)
 * [icon](icon.md)  <sub>0..\*</sub>
     * Description: Indicates an entity that describes an icon for this object. The image should have an aspect ratio of one (horizontal) to one (vertical) and should be suitable for presentation at a small size.
     * Range: [String](types/String.md)
 * [image](image.md)  <sub>0..\*</sub>
     * Description: Indicates an entity that describes an image for this object. Unlike the icon property, there are no aspect ratio or display size limitations assumed.
     * Range: [String](types/String.md)
 * [inReplyTo](inReplyTo.md)  <sub>0..\*</sub>
     * Description: Indicates one or more entities for which this object is considered a response.
     * Range: [String](types/String.md)
 * [location](location.md)  <sub>0..\*</sub>
     * Description: Indicates one or more physical or logical locations associated with the object.
     * Range: [String](types/String.md)
 * [name](name.md)  <sub>0..\*</sub>
     * Description: A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.
     * Range: [String](types/String.md)
 * [preview](preview.md)  <sub>0..\*</sub>
     * Description: Identifies an entity that provides a preview of this object.
     * Range: [String](types/String.md)
 * [replies](replies.md)  <sub>0..1</sub>
     * Description: Identifies a Collection containing objects considered to be responses to this object.
     * Range: [Collection](Collection.md)
 * [summary](summary.md)  <sub>0..\*</sub>
     * Description: A natural language summarization of the object encoded as HTML. Multiple language tagged summaries MAY be provided.
     * Range: [String](types/String.md)
 * [tag](tag.md)  <sub>0..\*</sub>
     * Description: One or more "tags" that have been associated with an objects. A tag can be any kind of Object. The key difference between attachment and tag is that the former implies association by inclusion, while the latter implies associated by reference.
     * Range: [String](types/String.md)
 * [to](to.md)  <sub>0..\*</sub>
     * Description: Identifies an entity considered to be part of the public primary audience of an Object
     * Range: [String](types/String.md)
 * [url](url.md)  <sub>0..\*</sub>
     * Description: Identifies one or more links to representations of the object
     * Range: [String](types/String.md)
 * [duration](duration.md)  <sub>0..1</sub>
     * Description: When the object describes a time-bound resource, such as an audio or video, a meeting, etc, the duration property indicates the object's approximate duration. The value MUST be expressed as an xsd:duration as defined by [ xmlschema11-2], section 3.3.6 (e.g. a period of 5 seconds is represented as "PT5S").
     * Range: [DurationType](types/DurationType.md)
 * [endTime](endTime.md)  <sub>0..1</sub>
     * Description: The date and time describing the actual or expected ending time of the object. When used with an Activity object, for instance, the endTime property specifies the moment the activity concluded or is expected to conclude.
     * Range: [Datetime](types/Datetime.md)
 * [id](id.md)  <sub>0..1</sub>
     * Description: Provides the globally unique identifier for an Object or Link.
     * Range: [AnyURI](types/AnyURI.md)
 * [mediaType](mediaType.md)  <sub>0..1</sub>
     * Description: When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.

     * Range: [String](types/String.md)
 * [published](published.md)  <sub>0..1</sub>
     * Description: The date and time at which the object was published
     * Range: [Datetime](types/Datetime.md)
 * [startTime](startTime.md)  <sub>0..1</sub>
     * Description: The date and time describing the actual or expected starting time of the object. When used with an Activity object, for instance, the startTime property specifies the moment the activity began or is scheduled to begin.
     * Range: [Datetime](types/Datetime.md)
 * [updated](updated.md)  <sub>0..1</sub>
     * Description: The date and time at which the object was updated
     * Range: [Datetime](types/Datetime.md)
 * [actor](actor.md)  <sub>0..\*</sub>
     * Description: Describes one or more entities that either performed or are expected to perform the activity. Any single activity can have multiple actors. The actor MAY be specified using an indirect Link.
     * Range: [String](types/String.md)
 * [instrument](instrument.md)  <sub>0..\*</sub>
     * Description: Identifies one or more objects used (or to be used) in the completion of an Activity.
     * Range: [String](types/String.md)
 * [object](object.md)  <sub>0..\*</sub>
     * Description: When used within an Activity, describes the direct object of the activity. For instance, in the activity "John added a movie to his wishlist", the object of the activity is the movie added.
When used within a Relationship describes the entity to which the subject is related.

     * Range: [String](types/String.md)
 * [origin](origin.md)  <sub>0..\*</sub>
     * Description: Describes an indirect object of the activity from which the activity is directed. The precise meaning of the origin is the object of the English preposition "from". For instance, in the activity "John moved an item to List B from List A", the origin of the activity is "List A".
     * Range: [String](types/String.md)
 * [result](result.md)  <sub>0..\*</sub>
     * Description: Describes the result of the activity. For instance, if a particular action results in the creation of a new resource, the result property can be used to describe that new resource.
     * Range: [String](types/String.md)
 * [target](target.md)  <sub>0..\*</sub>
     * Description: Describes the indirect object, or target, of the activity. The precise meaning of the target is largely dependent on the type of action being described but will often be the object of the English preposition "to". For instance, in the activity "John added a movie to his wishlist", the target of the activity is John's wishlist. An activity can have more than one target.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | as:Move |

