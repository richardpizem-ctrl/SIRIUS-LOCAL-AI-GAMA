# 🧭 GAMA NL Router — Version 3.0.0

The NL Router in **GAMA 3.0.0** is responsible for interpreting user input, classifying intent, and routing tasks through the **Unified Event Architecture 3.x**.  
It supports hybrid inputs, deterministic routing, metadata v3, fallback normalization, and full safety‑aware routing.

---

# 🎯 Responsibilities
- intent detection  
- task classification  
- deterministic routing  
- fallback handling  
- ambiguity resolution  
- module priority scoring v3  
- event normalization (EV3)  
- metadata v3 generation  
- safety‑aware routing  
- hybrid‑safe routing rules  

---

# 📝 Input Types (v3)
- text  
- voice (transcribed)  
- OCR (Vision Engine 3.0 output)  
- dict‑based fallback events  
- hybrid inputs (text + OCR combined)  
- low‑trust inputs (quarantine pipeline)  

---

# 📤 Output (v3)
- task category  
- target module  
- routing metadata v3  
- confidence score  
- safety flags  
- fallback reason  
- event version tag (EV3)  
- trust level  
- restricted/sandbox flags  

---

# 🏷 Version
**GAMA NL Router — v3.0.0**  
(fully aligned with Runtime 3.0.0 and Unified Event Architecture 3.x)

---

# 🔄 NL Router Flow (v3.0.0)

1. Receive normalized input from the Runtime.  
2. Detect input type:  
   - text  
   - voice transcript  
   - OCR (vision output)  
   - dict fallback  
   - hybrid input  
3. Perform intent classification.  
4. Apply safety‑intent detection.  
5. Match intent to deterministic routing rules.  
6. Determine task category:  
   - vision  
   - knowledge pack  
   - schoolwork  
   - security  
   - general assistant  
   - diagnostics  
   - system/meta commands  
7. Generate metadata v3.  
8. Apply restricted/sandbox rules if required.  
9. Return routing result to the Runtime Dispatcher.  
10. Log routing event for diagnostics.  

---

# 🧩 NL Router Components (v3)

## 1. Input Normalizer (v3)
Prepares incoming text, voice transcripts, OCR output, and hybrid inputs.

- cleanup  
- punctuation correction  
- language detection  
- tokenization  
- hybrid input merging  
- dict → text normalization  
- low‑trust input tagging  

---

## 2. Intent Classifier (v3)
Determines what the user wants.

- rule‑based patterns  
- keyword detection  
- lightweight offline ML model (optional)  
- fallback heuristics  
- multi‑intent detection  
- safety‑intent detection  
- hybrid‑safe classification  

---

## 3. Routing Engine (v3)
Maps intents to modules using deterministic routing.

- routing table v3  
- priority rules  
- fallback routes  
- ambiguity resolution  
- module priority scoring v3  
- safety‑aware routing  
- EV3 event mapping  
- restricted/sandbox enforcement  

---

## 4. Metadata Generator (v3)
Creates routing metadata for the Runtime.

- task category  
- confidence score  
- required module  
- flags (vision, schoolwork, security)  
- safety flags  
- fallback reason  
- event version tag (EV3)  
- trust level  
- restricted/sandbox flags  

---

## 5. Diagnostics Logger (v3)
Tracks routing decisions.

- input type  
- detected intent  
- selected module  
- errors or fallback usage  
- confidence score  
- rule hits  
- ambiguity resolution logs  
- metadata v3 trace  
- restricted/sandbox events  

---

# 🔁 NL Router Execution Cycle (v3.0.0)

1. Receive normalized input from the Runtime.  
2. Detect input type (text, voice, OCR, dict, hybrid).  
3. Run intent classification.  
4. Apply safety‑intent detection.  
5. Match intent to routing rules.  
6. Determine task category and target module.  
7. Generate metadata v3.  
8. Apply restricted/sandbox rules.  
9. Return routing result to the Runtime Dispatcher.  
10. Log routing event for diagnostics.  
11. Wait for next input.  

---

# 🟪 NEW IN VERSION 3.0.0
- deterministic routing v3  
- metadata v3  
- event versioning EV3  
- hybrid‑safe routing  
- low‑trust input tagging  
- restricted/sandbox enforcement  
- unified fallback normalization  
- diagnostics expansion v3  
- module priority scoring v3  
- unified event architecture integration  

---

# ✔ GAMA NL Router 3.0 — COMPLETE  
Fully aligned with the SIRIUS LOCAL AI GAMA 3.x ecosystem.
