
# Class: Mention


A specialized Link that represents an @mention.

URI: [as:Mention](http://www.w3.org/ns/activitystreams#Mention)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Link]^-[Mention&#124;name(i):string%20*;preview(i):string%20*;height(i):nonNegativeInteger%20%3F;href(i):anyURI%20%3F;hreflang(i):string%20%3F;id(i):anyURI%20%3F;mediaType(i):string%20%3F;rel(i):string%20*;width(i):nonNegativeInteger%20%3F],[Link])](https://yuml.me/diagram/nofunky;dir:TB/class/[Link]^-[Mention&#124;name(i):string%20*;preview(i):string%20*;height(i):nonNegativeInteger%20%3F;href(i):anyURI%20%3F;hreflang(i):string%20%3F;id(i):anyURI%20%3F;mediaType(i):string%20%3F;rel(i):string%20*;width(i):nonNegativeInteger%20%3F],[Link])

## Parents

 *  is_a: [Link](Link.md) - A Link is an indirect, qualified reference to a resource identified by a URL. The fundamental model for links is established by [ RFC5988]. Many of the properties defined by the Activity Vocabulary allow values that are either instances of Object or Link. When a Link is used, it establishes a qualified relation connecting the subject (the containing object) to the resource identified by the href. Properties of the Link are properties of the reference as opposed to properties of the resource.

## Attributes


### Inherited from Link:

 * [name](name.md)  <sub>0..\*</sub>
     * Description: A simple, human-readable, plain-text name for the object. HTML markup MUST NOT be included. The name MAY be expressed using multiple language-tagged values.
     * Range: [String](types/String.md)
 * [preview](preview.md)  <sub>0..\*</sub>
     * Description: Identifies an entity that provides a preview of this object.
     * Range: [String](types/String.md)
 * [height](height.md)  <sub>0..1</sub>
     * Description: On a Link, specifies a hint as to the rendering height in device-independent pixels of the linked resource.
     * Range: [NonNegativeInteger](types/NonNegativeInteger.md)
 * [href](href.md)  <sub>0..1</sub>
     * Description: The target resource pointed to by a Link.
     * Range: [AnyURI](types/AnyURI.md)
 * [hreflang](hreflang.md)  <sub>0..1</sub>
     * Description: Hints as to the language used by the target resource. Value MUST be a [BCP47] Language-Tag.
     * Range: [String](types/String.md)
 * [id](id.md)  <sub>0..1</sub>
     * Description: Provides the globally unique identifier for an Object or Link.
     * Range: [AnyURI](types/AnyURI.md)
 * [mediaType](mediaType.md)  <sub>0..1</sub>
     * Description: When used on a Link, identifies the MIME media type of the referenced resource.
When used on an Object, identifies the MIME media type of the value of the content property. If not specified, the content property is assumed to contain text/html content.

     * Range: [String](types/String.md)
 * [rel](rel.md)  <sub>0..\*</sub>
     * Description: A link relation associated with a Link. The value MUST conform to both the [HTML5] and [RFC5988] "link relation" definitions.
In the [HTML5], any string not containing the "space" U+0020, "tab" (U+0009), "LF" (U+000A), "FF" (U+000C), "CR" (U+000D) or "," (U+002C) characters can be used as a valid link relation.

     * Range: [String](types/String.md)
 * [width](width.md)  <sub>0..1</sub>
     * Description: On a Link, specifies a hint as to the rendering width in device-independent pixels of the linked resource.
     * Range: [NonNegativeInteger](types/NonNegativeInteger.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | as:Mention |

