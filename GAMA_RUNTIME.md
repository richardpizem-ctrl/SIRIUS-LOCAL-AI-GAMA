# ⚙️ GAMA Runtime Core — Version 3.2.0

The GAMA Runtime Core is the **central execution layer** of the SIRIUS LOCAL AI GAMA 3.x ecosystem.  
It provides deterministic task execution, unified event routing, hybrid‑safe processing, PACK_SUGGEST support, VisionEngineV3 routing, and full offline autonomy.

Version **3.2.0** introduces the **Unified Result Schema v3.2**, Hybrid Router 3.2,  
**Event Engine 3.2**, improved fallback logic, safer reset(), extended debug metadata,  
and stability improvements across the entire runtime pipeline.

---

# 🎯 Responsibilities
- Intent processing  
- Deterministic task dispatching  
- Module orchestration  
- Local data access  
- Security enforcement (restricted + sandbox)  
- Error handling + fallback  
- Diagnostics + event logging  
- Hybrid input normalization  
- Metadata v3.2 propagation  
- Unified event lifecycle management  
- PACK_SUGGEST routing support  
- VisionEngineV3 routing  
- Unified result schema v3.2 generation  

---

# 🧩 Components (v3.2)
- NL Router v3.2  
- Hybrid Router 3.2  
- Task Dispatcher v3.2  
- Module Manager v3.2  
- Local Storage Layer  
- Security Layer v3.2  
- Logging & Diagnostics v3.2  
- Runtime Context Manager v3.2  
- Event Metadata Engine v3.2  
- Module Priority Resolver v3.2  
- Fallback Normalizer v3.2  
- Hybrid‑Safe Gatekeeper v3.2  
- Unified Result Schema Engine v3.2  
- Runtime Info Handler v3.2  
- Event Compatibility Layer v3.2  
- Event Versioning Engine v3.2  

---

# 🏷 Version
**GAMA Runtime Core — v3.2.0**  
(fully aligned with Unified Event Architecture 3.2.x and VisionEngineV3)

---

# 🛡️ BEHAVIORAL SAFETY POLICY (v3.2) — UPDATED

The Runtime Core enforces global behavioral safety rules across all modules.  
This ensures deterministic, safe, family‑friendly execution for all inputs.

## 🔐 1. Deterministic Runtime Behavior
- no hallucinations  
- no unverified claims  
- if uncertain → respond “I don’t know”  
- deterministic routing + reasoning  
- unified fallback logic v3.2  
- unified result schema v3.2  

## 👨‍👩‍👧 2. Family‑Safe Execution
- child‑safe filtering  
- blocking sensitive topics  
- safe offline explanations  
- restricted reasoning for minors  

## 🔍 3. Local Ethical Filters
- all filtering is fully offline  
- no cloud APIs  
- no external requests  
- no telemetry  
- no remote logging  

## 🧱 4. Runtime Sandbox (v3.2)
- module isolation  
- event‑level sandboxing  
- no dynamic operations  
- no cross‑module privilege escalation  
- hybrid inputs treated as **low‑trust**  
- restricted/sandbox enforcement  
- hybrid‑safe sandbox rules  

## 🚫 5. Behavioral Limits
Runtime Core will **never**:
- generate harmful content  
- provide medical/legal/dangerous advice  
- perform identity inference  
- make autonomous decisions  
- manipulate or persuade users  

## 📜 6. Auditability
- event logs  
- safety flags  
- fallback traces  
- metadata v3.2 trace  
- deterministic replay of events  
- PACK_SUGGEST trace  
- hybrid‑safe logs  
- VisionEngineV3 routing logs  

---

# 🔄 Runtime Flow (v3.2.0)

1. User input is received (text, voice, image, hybrid).  
2. Input is normalized and sent to the NL Router v3.2.  
3. NL Router identifies the task category using deterministic routing.  
4. Hybrid Router 3.2 handles SCENE / DETECT / OCR / HOMEWORK events.  
5. Task Dispatcher selects the correct module.  
6. Module Manager loads the required module.  
7. Module executes the task locally (offline‑first).  
8. Security Layer validates the output (restricted + sandbox).  
9. Runtime formats the final response using **Unified Result Schema v3.2**.  
10. Response is returned to the user.  
11. Diagnostics log the event.  
12. Runtime waits for next input.  

---

# 🧱 Runtime Components Detail (v3.2)

## 1. NL Router v3.2
Analyzes user input and determines the correct task category.
- hybrid‑safe normalization  
- language detection  
- intent classification  
- PACK_SUGGEST detection  
- deterministic routing rules  
- multi‑intent detection  
- safety‑intent detection  
- EV3.2 event mapping  
- SCENE / DETECT / OCR / HOMEWORK detection  

## 2. Hybrid Router 3.2
Routes all vision‑related events.
- SCENE routing  
- DETECT routing  
- OCR routing  
- HOMEWORK routing  
- hybrid‑safe enforcement  
- deterministic routing tables  
- metadata v3.2 propagation  

## 3. Task Dispatcher v3.2
Selects the correct module for execution.
- deterministic module selection  
- priority scoring v3.2  
- fallback routing  
- restricted/sandbox enforcement  
- event version mapping  
- PACK_SUGGEST routing  

## 4. Module Manager v3.2
Loads and executes modules.
- module registry  
- lifecycle management  
- dependency handling  
- module compatibility checks  
- module tracking  
- sandbox isolation  

## 5. Local Storage Layer
Handles all offline data.
- knowledge packs  
- cached results  
- user preferences  
- secure storage  
- pack integrity validation v3.2  
- pack auto‑load support  

## 6. Security Layer v3.2
Ensures safe execution and output validation.
- OWNER/FAMILY/STRANGER rules  
- output filtering  
- permission checks  
- safety flags  
- restricted‑mode enforcement  
- sandbox enforcement  
- hybrid‑safe enforcement  

## 7. Logging & Diagnostics v3.2
Tracks runtime behavior.
- event logs  
- error reports  
- performance metrics  
- rule hits  
- example hits  
- pack usage logs  
- hybrid‑safe logs  
- PACK_SUGGEST logs  
- metadata trace v3.2  
- VisionEngineV3 routing logs  

## 8. Runtime Context Manager v3.2
Maintains runtime state.
- metadata v3.2  
- debug logs  
- reset()  
- event context  
- hybrid‑safe context isolation  
- runtime_info context  

## 9. Event Metadata Engine v3.2
Adds structured metadata to every event.
- event version (EV3.2)  
- module target  
- confidence score  
- safety flags  
- trust level  
- restricted/sandbox flags  
- PACK_SUGGEST metadata  
- VisionEngineV3 metadata  

## 10. Fallback Normalizer v3.2
Ensures deterministic fallback behavior.
- dict → event normalization  
- hybrid input fallback  
- security fallback  
- routing fallback  
- integrity fallback  
- unified fallback schema v3.2  

## 11. Unified Result Schema Engine v3.2
Produces consistent, deterministic output format.
- normalized fields  
- safety flags  
- metadata v3.2  
- fallback indicators  
- PACK_SUGGEST indicators  
- hybrid‑safe flags  
- VisionEngineV3 flags  

---

# 🔁 Runtime Execution Cycle (v3.2.0)

1. Initialize runtime core.  
2. Load essential modules and security rules.  
3. Wait for user input (text, voice, image, hybrid).  
4. Normalize input and send it to NL Router v3.2.  
5. NL Router determines the task category.  
6. Hybrid Router 3.2 handles vision events.  
7. Task Dispatcher selects the appropriate module.  
8. Module Manager loads and executes the module.  
9. Output is validated by the Security Layer.  
10. Runtime formats the final response using **Unified Result Schema v3.2**.  
11. Response is returned to the user.  
12. Runtime logs the event and waits for the next input.  

---

# 🟪 NEW IN VERSION 3.2.0
- unified result schema v3.2  
- metadata v3.2  
- event versioning EV3.2  
- Hybrid Router 3.2  
- VisionEngineV3 routing  
- SCENE / DETECT / OCR / HOMEWORK support  
- improved hybrid‑safe routing  
- reduced event collisions  
- improved fallback logic  
- diagnostics expansion v3.2  
- module priority scoring v3.2  
- runtime_info v3.2  
- extended debug metadata  

---

# ✔ GAMA Runtime Core 3.2 — COMPLETE  
Fully aligned with the SIRIUS LOCAL AI GAMA 3.2.x ecosystem.
