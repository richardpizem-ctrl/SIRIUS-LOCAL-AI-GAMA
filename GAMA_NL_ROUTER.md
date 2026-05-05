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
## NL Router Components

### 1. Input Normalizer
Prepares incoming text, voice transcripts, or OCR output.
- cleanup
- punctuation correction
- language detection
- tokenization

### 2. Intent Classifier
Determines what the user wants.
- rule-based patterns
- keyword detection
- lightweight offline ML model (optional)
- fallback heuristics

### 3. Routing Engine
Maps intents to modules.
- routing table
- priority rules
- fallback routes
- ambiguity resolution

### 4. Metadata Generator
Creates routing metadata for the Runtime.
- task category
- confidence score
- required module
- flags (vision, schoolwork, security)

### 5. Diagnostics Logger
Tracks routing decisions.
- input type
- detected intent
- selected module
- errors or fallback usage
## NL Router Execution Cycle

1. Receive normalized input from the Runtime.
2. Detect input type (text, voice transcript, OCR).
3. Run intent classification.
4. Match intent to routing rules.
5. Determine task category and target module.
6. Generate routing metadata.
7. Return routing result to the Runtime Task Dispatcher.
8. Log routing event for diagnostics.
9. Wait for next input.
