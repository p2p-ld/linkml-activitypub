# linkml-activitypub

LinkML representation of ActivityPub schema (which is mostly ActivityStreams except where it's not)

## Process

Intermediate files are in the `data` directory

- `activitystreams2.owl` - Initially imported from [activitystreams2.owl](https://github.com/w3c/activitystreams/blob/5910a59a6f46c1f8ec9fb028bd8bbb65a7332e4e/vocabulary/activitystreams2.owl)
  - Removed problematic OrderedCollection definitions
- `activitystreams2.ofn` - Convert to functional notation with [robot](http://robot.obolibrary.org/)
- `activitystreams2.yaml` - Then to rough linkml using [schema-automator](https://linkml.io/schema-automator/)

Then the final schema in `linkml_activitypub/activitypub.yaml`:
- Reorder to match ActivityStreams 
- Ensure correct
  - inheritance
  - `multivalued`
- Prune extra properties and classes to match those in [ActivityStreams2](https://www.w3.org/TR/activitystreams-vocabulary/) normative definition
  - Then re-add the ones that declare a class in their domain, even if the class doesn't list that property in its definition
  - Except for those types that seem to be metaclasses:
    - `attributedTo` (-> `actor`)
- Added LinkML properties (where needed):
  - Classes
    - `disjoint_with`
    - `see_also` when references given
  - Properties
    - `description`
    - `domain`
    - `range`
    - `minumum_value`
    - `maximum_value`
- Added missing slots
  - `closed`
  - `startIndex`
- Handle special property cases
  - `items` is marked as `list_elements_ordered: true` on `OrderedCollection` and false on `Collection`
- Made types
  - anyURI as `xsd:anyURI`, did not try and find a validator pattern. The spec alternatingly uses its own anyURI prop and `xsd:anyURI`
- Made enums
  - `unitEnum` - for `unit`
- Copied Notes to class `description` rather than `comments`
- Added schema prefixes:
  - `schema`: https://schema.org/ - for specifying IETF BCP 47 language codes


## Notes

Need properties...


## Errata

- `OrderedCollectionPage` is not a subclass of, and doesn't mix in `CollectionPage` since it would then have an ambiguous
  class definition, since `OrderedCollection` inherits from `Collection` but asserts that the `list_items_ordered` slot is `true`
  rather than `false`. Instead, the slots from `CollectionPage` are just duplicated.
  - Accordingly, the domain and range of slots that include `CollectionPage` also include `OrderedCollectionPage

# References

- Status of AS OWL vocabulary and etc. https://github.com/w3c/activitystreams/issues/416

# See Also

- https://github.com/steve-bate/activitypub-ontology