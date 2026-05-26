# 🧭 GAMA NL Router — Version 3.2.0

The NL Router in **GAMA 3.2.0** is responsible for interpreting user input, classifying intent, and routing tasks through the **Unified Event Architecture 3.2.x**.  
It supports hybrid inputs, deterministic routing, metadata v3.2, PACK_SUGGEST routing, improved fallback logic, VisionEngineV3 routing, and full safety‑aware routing.

Version 3.2.0 stabilizes the routing engine, reduces event collisions, improves hybrid‑safe behavior, and introduces unified result schema v3.2.

---

# 🎯 Responsibilities
- intent detection  
- task classification  
- deterministic routing  
- PACK_SUGGEST routing  
- SCENE / DETECT / OCR / HOMEWORK routing  
- fallback handling  
- ambiguity resolution  
- module priority scoring v3.2  
- event normalization (EV3.2)  
- metadata v3.2 generation  
- safety‑aware routing  
- hybrid‑safe routing rules  
- restricted/sandbox enforcement  
- compatibility with VisionEngineV3  

---

# 📝 Input Types (v3.2)
- text  
- voice (transcribed)  
- OCR (VisionEngineV3 output)  
- dict‑based fallback events  
- hybrid inputs (text + OCR combined)  
- low‑trust inputs (quarantine pipeline)  
- PACK_SUGGEST prefix queries  
- SCENE / DETECT / OCR / HOMEWORK events  

---

# 📤 Output (v3.2)
- task category  
- target module  
- routing metadata v3.2  
- confidence score  
- safety flags  
- fallback reason  
- event version tag (EV3.2)  
- trust level  
- restricted/sandbox flags  
- unified result schema v3.2  

---

# 🏷 Version
**GAMA NL Router — v3.2.0**  
(fully aligned with Runtime 3.2.0, VisionEngineV3, and Unified Event Architecture 3.2.x)

---

# 🔄 NL Router Flow (v3.2.0)

1. Receive normalized input from the Runtime.  
2. Detect input type:  
   - text  
   - voice transcript  
   - OCR (VisionEngineV3 output)  
   - dict fallback  
   - hybrid input  
   - PACK_SUGGEST prefix  
   - SCENE / DETECT / OCR / HOMEWORK  
3. Perform intent classification.  
4. Apply safety‑intent detection.  
5. Match intent to deterministic routing rules.  
6. Determine task category:  
   - vision (SCENE / DETECT / OCR / HOMEWORK)  
   - knowledge pack  
   - PACK_SUGGEST  
   - schoolwork  
   - security  
   - general assistant  
   - diagnostics  
   - system/meta commands  
7. Generate metadata v3.2.  
8. Apply restricted/sandbox rules if required.  
9. Produce unified result schema v3.2.  
10. Return routing result to the Runtime Dispatcher.  
11. Log routing event for diagnostics.  

---

# 🧩 NL Router Components (v3.2)

## 1. Input Normalizer (v3.2)
Prepares incoming text, voice transcripts, OCR output, and hybrid inputs.

- cleanup  
- punctuation correction  
- language detection  
- tokenization  
- hybrid input merging  
- dict → text normalization  
- low‑trust input tagging  
- PACK_SUGGEST prefix extraction  
- VisionEngineV3 payload normalization  

---

## 2. Intent Classifier (v3.2)
Determines what the user wants.

- rule‑based patterns  
- keyword detection  
- PACK_SUGGEST detection  
- fallback heuristics  
- multi‑intent detection  
- safety‑intent detection  
- hybrid‑safe classification  
- improved ambiguity resolution  
- SCENE / DETECT / OCR / HOMEWORK detection  

---

## 3. Routing Engine (v3.2)
Maps intents to modules using deterministic routing.

- routing table v3.2  
- priority rules  
- fallback routes  
- ambiguity resolution  
- module priority scoring v3.2  
- PACK_SUGGEST routing  
- VisionEngineV3 routing  
- safety‑aware routing  
- EV3.2 event mapping  
- restricted/sandbox enforcement  
- reduced routing collisions  

---

## 4. Metadata Generator (v3.2)
Creates routing metadata for the Runtime.

- task category  
- confidence score  
- required module  
- flags (vision, schoolwork, security, packs)  
- safety flags  
- fallback reason  
- event version tag (EV3.2)  
- trust level  
- restricted/sandbox flags  
- PACK_SUGGEST metadata  
- unified result schema v3.2  
- VisionEngineV3 metadata  

---

## 5. Diagnostics Logger (v3.2)
Tracks routing decisions.

- input type  
- detected intent  
- selected module  
- errors or fallback usage  
- confidence score  
- rule hits  
- PACK_SUGGEST hits  
- ambiguity resolution logs  
- metadata v3.2 trace  
- restricted/sandbox events  
- hybrid‑safe routing logs  
- VisionEngineV3 routing logs  

---

# 🔁 NL Router Execution Cycle (v3.2.0)

1. Receive normalized input from the Runtime.  
2. Detect input type (text, voice, OCR, dict, hybrid, PACK_SUGGEST, vision events).  
3. Run intent classification.  
4. Apply safety‑intent detection.  
5. Match intent to routing rules.  
6. Determine task category and target module.  
7. Generate metadata v3.2.  
8. Apply restricted/sandbox rules.  
9. Produce unified result schema v3.2.  
10. Return routing result to the Runtime Dispatcher.  
11. Log routing event for diagnostics.  
12. Wait for next input.  

---

# 🟪 NEW IN VERSION 3.2.0
- VisionEngineV3 routing  
- SCENE / DETECT / OCR / HOMEWORK support  
- metadata v3.2  
- event versioning EV3.2  
- unified result schema v3.2  
- improved hybrid‑safe routing  
- reduced event collisions  
- improved fallback logic  
- diagnostics expansion v3.2  
- module priority scoring v3.2  
- runtime_info routing improvements  

---

# ✔ GAMA NL Router 3.2 — COMPLETE  
Fully aligned with the SIRIUS LOCAL AI GAMA 3.2.x ecosystem.
