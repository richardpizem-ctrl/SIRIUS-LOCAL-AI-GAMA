# ⚙️ GAMA Runtime Core

The GAMA Runtime Core is the central execution layer responsible for:
- handling user intents  
- routing tasks to modules  
- managing offline capabilities  
- coordinating knowledge packs  
- executing mobile workflows  
- providing a unified interface for all GAMA features  
- enforcing deterministic behavior (NEW)  
- managing event lifecycle (NEW)  
- supporting Runtime 3.x metadata (NEW)  

---

# 🎯 Responsibilities
- Intent processing  
- Task dispatching  
- Module orchestration  
- Local data access  
- Security enforcement  
- Error handling and recovery  
- Diagnostics + event logging (NEW)  
- Hybrid input normalization (NEW)  
- Safety‑aware execution (NEW)  

---

# 🧩 Components
- Intent Router  
- Task Dispatcher  
- Module Manager  
- Local Storage Layer  
- Security Layer  
- Logging & Diagnostics  
- Runtime Context Manager (NEW)  
- Event Metadata Engine (NEW)  
- Module Priority Resolver (NEW)  

---

# 🏷 Version
**GAMA Runtime Core — v1.0.0**  
(fully prepared for Runtime 3.0.0‑pre)

---

# 🔄 Runtime Flow

1. User input is received (text, voice, image).  
2. Input is normalized and sent to the Intent Router.  
3. Intent Router identifies the task category:  
   - vision  
   - knowledge pack  
   - schoolwork  
   - security  
   - general assistant  
   - diagnostics (NEW)  
   - system/meta commands (NEW)  
4. Task Dispatcher selects the correct module.  
5. Module Manager loads the required module.  
6. Module executes the task locally (offline‑first).  
7. Runtime collects the output.  
8. Security Layer validates the output.  
9. Runtime formats the final response.  
10. Response is returned to the user.  
11. Diagnostics log the event.  
12. Runtime waits for next input.  

---

# 🧱 Runtime Components Detail

## 1. Intent Router
Responsible for analyzing user input and determining the correct task category.
- text normalization  
- language detection  
- intent classification  
- routing rules  
- multi‑intent detection (NEW)  
- safety‑intent detection (NEW)  
- hybrid input support (NEW)  

## 2. Task Dispatcher
Receives the intent and selects the correct module.
- module selection logic  
- priority handling  
- fallback routing  
- module priority scoring (NEW)  
- event version mapping (NEW)  

## 3. Module Manager
Loads and executes modules required for the task.
- module registry  
- lifecycle management  
- dependency handling  
- module compatibility checks (NEW)  
- module tracking (NEW)  

## 4. Local Storage Layer
Handles all offline data.
- knowledge packs  
- cached results  
- user preferences  
- secure storage  
- pack integrity validation (NEW)  
- pack auto‑load support (NEW)  

## 5. Security Layer
Ensures safe execution and output validation.
- OWNER/FAMILY mode rules  
- output filtering  
- permission checks  
- safety flags (NEW)  
- restricted‑mode enforcement (NEW)  

## 6. Logging & Diagnostics
Tracks runtime behavior for debugging and stability.
- event logs  
- error reports  
- performance metrics  
- rule hits (NEW)  
- example hits (NEW)  
- pack usage logs (NEW)  

## 7. Runtime Context Manager (NEW)
Maintains runtime state.
- metadata  
- debug logs  
- reset()  
- event context  

## 8. Event Metadata Engine (NEW)
Adds structured metadata to every event.
- event version  
- module target  
- confidence score  
- safety flags  

---

# 🔁 Runtime Execution Cycle

1. Initialize runtime core.  
2. Load essential modules and security rules.  
3. Wait for user input (text, voice, image).  
4. Normalize input and send it to the Intent Router.  
5. Intent Router determines the task category.  
6. Task Dispatcher selects the appropriate module.  
7. Module Manager loads and executes the module.  
8. Module performs the task using local data and knowledge packs.  
9. Output is validated by the Security Layer.  
10. Runtime formats the final response.  
11. Response is returned to the user.  
12. Runtime logs the event and waits for the next input.  

---

# 🟪 NEW IN VERSION 2 → PREPARED FOR VERSION 3.0.0‑pre
- hybrid input support  
- multi‑intent routing  
- safety‑aware execution  
- module priority scoring  
- event metadata engine  
- runtime context v3  
- pack integrity validation  
- diagnostics expansion  
- unified event architecture  
- dict → event fallback normalization  
