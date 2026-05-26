# 📁 SIRIUS LOCAL AI GAMA – Folder Structure  
Version: **3.2.0**

This is the official folder structure for **SIRIUS LOCAL AI GAMA 3.2.0**, fully aligned with the 3.2.x architecture, unified event system, hybrid‑safe rules, VisionEngineV3, Event Engine 3.2, and Runtime Core 3.2.

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
The main mobile runtime for GAMA 3.2.  
Contains all core orchestrators and 3.2.x architecture components:

- runtime_core.py  
- system_loader.py  
- system_manager.py  
- system_api.py  
- hybrid_router_3_2.py  
- event_router_entry.py  
- event_compatibility.py  
- event_versioning_3.py  
- event_diagnostics_v3.py  
- runtime_context_manager.py  
- event_metadata_engine_v3_2.py  
- hybrid_input_normalizer.py  
- safety_execution_layer.py  
- module_priority_resolver_v3_2.py  
- fallback_normalizer.py  
- runtime_info_handler.py  

---

# 🟪 /modules  
All functional modules for GAMA 3.2 (rewritten or upgraded):

- **vision_engine_v3**  
- **object_detection_mobile_v3**  
- **scene_understanding_mobile_v3**  
- **ocr_mobile_v3**  
- **homework_vision_v3**  
- **vision_fallback_mobile_v3**  
- **schoolwork_mode_mobile_v3_2**  
- **math_solver_mobile_v3_2**  
- **step_by_step_engine_v3_2**  
- **schoolwork_detector_v3_2**  
- **knowledge_pack_integrator_v3_2**  
- **health_assistant_mobile_v3_2**  
- **diagnostics_mobile_v3_2**  
- **security_family_mobile_v3_2**  
- **workflow_engine_mobile_3_2**  
- **pack_integrity_checker_v3_2**  
- **low_trust_classifier_v3_2**  
- **hybrid_safe_gatekeeper_v3_2**  
- **result_schema_normalizer_v3_2**  

---

# 🟩 /ui  
Mobile UI components for GAMA 3.2:

- screens/  
- components/  
- dialogs/  
- animations/  
- hybrid_input_ui/  
- camera_ui/  
- diagnostics_ui/  
- safety_ui/  
- runtime_info_ui/  

---

# 🟧 /vision  
All Vision Engine V3 modules:

- ocr_mobile_v3/  
- object_detection_mobile_v3/  
- scene_understanding_mobile_v3/  
- homework_vision_v3/  
- preprocessing_native_v3/  
- vision_fallback_mobile_v3/  
- vision_diagnostics_v3/  
- hybrid_input_merger_v3/  
- image_metadata_engine_v3/  

---

# 🟫 /security  
Security Family 3.2 modules:

- security_family_mobile_v3_2/  
- behavior_monitor_v3_2/  
- safety_rules_engine_v3_2/  
- operation_filter_v3_2/  
- mode_controller_v3_2/  
- quarantine_pipeline_v3_2/  
- envoy_low_trust_handler_v3_2/  
- security_diagnostics_v3_2/  
- restricted_mode_controller_v3_2/  
- hybrid_safe_policy_enforcer_v3_2/  

---

# 🟩 /knowledge_packs  
Knowledge Packs 3.2:

- cooking_pack/  
- repairs_pack/  
- school_pack/  
- household_pack/  
- logic_pack/  
- safety_rules_pack/  
- general_knowledge_pack/  
- metadata_specs_v3_2/  
- pack_integrity_checker_v3_2/  
- pack_priority_engine_v3_2/  
- pack_suggest_engine_v3_2/  

---

# 🟫 /bridge  
LAN Offline Bridge 3.2 + PC connectivity:

- lan_bridge_v3_2/  
- pc_runtime_connector_v3_2/  
- offline_sync_manager_v3_2/  
- mobile_pc_event_bridge_v3_2/  
- diagnostics_bridge_v3_2/  
- hybrid_safe_bridge_layer_v3_2/  

---

# 🩺 /health  
Health Assistant 3.2:

- health_assistant_entry_v3_2/  
- health_ocr_pipeline_v3_2/  
- medication_info_engine_v3_2/  
- first_aid_logic_v3_2/  
- symptom_explanation_engine_v3_2/  
- health_safety_layer_v3_2/  
- health_diagnostics_v3_2/  
- health_metadata_engine_v3_2/  

---

# 🛠 /diagnostics  
Diagnostics 3.2:

- battery_diagnostics_v3_2/  
- thermal_diagnostics_v3_2/  
- storage_diagnostics_v3_2/  
- memory_diagnostics_v3_2/  
- performance_logs_v3_2/  
- event_logs_v3_2/  
- rule_hits_v3_2/  
- example_hits_v3_2/  
- hybrid_safe_logs_v3_2/  
- runtime_info_logs_v3_2/  

---

# 🧠 /context  
Runtime Context 3.2:

- runtime_context_manager_v3_2/  
- event_context_v3_2/  
- metadata_store_v3_2/  
- debug_logs_v3_2/  
- hybrid_safe_context_v3_2/  
- runtime_info_context_v3_2/  

---

# 🔄 /events  
Unified Event Architecture 3.2.x:

- event_router_entry.py  
- hybrid_router_3_2.py  
- event_compatibility.py  
- event_versioning_3.py  
- event_diagnostics_v3.py  
- unified_events_v3_2/  
- PACK_QUERY/  
- PACK_INFO/  
- PACK_SUGGEST/  
- SCENE_EVENT/  
- DETECT_EVENT/  
- OCR_EVENT/  
- HOMEWORK_EVENT/  
- SCHOOLWORK_EVENT/  
- SECURITY_EVENT/  
- DIAGNOSTICS_EVENT/  
- HYBRID_SAFE_EVENT/  
- RUNTIME_INFO_EVENT/  

---

# 📚 /docs  
All documentation for version 3.2.0:

- README.md  
- SECURITY.md  
- ARCHITECTURE_3.2.md  
- WORKFLOW_3.2.md  
- MODULE_MAP_3.2.md  
- KNOWLEDGE_PACKS_3.2.md  
- HEALTH_ASSISTANT_3.2.md  
- VISION_ENGINE_V3.md  
- RUNTIME_CORE_3.2.md  
- ROADMAP_3.x.md  
- HYBRID_SAFE_POLICY_3.2.md  

---

# 🏗 /build  
Build system for mobile platforms:

- android/  
- ios/  
- packaging/  
- versioning/  
- release/  
- hybrid_safe_build/  
- diagnostics_build/  
