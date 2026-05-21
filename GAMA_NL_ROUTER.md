# 🧭 GAMA NL Router — Version 3.1.0

The NL Router in **GAMA 3.1.0** is responsible for interpreting user input, classifying intent, and routing tasks through the **Unified Event Architecture 3.1.x**.  
It supports hybrid inputs, deterministic routing, metadata v3.1, PACK_SUGGEST routing, improved fallback logic, and full safety‑aware routing.

Version 3.1.0 stabilizes the routing engine, reduces event collisions, improves hybrid‑safe behavior, and introduces unified result schema v3.1.

---

# 🎯 Responsibilities
- intent detection  
- task classification  
- deterministic routing  
- PACK_SUGGEST routing (NEW in 3.1)  
- fallback handling  
- ambiguity resolution  
- module priority scoring v3.1  
- event normalization (EV3.1)  
- metadata v3.1 generation  
- safety‑aware routing  
- hybrid‑safe routing rules  
- restricted/sandbox enforcement  

---

# 📝 Input Types (v3.1)
- text  
- voice (transcribed)  
- OCR (Vision Engine 3.1 output)  
- dict‑based fallback events  
- hybrid inputs (text + OCR combined)  
- low‑trust inputs (quarantine pipeline)  
- PACK_SUGGEST prefix queries  

---

# 📤 Output (v3.1)
- task category  
- target module  
- routing metadata v3.1  
- confidence score  
- safety flags  
- fallback reason  
- event version tag (EV3.1)  
- trust level  
- restricted/sandbox flags  
- unified result schema v3.1  

---

# 🏷 Version
**GAMA NL Router — v3.1.0**  
(fully aligned with Runtime 3.1.0 and Unified Event Architecture 3.1.x)

---

# 🔄 NL Router Flow (v3.1.0)

1. Receive normalized input from the Runtime.  
2. Detect input type:  
   - text  
   - voice transcript  
   - OCR (vision output)  
   - dict fallback  
   - hybrid input  
   - PACK_SUGGEST prefix  
3. Perform intent classification.  
4. Apply safety‑intent detection.  
5. Match intent to deterministic routing rules.  
6. Determine task category:  
   - vision  
   - knowledge pack  
   - PACK_SUGGEST  
   - schoolwork  
   - security  
   - general assistant  
   - diagnostics  
   - system/meta commands  
7. Generate metadata v3.1.  
8. Apply restricted/sandbox rules if required.  
9. Produce unified result schema v3.1.  
10. Return routing result to the Runtime Dispatcher.  
11. Log routing event for diagnostics.  

---

# 🧩 NL Router Components (v3.1)

## 1. Input Normalizer (v3.1)
Prepares incoming text, voice transcripts, OCR output, and hybrid inputs.

- cleanup  
- punctuation correction  
- language detection  
- tokenization  
- hybrid input merging  
- dict → text normalization  
- low‑trust input tagging  
- PACK_SUGGEST prefix extraction  

---

## 2. Intent Classifier (v3.1)
Determines what the user wants.

- rule‑based patterns  
- keyword detection  
- PACK_SUGGEST detection  
- fallback heuristics  
- multi‑intent detection  
- safety‑intent detection  
- hybrid‑safe classification  
- improved ambiguity resolution  

---

## 3. Routing Engine (v3.1)
Maps intents to modules using deterministic routing.

- routing table v3.1  
- priority rules  
- fallback routes  
- ambiguity resolution  
- module priority scoring v3.1  
- PACK_SUGGEST routing  
- safety‑aware routing  
- EV3.1 event mapping  
- restricted/sandbox enforcement  
- reduced routing collisions  

---

## 4. Metadata Generator (v3.1)
Creates routing metadata for the Runtime.

- task category  
- confidence score  
- required module  
- flags (vision, schoolwork, security, packs)  
- safety flags  
- fallback reason  
- event version tag (EV3.1)  
- trust level  
- restricted/sandbox flags  
- PACK_SUGGEST metadata  
- unified result schema v3.1  

---

## 5. Diagnostics Logger (v3.1)
Tracks routing decisions.

- input type  
- detected intent  
- selected module  
- errors or fallback usage  
- confidence score  
- rule hits  
- PACK_SUGGEST hits  
- ambiguity resolution logs  
- metadata v3.1 trace  
- restricted/sandbox events  
- hybrid‑safe routing logs  

---

# 🔁 NL Router Execution Cycle (v3.1.0)

1. Receive normalized input from the Runtime.  
2. Detect input type (text, voice, OCR, dict, hybrid, PACK_SUGGEST).  
3. Run intent classification.  
4. Apply safety‑intent detection.  
5. Match intent to routing rules.  
6. Determine task category and target module.  
7. Generate metadata v3.1.  
8. Apply restricted/sandbox rules.  
9. Produce unified result schema v3.1.  
10. Return routing result to the Runtime Dispatcher.  
11. Log routing event for diagnostics.  
12. Wait for next input.  

---

# 🟪 NEW IN VERSION 3.1.0
- PACK_SUGGEST support  
- metadata v3.1  
- event versioning EV3.1  
- unified result schema v3.1  
- improved hybrid‑safe routing  
- reduced event collisions  
- improved fallback logic  
- diagnostics expansion v3.1  
- module priority scoring v3.1  
- runtime_info routing support  

---

# ✔ GAMA NL Router 3.1 — COMPLETE  
Fully aligned with the SIRIUS LOCAL AI GAMA 3.1.x ecosystem.
