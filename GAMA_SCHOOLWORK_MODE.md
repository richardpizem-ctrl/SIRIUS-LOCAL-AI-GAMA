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
## Schoolwork Components

### 1. Subject Detector
Identifies the subject of the task.
- math
- language
- science
- general knowledge
- mixed tasks

### 2. Problem Normalizer
Prepares the input for reasoning.
- cleanup
- structure detection
- OCR correction
- math formatting

### 3. Reasoning Engine
Core logic for solving tasks.
- step-by-step reasoning
- rule-based logic
- pattern matching
- offline inference

### 4. Knowledge Pack Integrator
Connects Schoolwork Mode with Knowledge Packs.
- pack selection
- rule application
- example matching
- fallback handling

### 5. Explanation Generator
Produces human‑readable explanations.
- step breakdown
- reasoning trace
- final summary

### 6. Output Formatter
Structures the final result.
- solution
- steps
- explanation
- metadata

### 7. Diagnostics Logger
Tracks Schoolwork events.
- subject type
- pack used
- reasoning time
- errors or fallbacks
