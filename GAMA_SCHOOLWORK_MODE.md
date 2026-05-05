# GAMA Schoolwork Mode

Schoolwork Mode provides offline reasoning and problem‑solving for students.

## Responsibilities
- math problem solving
- text analysis
- explanations and step-by-step reasoning
- OCR-based homework support
- offline knowledge usage

## Input Types
- text questions
- OCR from Vision Engine
- structured tasks

## Output
- solutions
- explanations
- steps
- reasoning trace

## Version
GAMA Schoolwork Mode — v1.0.0
## Schoolwork Flow

1. Receive input from Runtime (text or OCR).
2. Detect subject type:
   - math
   - language
   - science
   - general knowledge
3. Load appropriate Knowledge Pack.
4. Normalize the problem or question.
5. Apply reasoning rules based on subject.
6. Generate solution steps.
7. Produce final explanation and answer.
8. Return structured output to Runtime.
9. Log schoolwork event for diagnostics.
