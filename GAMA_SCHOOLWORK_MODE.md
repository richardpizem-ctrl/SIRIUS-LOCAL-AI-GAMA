# 🎓 GAMA Schoolwork Mode — Version 2.0.0

Schoolwork Mode provides **offline reasoning and problem‑solving** for students in GAMA 2.0.0.  
Fully deterministic, family‑safe, hybrid‑input capable.

---

# 🎯 Responsibilities
- math problem solving  
- text analysis  
- explanations and step‑by‑step reasoning  
- OCR‑based homework support  
- offline knowledge usage  
- mixed‑subject reasoning  
- safety‑filtered educational output  
- deterministic reasoning trace  

---

# 📝 Input Types
- text questions  
- OCR from Vision Engine  
- structured tasks  
- hybrid inputs (text + OCR combined)  
- dict‑based fallback from Vision  

---

# 📤 Output
- solutions  
- explanations  
- steps  
- reasoning trace  
- subject metadata  
- confidence score  

---

# 🏷 Version
**GAMA Schoolwork Mode — v2.0.0**  
(compatible with Runtime 2.0, prepared for Runtime 3.0.0‑pre)

---

# 🔄 Schoolwork Flow (v2.0.0)

1. Receive input from Runtime (text or OCR).  
2. Detect subject type:  
   - math  
   - language  
   - science  
   - general knowledge  
   - mixed subjects  
3. Load appropriate Knowledge Pack.  
4. Normalize the problem or question.  
5. Apply reasoning rules based on subject.  
6. Generate solution steps.  
7. Produce final explanation and answer.  
8. Add reasoning trace + metadata.  
9. Return structured output to Runtime.  
10. Log schoolwork event for diagnostics.  

---

# 🧩 Schoolwork Components

## 1. Subject Detector
Identifies the subject of the task.
- math  
- language  
- science  
- general knowledge  
- mixed tasks  
- subject confidence scoring  
- fallback subject detection  

## 2. Problem Normalizer
Prepares the input for reasoning.
- cleanup  
- structure detection  
- OCR correction  
- math formatting  
- hybrid input merging  
- dict → text normalization  

## 3. Reasoning Engine
Core logic for solving tasks.
- step‑by‑step reasoning  
- rule‑based logic  
- pattern matching  
- offline inference  
- rule chaining  
- example‑based fallback reasoning  
- deterministic reasoning trace  

## 4. Knowledge Pack Integrator
Connects Schoolwork Mode with Knowledge Packs.
- pack selection  
- rule application  
- example matching  
- fallback handling  
- pack priority scoring  
- pack integrity validation  

## 5. Explanation Generator
Produces human‑readable explanations.
- step breakdown  
- reasoning trace  
- final summary  
- simplified child‑safe explanations  
- multi‑format output (short/long)  

## 6. Output Formatter
Structures the final result.
- solution  
- steps  
- explanation  
- metadata  
- subject tags  
- confidence score  

## 7. Diagnostics Logger
Tracks Schoolwork events.
- subject type  
- pack used  
- reasoning time  
- errors or fallbacks  
- rule hits  
- example hits  
- OCR quality score  

---

# 🔁 Schoolwork Execution Cycle (v2.0.0)

1. Runtime sends a schoolwork task (text or OCR).  
2. Subject Detector identifies the subject category.  
3. Problem Normalizer prepares the input for reasoning.  
4. Knowledge Pack Integrator loads the required pack.  
5. Reasoning Engine generates step‑by‑step reasoning.  
6. Explanation Generator produces a clear explanation.  
7. Output Formatter structures the final answer.  
8. Final result is returned to the Runtime.  
9. Diagnostics Logger records the schoolwork event.  
10. System waits for the next task.  

---

# 🟪 NEW IN VERSION 2 → PREPARED FOR VERSION 3.0.0‑pre
- hybrid input support  
- dict → event fallback normalization  
- rule chaining  
- example‑based fallback reasoning  
- deterministic reasoning trace  
- subject confidence scoring  
- pack priority scoring  
- pack integrity validation  
- child‑safe explanation mode  
- diagnostics expansion  
- unified SCHOOLWORK event metadata  
