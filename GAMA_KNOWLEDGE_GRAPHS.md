# How SIRIUS GAMA’s local knowledge graph works

SIRIUS GAMA can answer supported Slovak school questions from a local knowledge pack. The Windows panel accepts a question such as “Povedz mi o aute” (“Tell me about the car”), looks up a stored relationship, and shows the answer together with its source.

## What the pack stores

The school pack, `gama_school_kg.json`, keeps vocabulary and facts in separate sections of the same JSON file.

| Section | Role | Example |
| --- | --- | --- |
| `lexicon` | Maps words and grammatical forms to entity IDs | `auto` and `aute` both map to `1103` |
| `entities` | Maps entity IDs to display names | `1103` is `auto`, `1104` is `vozidlo` |
| `relations` | Maps relationship IDs to labels | `51` means `je` (“is”) |
| `graph.edges` | Stores facts as links between entities | `1103` → `51` → `1104` means “A car is a vehicle” |
| `sources` | Identifies where a stored fact came from | The edge’s `provenance` value `1` points to the GAMA school pack |

These numbers are internal identifiers defined by the pack. Its `schema_version` identifies the JSON format. Since word forms live in the lexicon, another form can point to `1103` and reuse the same stored fact.

## From a question to an answer

GAMA recognizes the supported pattern “Povedz mi o …” and extracts `aute`. It checks the normalized spelling first and falls back to a comparison without diacritics when that spelling has no match. The lexicon resolves `aute` to `1103`. GAMA then looks up the `je` relationship and returns `vozidlo` (“vehicle”) together with the source label.

If a term maps to multiple entities, GAMA asks the user to clarify. We verified both paths in the Windows panel:

- **Povedz mi o myši** (“Tell me about the mouse”) shows two choices: `počítačová myš` (computer mouse) and `myš domová` (house mouse).
- **Povedz mi o počítačovej myši** (“Tell me about the computer mouse”) resolves to one entity and returns `vstupné zariadenie` (“input device”) with its source.

The school graph covers the question patterns and vocabulary defined in the pack. When no matching fact is available, the lookup returns `not_found`. We also verified a local photosynthesis query after restarting GAMA with Wi-Fi disabled.

The Slovak query and clarification changes are in [PR #45](https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-GAMA/pull/45).

What Slovak word forms or ambiguous terms would you like to see in the next school pack examples?
