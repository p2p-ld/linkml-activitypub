
# Class: Object


Describes an object of any kind. The Object type serves as the base type for most of the other kinds of objects defined in the Activity Vocabulary, including other Core types such as Activity, IntransitiveActivity, Collection and OrderedCollection.

URI: [as:Object](http://www.w3.org/ns/activitystreams#Object)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Tombstone],[Service],[Relationship],[Profile],[Place],[Person],[Page],[Organization],[Collection]<replies%200..1-++[Object&#124;attachment:string%20*;attributedTo:string%20*;audience:string%20*;bcc:string%20*;bto:string%20*;cc:string%20*;content:string%20*;context:string%20*;generator:string%20*;icon:string%20*;image:string%20*;inReplyTo:string%20*;location:string%20*;name:string%20*;preview:string%20*;summary:string%20*;tag:string%20*;to:string%20*;url:string%20*;duration:durationType%20%3F;endTime:datetime%20%3F;id:anyURI%20%3F;mediaType:string%20%3F;published:datetime%20%3F;startTime:datetime%20%3F;updated:datetime%20%3F],[Profile]++-%20describes%200..1>[Object],[Tombstone]++-%20formerType%200..*>[Object],[Relationship]++-%20relationship%200..*>[Object],[Object]^-[Tombstone],[Object]^-[Service],[Object]^-[Relationship],[Object]^-[Profile],[Object]^-[Place],[Object]^-[Person],[Object]^-[Page],[Object]^-[Organization],[Object]^-[Note],[Object]^-[Group],[Object]^-[Event],[Object]^-[Document],[Object]^-[Collection],[Object]^-[Article],[Object]^-[Application],[Object]^-[Activity],[Note],[Group],[Event],[Document],[Collection],[Article],[Application],[Activity])](https://yuml.me/diagram/nofunky;dir:TB/class/[Tombstone],[Service],[Relationship],[Profile],[Place],[Person],[Page],[Organization],[Collection]<replies%200..1-++[Object&#124;attachment:string%20*;attributedTo:string%20*;audience:string%20*;bcc:string%20*;bto:string%20*;cc:string%20*;content:string%20*;context:string%20*;generator:string%20*;icon:string%20*;image:string%20*;inReplyTo:string%20*;location:string%20*;name:string%20*;preview:string%20*;summary:string%20*;tag:string%20*;to:string%20*;url:string%20*;duration:durationType%20%3F;endTime:datetime%20%3F;id:anyURI%20%3F;mediaType:string%20%3F;published:datetime%20%3F;startTime:datetime%20%3F;updated:datetime%20%3F],[Profile]++-%20describes%200..1>[Object],[Tombstone]++-%20formerType%200..*>[Object],[Relationship]++-%20relationship%200..*>[Object],[Object]^-[Tombstone],[Object]^-[Service],[Object]^-[Relationship],[Object]^-[Profile],[Object]^-[Place],[Object]^-[Person],[Object]^-[Page],[Object]^-[Organization],[Object]^-[Note],[Object]^-[Group],[Object]^-[Event],[Object]^-[Document],[Object]^-[Collection],[Object]^-[Article],[Object]^-[Application],[Object]^-[Activity],[Note],[Group],[Event],[Document],[Collection],[Article],[Application],[Activity])

## Children

 * [Activity](Activity.md) - An Activity is a subtype of Object that describes some form of action that may happen, is currently happening, or has already happened. The Activity type itself serves as an abstract base type for all types of activities. It is important to note that the Activity type itself does not carry any specific semantics about the kind of action being taken.
 * [Application](Application.md) - Describes a software application.
 * [Article](Article.md)
 * [Collection](Collection.md) - A Collection is a subtype of Object that represents ordered or unordered sets of Object or Link instances. Refer to the Activity Streams 2.0 Core specification for a complete description of the Collection type.
 * [Document](Document.md) - Represents a document of any kind.
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

## Referenced by Class

 *  **None** *[describes](describes.md)*  <sub>0..1</sub>  **[Object](Object.md)**
 *  **None** *[formerType](formerType.md)*  <sub>0..\*</sub>  **[Object](Object.md)**
 *  **None** *[relationship](relationship.md)*  <sub>0..\*</sub>  **[Object](Object.md)**

## Attributes


### Own

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | as:Object |

