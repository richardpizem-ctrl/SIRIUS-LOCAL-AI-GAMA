# 🗺️ SIRIUS LOCAL AI GAMA – Module Map  
Version: **2.0.0**

---

## 🟦 Core Modules
- runtime_mobile  
- workflow_mobile  
- nl_router_mobile  
- reasoning_mobile  
- security_mobile  
- diagnostics_mobile  
- context_manager_mobile  
- event_dispatcher_mobile  

---

## 🟪 Vision Modules
- ocr_mobile  
- object_detection_mobile  
- scene_understanding_mobile  
- analyze_mobile (unified ANALYZE event)  
- vision_fallback_mobile (dict → event conversion)  

---

## 🟧 Schoolwork Modules
- math_solver_mobile  
- handwriting_recognition  
- textbook_knowledge  
- step_by_step_engine  
- schoolwork_detector (auto‑detect homework tasks)  

---

## 🟩 Knowledge Packs
- cooking_pack  
- repairs_pack  
- school_pack  
- household_pack  
- logic_pack  
- safety_rules_pack  
- general_knowledge_pack  
- pack_integrity_checker (runtime 3.x compatibility)  

---

## 🟫 Bridge Modules
- lan_bridge  
- pc_runtime_connector  
- offline_sync_manager  
- mobile_pc_event_bridge  

---

## 🟪 Prepared for GAMA 3.0.0‑pre
- unified PACK_QUERY event  
- unified PACK_INFO event  
- rule chaining support  
- example‑based fallback reasoning  
- diagnostics expansion (rule hits, example hits)  
- runtime compatibility flags in metadata.json  
- module priority + module tracking  
- extended event metadata  
- router → dispatcher → core integration  

---

## 🟧 Prepared for GAMA 4.0 (Hybrid‑Safe Architecture)
- secure_online_envoy (sandboxed online agent)  
- quarantine_pipeline (sanitization layer)  
- offline_core_airgap (strict isolation)  
- structured_data_import (clean text + JSON only)  
