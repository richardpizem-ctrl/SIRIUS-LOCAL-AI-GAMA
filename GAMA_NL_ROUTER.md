# 🧭 GAMA NL Router

The NL Router is responsible for interpreting user input and determining the correct task category.

---

# 🎯 Responsibilities
- intent detection  
- task classification  
- routing logic  
- fallback handling  
- ambiguity resolution  
- module priority resolution (NEW)  
- event normalization for Runtime 3.x (NEW)  
- safety‑aware routing (NEW)  

---

# 📝 Input Types
- text  
- voice (transcribed)  
- OCR (vision engine output)  
- dict‑based events from Vision fallback (NEW)  
- hybrid inputs (text + OCR combined) (NEW)  

---

# 📤 Output
- task category  
- module target  
- routing metadata  
- confidence score (NEW)  
- safety flags (NEW)  
- fallback reason (NEW)  

---

# 🏷 Version
**GAMA NL Router — v1.0.0**  
(fully prepared for Runtime 3.0.0‑pre)

---

# 🔄 NL Router Flow

1. Receive normalized user input from the Runtime.  
2. Detect input type:  
   - text  
   - voice (transcribed)  
   - OCR (vision output)  
   - dict fallback (NEW)  
3. Perform intent classification.  
4. Match intent to routing rules.  
5. Determine task category:  
   - vision  
   - knowledge pack  
   - schoolwork  
   - security  
   - general assistant  
   - diagnostics (NEW)  
   - system/meta commands (NEW)  
6. Generate routing metadata.  
7. Send routing result back to the Runtime Task Dispatcher.  
8. Log routing event for diagnostics.  
9. Apply safety filters if required (NEW).  

---

# 🧩 NL Router Components

## 1. Input Normalizer
Prepares incoming text, voice transcripts, or OCR output.
- cleanup  
- punctuation correction  
- language detection  
- tokenization  
- hybrid input merging (NEW)  
- dict → text normalization (NEW)  

## 2. Intent Classifier
Determines what the user wants.
- rule‑based patterns  
- keyword detection  
- lightweight offline ML model (optional)  
- fallback heuristics  
- multi‑intent detection (NEW)  
- safety‑intent detection (NEW)  

## 3. Routing Engine
Maps intents to modules.
- routing table  
- priority rules  
- fallback routes  
- ambiguity resolution  
- module priority scoring (NEW)  
- safety‑aware routing (NEW)  
- Runtime 3.x event mapping (NEW)  

## 4. Metadata Generator
Creates routing metadata for the Runtime.
- task category  
- confidence score  
- required module  
- flags (vision, schoolwork, security)  
- safety flags (NEW)  
- fallback reason (NEW)  
- event version tag (NEW)  

## 5. Diagnostics Logger
Tracks routing decisions.
- input type  
- detected intent  
- selected module  
- errors or fallback usage  
- confidence score (NEW)  
- rule hits (NEW)  
- ambiguity resolution logs (NEW)  

---

# 🔁 NL Router Execution Cycle

1. Receive normalized input from the Runtime.  
2. Detect input type (text, voice transcript, OCR, dict).  
3. Run intent classification.  
4. Match intent to routing rules.  
5. Determine task category and target module.  
6. Generate routing metadata.  
7. Return routing result to the Runtime Task Dispatcher.  
8. Log routing event for diagnostics.  
9. Apply safety filters if needed.  
10. Wait for next input.  

---

# 🟪 NEW IN VERSION 2 → PREPARED FOR VERSION 3.0.0‑pre
- dict → event fallback normalization  
- multi‑intent detection  
- safety‑aware routing  
- module priority scoring  
- diagnostics expansion  
- unified routing metadata  
- event version tagging  
- hybrid input support  
- Runtime 3.x compatibility layer  
