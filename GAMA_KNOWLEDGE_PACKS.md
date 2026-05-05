# GAMA Knowledge Packs

Knowledge Packs provide offline knowledge modules used by the GAMA Runtime and NL Router.

## Purpose
- enable offline reasoning
- provide structured knowledge
- support schoolwork mode
- enhance general assistant capabilities
- reduce dependency on online sources

## Types of Knowledge Packs
- math
- language
- science
- history
- geography
- general knowledge
- custom user packs

## Structure
Each pack contains:
- metadata.json
- knowledge.json
- rules.json
- examples.json

## Version
GAMA Knowledge Packs — v1.0.0
## Knowledge Pack Flow

1. Runtime requests a knowledge pack based on task category.
2. Pack Loader checks if the pack exists locally.
3. If missing, fallback pack is used.
4. metadata.json is parsed to identify pack type and version.
5. knowledge.json is loaded into memory.
6. rules.json is applied to structure reasoning.
7. examples.json is used for pattern matching.
8. Pack returns structured knowledge to the Runtime.
9. Runtime uses the knowledge to complete the task.
10. Diagnostics log the pack usage.
