# 📁 SIRIUS LOCAL AI GAMA – Folder Structure  
Version: **3.0.0**

This is the official folder structure for **SIRIUS LOCAL AI GAMA 3.0.0**, fully aligned with the new 3.x architecture, unified event system, hybrid‑safe rules, and Runtime Core 3.0.

---
/runtime_mobile
/modules
/ui
/vision
/security
/knowledge_packs
/bridge
/health
/diagnostics
/context
/events
/docs
/build

---

# 🟦 /runtime_mobile  
The main mobile runtime for GAMA 3.0.  
Contains all core orchestrators and 3.x architecture components:

- runtime_core.py  
- event_dispatcher_mobile.py  
- module_manager.py  
- runtime_context_manager.py  
- event_metadata_engine_v3.py  
- hybrid_input_normalizer.py  
- safety_execution_layer.py  
- module_priority_resolver_v3.py  
- fallback_normalizer.py  
- unified_event_router.py  

---

# 🟪 /modules  
All functional modules for GAMA 3.0 (rewritten or upgraded):

- **vision_engine_mobile_v3**  
- **object_detection_mobile_v3**  
- **scene_understanding_mobile_v3**  
- **analyze_mobile_v3**  
- **vision_fallback_mobile_v3**  
- **schoolwork_mode_mobile_v3**  
- **math_solver_mobile_v3**  
- **step_by_step_engine_v3**  
- **schoolwork_detector_v3**  
- **knowledge_pack_integrator_v3**  
- **health_assistant_mobile_v3**  
- **diagnostics_mobile_v3**  
- **security_family_mobile_v3**  
- **workflow_engine_mobile_3**  
- **pack_integrity_checker_v3**  
- **low_trust_classifier_v3**  
- **hybrid_safe_gatekeeper**  

---

# 🟩 /ui  
Mobile UI components for GAMA 3.x:

- screens/  
- components/  
- dialogs/  
- animations/  
- hybrid_input_ui/  
- camera_ui/  
- diagnostics_ui/  
- safety_ui/  

---

# 🟧 /vision  
All Vision Engine 3.0 modules:

- ocr_mobile_v3/  
- object_detection_mobile_v3/  
- scene_understanding_mobile_v3/  
- analyze_mobile_v3/  
- preprocessing_native_v3/  
- vision_fallback_mobile_v3/  
- vision_diagnostics_v3/  
- hybrid_input_merger/  

---

# 🟫 /security  
Security Family 3.0 modules:

- security_family_mobile_v3/  
- behavior_monitor_v3/  
- safety_rules_engine_v3/  
- operation_filter_v3/  
- mode_controller_v3/  
- quarantine_pipeline_v3/  
- envoy_low_trust_handler_v3/  
- security_diagnostics_v3/  
- restricted_mode_controller/  

---

# 🟩 /knowledge_packs  
Knowledge Packs 3.0:

- cooking_pack/  
- repairs_pack/  
- school_pack/  
- household_pack/  
- logic_pack/  
- safety_rules_pack/  
- general_knowledge_pack/  
- metadata_specs_v3/  
- pack_integrity_checker_v3/  
- pack_priority_engine_v3/  

---

# 🟫 /bridge  
LAN Offline Bridge 3.0 + PC connectivity:

- lan_bridge_v3/  
- pc_runtime_connector_v3/  
- offline_sync_manager_v3/  
- mobile_pc_event_bridge_v3/  
- diagnostics_bridge/  

---

# 🩺 /health  
Health Assistant 3.0:

- health_assistant_entry_v3/  
- health_ocr_pipeline_v3/  
- medication_info_engine_v3/  
- first_aid_logic_v3/  
- symptom_explanation_engine_v3/  
- health_safety_layer_v3/  
- health_diagnostics_v3/  

---

# 🛠 /diagnostics  
Diagnostics 3.0:

- battery_diagnostics_v3/  
- thermal_diagnostics_v3/  
- storage_diagnostics_v3/  
- memory_diagnostics_v3/  
- performance_logs_v3/  
- event_logs_v3/  
- rule_hits_v3/  
- example_hits_v3/  
- hybrid_safe_logs/  

---

# 🧠 /context  
Runtime Context 3.0:

- runtime_context_manager_v3/  
- event_context_v3/  
- metadata_store_v3/  
- debug_logs_v3/  
- hybrid_safe_context/  

---

# 🔄 /events  
Unified Event Architecture 3.x:

- event_dispatcher_mobile_v3/  
- event_metadata_engine_v3/  
- unified_events_v3/  
- PACK_QUERY/  
- PACK_INFO/  
- VISION_ANALYZE/  
- VISION_SCENE/  
- SCHOOLWORK_EVENT/  
- SECURITY_EVENT/  
- DIAGNOSTICS_EVENT/  
- HYBRID_SAFE_EVENT/  

---

# 📚 /docs  
All documentation for version 3.0.0:

- README.md  
- SECURITY.md  
- ARCHITECTURE_3.0.md  
- WORKFLOW_3.0.md  
- MODULE_MAP_3.0.md  
- KNOWLEDGE_PACKS_3.0.md  
- HEALTH_ASSISTANT_3.0.md  
- VISION_ENGINE_3.0.md  
- RUNTIME_CORE_3.0.md  
- ROADMAP_3.x.md  

---

# 🏗 /build  
Build system for mobile platforms:

- android/  
- ios/  
- packaging/  
- versioning/  
- release/  
- hybrid_safe_build/  
