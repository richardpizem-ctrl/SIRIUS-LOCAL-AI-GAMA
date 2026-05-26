# 🟪 SIRIUS LOCAL AI GAMA — CHANGELOG (ENGLISH EDITION)
Versions: **2.0.0 → 3.0.0 → 3.1.0 → 3.2.0**

---

# 📌 Version 3.2.0 — (Mobile Runtime Upgrade: VisionEngineV3 + Event Engine 3.2)
**Release Date:** 2026‑05‑26  
**Status:** Stable — full runtime, vision, and event engine upgrade  
**Compatibility:** Fully aligned with SIRIUS LOCAL AI 3.2.x ecosystem  
**Documentation:** Public  
**Source Code:** May be private under SUL 3.0.0  

Version 3.2.0 delivers the largest runtime update since 3.0, introducing the new VisionEngineV3, a fully redesigned event pipeline, and a stabilized system layer.  
This release finalizes the modern runtime architecture and prepares the system for the upcoming 4.x multimodal generation.

---

# 🚀 WHAT’S NEW IN VERSION 3.2.0

## 🟦 1. VisionEngineV3 (NEW)
- deterministic vision engine  
- SCENE / DETECT / OCR / HOMEWORK support  
- normalized output schema  
- improved preprocessing  
- faster image handling  
- stable fallback logic  
- prepared for multimodal 4.x  

---

## 🟩 2. Vision Entry 3.2 (REDESIGNED)
- clean bridge between Event Engine and VisionEngineV3  
- unified API: `process_scene`, `process_detect`, `process_ocr`, `process_homework`  
- stable payload normalization  
- improved error handling  

---

## 🟪 3. Event Engine 3.2 (FULL UPGRADE)

### hybrid_router_3_2.py
- new hybrid routing logic  
- accurate TEXT vs VISION detection  
- SCENE / DETECT / OCR / HOMEWORK routing  

### event_compatibility.py
- legacy → modern event conversion  
- normalized vision payloads  
- IMG_* → modern mapping  

### event_versioning_3.py
- normalized event names  
- stable fallback behavior  
- support for all new vision events  

### event_diagnostics_v3.py
- clean diagnostics  
- routing logs  
- vision logs  
- error logs  
- prepared for Self‑Repair Layer 4.4  

### event_router_entry.py
- integrated VisionEntry  
- stable event dispatching  

---

## 🟧 4. System Layer 3.2

### system_loader.py
- loads VisionEngineV3  
- loads EventRouterEntry  

### system_manager.py
- runtime lifecycle  
- health reporting  

### system_api.py
- public API for mobile runtime  
- `run_event`, `get_health`, `restart_runtime`, `get_system_info`  

---

# 🛠 ARCHITECTURE IMPROVEMENTS (3.2.x)
- deterministic hybrid input pipeline  
- unified event → vision → result flow  
- stronger safety sandbox  
- normalized metadata  
- improved fallback logic  
- groundwork for VisionEngine 4.0  
- groundwork for Self‑Repair Layer 4.4  

---

# 🟪 STATUS
GAMA 3.2.0 is a **stable runtime release**, fully aligned with the SIRIUS LOCAL AI 3.2.x ecosystem.

📘 Documentation for version 3.2.0 is public.  
🔒 Source code may be private under SUL 3.0.0.

---

# 📌 Version 3.1.0 — (Stability & Runtime Upgrade Release)
**Release Date:** 2026‑05‑21  
**Status:** Stable — runtime, dispatcher, vision, packs, and security upgraded  
**Compatibility:** Fully aligned with SIRIUS LOCAL AI 3.1.x ecosystem  

Version 3.1.0 focuses on runtime stability, module cleanup, dispatcher improvements,  
and full alignment with the 3.1.x event system.

---

# 🚀 WHAT’S NEW IN VERSION 3.1.0
*(unchanged from original)*

---

# 📌 Version 3.0.0 — (Major Release)
*(unchanged from original)*

---

# 📌 Version 2.0.0 — (Stable Release)
*(unchanged from original)*

