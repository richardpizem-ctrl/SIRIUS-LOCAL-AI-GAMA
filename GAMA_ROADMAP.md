# 🚀 SIRIUS LOCAL AI GAMA – Roadmap  
Version: **3.2.0**

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

# 🟦 GAMA 3.x – CURRENT & UPCOMING RELEASES

## 🟩 GAMA 3.1.0
**Stability, metadata, routing, hybrid‑safe improvements**

- Runtime Core 3.1  
- unified result schema v3.1  
- PACK_SUGGEST support  
- improved fallback logic  
- ANALYZE → SCENE alias stabilization  
- metadata v3.1  
- hybrid‑safe routing improvements  
- pack priority v3.1  
- compatibility flags v3.1  
- SECURITY_ALERT stabilization  
- hybrid‑safe enforcement v3.1  

---

## 🟩 GAMA 3.2.0 (CURRENT RELEASE)
**Modern Runtime Pipeline + VisionEngineV3**

### 🔹 Runtime & Core
- Runtime Core 3.2  
- System Layer 3.2  
- Hybrid Router 3.2  
- Event Engine 3.2  
- deterministic routing v3.2  
- unified result schema v3.2  
- improved fallback logic  
- runtime_info v3.2  

### 🔹 VisionEngineV3
- SCENE event  
- DETECT event  
- OCR event  
- HOMEWORK event  
- deterministic preprocessing  
- normalized output schema  
- hybrid‑safe vision flow  

### 🔹 Knowledge Packs 3.2
- metadata v3.2  
- pack priority v3.2  
- compatibility flags v3.2  
- PACK_SUGGEST improvements  
- deterministic pack routing v3.2  

### 🔹 NL Router 3.2
- SCENE / DETECT / OCR / HOMEWORK routing  
- PACK_SUGGEST v3.2  
- metadata v3.2  
- EV3.2 event mapping  
- reduced routing collisions  

### 🔹 Security Family 3.2
- restricted mode v3.2  
- sandbox enforcement v3.2  
- quarantine pipeline v3.2  
- hybrid‑safe enforcement v3.2  

### 🔹 Diagnostics 3.2
- expanded pack usage logs  
- example hits v3.2  
- hybrid‑safe logs v3.2  
- metadata trace v3.2  

---

## 🟩 GAMA 3.3.0
- Quarantine pipeline v3 (full)  
- Sandbox enforcement v3 (full)  
- Restricted mode v3 (full)  
- VisionEngine deterministic flow v3  
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
