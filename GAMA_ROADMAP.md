# 🚀 SIRIUS LOCAL AI GAMA – Roadmap  
Version: **3.1.0**

---

## 🟦 GAMA 1.0 (Initial Release)
- Mobile Runtime Core  
- NL Router Mobile  
- Knowledge Packs Mobile  
- Vision Engine (OCR)  
- Schoolwork Mode Mobile  
- SECURITY FAMILY Mobile  

---

## 🟪 GAMA 1.1 (Enhancements)

### 1) Priority Score for Knowledge Packs
- new field in metadata.json: `"priority": 0.0 – 1.0`  
- specialized packs preferred over general packs  
- deterministic PACK_LOOKUP  
- fallback for equal scores  
- improved accuracy without NLP  

### 2) Native Image Preprocessing (Android/iOS)
**Android (CameraX / ML Kit):**
- auto‑focus  
- auto‑exposure  
- auto‑white balance  
- document detection  
- perspective correction  
- stabilization  

**iOS (VisionKit / AVFoundation):**
- VNDocumentCameraViewController  
- auto‑crop  
- auto‑enhance  
- auto‑deskew  
- noise reduction  

**Result:**
- higher OCR accuracy  
- lower CPU load  
- faster processing  
- cleaner input for Vision Engine  

### 3) Vision Engine Pipeline Improvements
- native preprocessing → Vision Engine → OCR → Reasoning  
- ARM optimization  
- reduced noise and OCR errors  

### 4) Knowledge Pack Spec 2.0
- expanded metadata  
- pack categorization  
- priority routing  
- preparation for Knowledge Graphs (GAMA 3.0)  

---

## 🟩 GAMA 2.0 (STABLE RELEASE)
- LAN Offline Bridge  
- Device Diagnostics Mobile  
- Scene Understanding  
- Workflow Engine Mobile 2.0  
- **Health Assistant 2.0**  
  - offline medical module  
  - OCR of medical documents  
  - medication & dosage recognition  
  - first‑aid & triage logic  
  - family‑safe medical guidance  
  - 100% offline processing  

### 🔹 NEW IN GAMA 2.0
- Diagnostics Expansion (battery, thermal, storage, memory)  
- Runtime Context v2  
- Pack Integrity Checker  
- Rule Chaining (foundation for 3.0)  
- Example‑based fallback reasoning  
- Unified PACK_QUERY + PACK_INFO events  
- Module priority + module tracking  
- Hybrid input support (text + OCR)  
- Safety‑aware routing in NL Router  
- Event Metadata Engine v2  
- Deterministic workflow execution  

---

# 🟧 GAMA 3.0 (MAJOR RE‑ARCHITECTURE)
**Full re‑architecture of the mobile runtime.**

## 🔹 Runtime & Core
- Full Mobile Reasoning Engine  
- Deterministic Runtime Core 3.0  
- Unified Event Architecture (router → dispatcher → core)  
- Multi‑intent routing  
- Hybrid‑safe routing  
- Metadata v3 + Event Versioning v3  
- Runtime Context v3 (debug logs, metadata, reset)  

## 🔹 Vision Engine 3.0
- ANALYZE event  
- SCENE event  
- improved OCR pipeline  
- hybrid reasoning support  
- deterministic vision flow  

## 🔹 Knowledge Packs 3.0
- auto‑load  
- pack integrity v3  
- pack priority v3  
- compatibility flags v3  
- PACK_QUERY / PACK_INFO v3  
- deterministic pack routing  

## 🔹 Diagnostics 3.0
- rule hits  
- example hits  
- pack usage  
- hybrid‑safe logs  
- metadata trace  

## 🔹 Security Family 3.0
- restricted mode v3  
- sandbox enforcement v3  
- quarantine pipeline v3  
- low‑trust classification  
- deterministic safety routing  

## 🔹 Schoolwork Mode 3.0
- deterministic academic reasoning  
- schoolwork_trace  
- hybrid input support  
- OCR schoolwork integration  

## 🔹 Additional 3.0 Features
- dict → event fallback normalization  
- unified SCHOOLWORK + VISION + PACK events  
- deterministic reasoning trace  
- module compatibility flags  
- hybrid reasoning (rules + examples)  

---

# 🟦 GAMA 3.x – UPCOMING RELEASES

## 🟩 GAMA 3.1.0 (CURRENT RELEASE)
**Stability, metadata, routing, hybrid‑safe improvements**

### 🔹 Runtime & Core
- Runtime Core 3.1 (stability pass)  
- unified result schema v3.1  
- improved fallback logic  
- runtime_info event  
- safer reset()  
- extended debug metadata  

### 🔹 NL Router 3.1
- PACK_SUGGEST support  
- improved multi‑intent routing  
- reduced event collisions  
- metadata v3.1  
- hybrid‑safe routing improvements  

### 🔹 Vision Engine 3.1
- ANALYZE → SCENE alias stabilization  
- improved OCR fallback  
- deterministic preprocessing  
- unified error schema v3.1  

### 🔹 Knowledge Packs 3.1
- PACK_SUGGEST prefix search  
- metadata v3.1  
- pack priority v3.1  
- compatibility flags v3.1  
- improved fallback reasoning  

### 🔹 Security Family 3.1
- extended restricted mode  
- improved unsafe‑text filter  
- SECURITY_ALERT stabilization  
- hybrid‑safe enforcement v3.1  

### 🔹 Diagnostics 3.1
- PACK_SUGGEST logs  
- hybrid‑safe logs  
- unified metadata trace v3.1  

---

## 🟩 GAMA 3.2.0
- Hybrid‑safe routing v3  
- Event Versioning v3 (full)  
- Diagnostics v3 (example hits + pack usage)  
- Vision Engine: ANALYZE v2  
- Pack compatibility flags v3  
- Schoolwork Mode: OCR integration v2  

---

## 🟩 GAMA 3.3.0
- Quarantine pipeline v3  
- Sandbox enforcement v3  
- Restricted mode v3  
- Vision Engine deterministic flow v3  
- Pack integrity v3 (full)  
- Schoolwork Mode: deterministic academic reasoning  

---

## 🟩 GAMA 3.4.0
- Trace logs v3 (full)  
- Fallback normalization v3  
- Unified SCHOOLWORK + VISION + PACK events v3  
- Runtime Context v3 (extended debug metadata)  

---

## 🟩 GAMA 3.5.0 (FINAL 3.x RELEASE)
- Architecture cleanup  
- Performance optimization  
- Stability pass  
- Final hybrid reasoning refinements  
- Preparation for GAMA 4.0 migration  

---

# 🟪 GAMA 4.0 (Hybrid‑Safe Architecture)

## Secure Online Envoy (Isolated Online Agent)
- sandboxed online agent  
- outbound‑only internet  
- fetches text, JSON, structured data  
- no access to local files, models, APIs  
- no local data ever sent out  
- acts as a courier, not part of AI  

## Quarantine Pipeline (Data Sanitization Layer)
- script & HTML removal  
- format validation  
- size limits  
- text cleaning  
- security filtering  
- only clean text + JSON allowed  
- offline core never touches untrusted data  

## Offline Core Remains Fully Air‑Gapped
- inference offline  
- reasoning offline  
- knowledge packs offline  
- no cloud calls  
- no telemetry  
- no outbound data  

## Why This Matters
- offline AI stays offline  
- absolute user privacy  
- AI can use up‑to‑date information  
- modular, safe, enterprise‑grade  
- same model as air‑gapped critical systems  

---

## 🟫 Optional: LAN Offline Bridge
Mobile ↔ PC communication over **local Wi‑Fi only**:
- mobile = camera, UI, input  
- PC = heavy reasoning, diagnostics, WIN‑CAP, FS‑AGENT  

No internet required.
