# GAMA NL Router

The NL Router is responsible for interpreting user input and determining the correct task category.

## Responsibilities
- intent detection
- task classification
- routing logic
- fallback handling
- ambiguity resolution

## Input Types
- text
- voice (transcribed)
- OCR (vision engine output)

## Output
- task category
- module target
- routing metadata

## Version
GAMA NL Router — v1.0.0
## NL Router Flow

1. Receive normalized user input from the Runtime.
2. Detect input type:
   - text
   - voice (transcribed)
   - OCR (vision output)
3. Perform intent classification.
4. Match intent to routing rules.
5. Determine task category:
   - vision
   - knowledge pack
   - schoolwork
   - security
   - general assistant
6. Generate routing metadata.
7. Send routing result back to the Runtime Task Dispatcher.
8. Log routing event for diagnostics.
