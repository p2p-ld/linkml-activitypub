# linkml-activitypub

LinkML representation of ActivityPub schema (which is mostly ActivityStreams except where it's not)

## Process

Intermediate files are in the `data` directory

- `activitystreams2.owl` - Initially imported from [activitystreams2.owl](https://github.com/w3c/activitystreams/blob/5910a59a6f46c1f8ec9fb028bd8bbb65a7332e4e/vocabulary/activitystreams2.owl)
  - Removed problematic OrderedCollection definitions
- `activitystreams2.ofn` - Convert to functional notation with [robot](http://robot.obolibrary.org/)
- `activitystreams2.yaml` - Then to rough linkml using [schema-automator](https://linkml.io/schema-automator/)

Then the final schema in 
- Manually refined...

# References

- Status of AS OWL vocabulary and etc. https://github.com/w3c/activitystreams/issues/416

# See Also

- https://github.com/steve-bate/activitypub-ontology