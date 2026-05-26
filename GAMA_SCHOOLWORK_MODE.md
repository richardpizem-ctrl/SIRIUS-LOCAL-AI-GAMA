# 🎓 GAMA Schoolwork Mode — Version 3.2.0

Schoolwork Mode provides **offline, deterministic academic reasoning** for students in GAMA 3.2.0.  
It integrates with the Unified Event Architecture 3.2.x, Metadata v3.2, Knowledge Packs 3.2,  
the hybrid‑safe pipeline, PACK_SUGGEST routing, VisionEngineV3 HOMEWORK events,  
and the unified result schema v3.2.

Version 3.2.0 introduces **VisionEngineV3 homework routing**, improved fallback logic,  
enhanced hybrid‑safe behavior, PACK_SUGGEST v3.2, and deterministic academic reasoning flow.

---

# 🎯 Responsibilities
- math problem solving  
- text analysis  
- step‑by‑step reasoning  
- OCR‑based homework support (VisionEngineV3 HOMEWORK event)  
- deterministic academic explanations  
- mixed‑subject reasoning  
- hybrid input support (text + OCR)  
- safety‑filtered educational output  
- reasoning_trace v3.2 generation  
- metadata v3.2 integration  
- PACK_SUGGEST academic prefix search  
- unified result schema v3.2  

---

# 📝 Input Types (v3.2)
- text questions  
- OCR from VisionEngineV3  
- HOMEWORK events (VisionEngineV3)  
- structured tasks  
- hybrid inputs (text + OCR combined)  
- dict‑based fallback events  
- low‑trust inputs (quarantine pipeline)  
- PACK_SUGGEST academic queries  

---

# 📤 Output (v3.2)
- solution  
- explanation  
- step‑by‑step reasoning  
- reasoning_trace v3.2  
- subject metadata  
- confidence score  
- safety flags  
- event version tag (EV3.2)  
- unified result schema v3.2  

---

# 🏷 Version
**GAMA Schoolwork Mode — v3.2.0**  
(fully aligned with Runtime 3.2.0, VisionEngineV3, and Unified Event Architecture 3.2.x)

---

# 🔄 Schoolwork Flow (v3.2.0)

1. Receive SCHOOLWORK_EVENT (EV3.2) from Runtime or HOMEWORK event from VisionEngineV3.  
2. Detect subject type:  
   - math  
   - language  
   - science  
   - general knowledge  
   - mixed subjects  
3. Load appropriate Knowledge Pack (v3.2).  
4. Normalize the problem or question.  
5. Apply deterministic reasoning rules.  
6. Generate step‑by‑step solution.  
7. Produce final explanation.  
8. Add reasoning_trace v3.2 + metadata v3.2.  
9. Format output using unified result schema v3.2.  
10. Return structured SCHOOLWORK_EVENT response.  
11. Log event for diagnostics.  

---

# 🧩 Schoolwork Components (v3.2)

## 1. Subject Detector v3.2
Identifies the subject category.
- math / language / science / general knowledge  
- mixed‑subject detection  
- subject confidence scoring v3.2  
- fallback subject detection  
- hybrid‑safe subject classification  
- PACK_SUGGEST academic detection  
- HOMEWORK event subject extraction  

---

## 2. Problem Normalizer v3.2
Prepares the input for deterministic reasoning.
- cleanup  
- structure detection  
- OCR correction (VisionEngineV3)  
- math formatting  
- hybrid input merging  
- dict → text normalization  
- low‑trust input tagging  
- PACK_SUGGEST normalization  
- HOMEWORK event normalization  

---

## 3. Reasoning Engine v3.2
Core deterministic reasoning engine.
- step‑by‑step reasoning  
- rule‑based logic  
- pattern matching  
- offline inference  
- rule chaining v3.2  
- example‑based fallback reasoning v3.2  
- deterministic reasoning trace v3.2  
- sandbox‑safe execution  
- unified result schema integration  

---

## 4. Knowledge Pack Integrator v3.2
Connects Schoolwork Mode with Knowledge Packs 3.2.
- pack selection  
- rule application  
- example matching  
- fallback handling  
- pack priority scoring v3.2  
- pack integrity validation v3.2  
- compatibility flags v3.2  
- PACK_SUGGEST support  

---

## 5. Explanation Generator v3.2
Produces human‑readable explanations.
- step breakdown  
- reasoning trace  
- final summary  
- simplified child‑safe explanations  
- multi‑format output (short/long)  
- metadata v3.2 integration  
- unified result schema formatting  

---

## 6. Output Formatter v3.2
Structures the final result.
- solution  
- steps  
- explanation  
- metadata v3.2  
- subject tags  
- confidence score  
- safety flags  
- event version tag (EV3.2)  
- unified result schema v3.2  

---

## 7. Diagnostics Logger v3.2
Tracks Schoolwork events.
- subject type  
- pack used  
- reasoning time  
- errors or fallbacks  
- rule hits  
- example hits  
- OCR quality score  
- metadata trace v3.2  
- hybrid‑safe logs  
- PACK_SUGGEST logs  
- HOMEWORK event logs  

---

# 🔁 Schoolwork Execution Cycle (v3.2.0)

1. Runtime sends SCHOOLWORK_EVENT (EV3.2) or VisionEngineV3 sends HOMEWORK event.  
2. Subject Detector identifies the subject category.  
3. Problem Normalizer prepares the input.  
4. Knowledge Pack Integrator loads the required pack.  
5. Reasoning Engine generates deterministic reasoning.  
6. Explanation Generator produces the explanation.  
7. Output Formatter structures the final answer.  
8. SCHOOLWORK_EVENT response is returned to Runtime.  
9. Diagnostics Logger records the event.  
10. System waits for the next task.  

---

# 🟪 NEW IN VERSION 3.2.0
- metadata v3.2  
- event versioning EV3.2  
- unified result schema v3.2  
- VisionEngineV3 HOMEWORK event support  
- improved hybrid‑safe input handling  
- reduced reasoning collisions  
- improved fallback logic  
- rule chaining v3.2  
- example‑based fallback v3.2  
- pack priority v3.2  
- pack integrity v3.2  
- sandbox‑safe reasoning improvements  
- diagnostics expansion v3.2  

---

# ✔ GAMA Schoolwork Mode 3.2 — COMPLETE  
Fully aligned with the SIRIUS LOCAL AI GAMA 3.2.x ecosystem.
