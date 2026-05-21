# 📁 SIRIUS LOCAL AI GAMA – Folder Structure  
Version: **3.1.0**

This is the official folder structure for **SIRIUS LOCAL AI GAMA 3.1.0**, fully aligned with the 3.1.x architecture, unified event system, hybrid‑safe rules, and Runtime Core 3.1.

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
The main mobile runtime for GAMA 3.1.  
Contains all core orchestrators and 3.1.x architecture components:

- runtime_core.py  
- event_dispatcher_mobile.py  
- module_manager.py  
- runtime_context_manager.py  
- event_metadata_engine_v3_1.py  
- hybrid_input_normalizer.py  
- safety_execution_layer.py  
- module_priority_resolver_v3_1.py  
- fallback_normalizer.py  
- unified_event_router_v3_1.py  
- runtime_info_handler.py  

---

# 🟪 /modules  
All functional modules for GAMA 3.1 (rewritten or upgraded):

- **vision_engine_mobile_v3_1**  
- **object_detection_mobile_v3_1**  
- **scene_understanding_mobile_v3_1**  
- **analyze_mobile_v3_1**  
- **vision_fallback_mobile_v3_1**  
- **schoolwork_mode_mobile_v3_1**  
- **math_solver_mobile_v3_1**  
- **step_by_step_engine_v3_1**  
- **schoolwork_detector_v3_1**  
- **knowledge_pack_integrator_v3_1**  
- **health_assistant_mobile_v3_1**  
- **diagnostics_mobile_v3_1**  
- **security_family_mobile_v3_1**  
- **workflow_engine_mobile_3_1**  
- **pack_integrity_checker_v3_1**  
- **low_trust_classifier_v3_1**  
- **hybrid_safe_gatekeeper_v3_1**  
- **result_schema_normalizer_v3_1**  

---

# 🟩 /ui  
Mobile UI components for GAMA 3.1:

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
All Vision Engine 3.1 modules:

- ocr_mobile_v3_1/  
- object_detection_mobile_v3_1/  
- scene_understanding_mobile_v3_1/  
- analyze_mobile_v3_1/  
- preprocessing_native_v3_1/  
- vision_fallback_mobile_v3_1/  
- vision_diagnostics_v3_1/  
- hybrid_input_merger_v3_1/  
- image_metadata_engine_v3_1/  

---

# 🟫 /security  
Security Family 3.1 modules:

- security_family_mobile_v3_1/  
- behavior_monitor_v3_1/  
- safety_rules_engine_v3_1/  
- operation_filter_v3_1/  
- mode_controller_v3_1/  
- quarantine_pipeline_v3_1/  
- envoy_low_trust_handler_v3_1/  
- security_diagnostics_v3_1/  
- restricted_mode_controller_v3_1/  
- hybrid_safe_policy_enforcer_v3_1/  

---

# 🟩 /knowledge_packs  
Knowledge Packs 3.1:

- cooking_pack/  
- repairs_pack/  
- school_pack/  
- household_pack/  
- logic_pack/  
- safety_rules_pack/  
- general_knowledge_pack/  
- metadata_specs_v3_1/  
- pack_integrity_checker_v3_1/  
- pack_priority_engine_v3_1/  
- pack_suggest_engine_v3_1/  

---

# 🟫 /bridge  
LAN Offline Bridge 3.1 + PC connectivity:

- lan_bridge_v3_1/  
- pc_runtime_connector_v3_1/  
- offline_sync_manager_v3_1/  
- mobile_pc_event_bridge_v3_1/  
- diagnostics_bridge_v3_1/  
- hybrid_safe_bridge_layer/  

---

# 🩺 /health  
Health Assistant 3.1:

- health_assistant_entry_v3_1/  
- health_ocr_pipeline_v3_1/  
- medication_info_engine_v3_1/  
- first_aid_logic_v3_1/  
- symptom_explanation_engine_v3_1/  
- health_safety_layer_v3_1/  
- health_diagnostics_v3_1/  
- health_metadata_engine_v3_1/  

---

# 🛠 /diagnostics  
Diagnostics 3.1:

- battery_diagnostics_v3_1/  
- thermal_diagnostics_v3_1/  
- storage_diagnostics_v3_1/  
- memory_diagnostics_v3_1/  
- performance_logs_v3_1/  
- event_logs_v3_1/  
- rule_hits_v3_1/  
- example_hits_v3_1/  
- hybrid_safe_logs_v3_1/  
- runtime_info_logs/  

---

# 🧠 /context  
Runtime Context 3.1:

- runtime_context_manager_v3_1/  
- event_context_v3_1/  
- metadata_store_v3_1/  
- debug_logs_v3_1/  
- hybrid_safe_context_v3_1/  
- runtime_info_context/  

---

# 🔄 /events  
Unified Event Architecture 3.1.x:

- event_dispatcher_mobile_v3_1/  
- event_metadata_engine_v3_1/  
- unified_events_v3_1/  
- PACK_QUERY/  
- PACK_INFO/  
- PACK_SUGGEST/  
- VISION_ANALYZE/  
- VISION_SCENE/  
- SCHOOLWORK_EVENT/  
- SECURITY_EVENT/  
- DIAGNOSTICS_EVENT/  
- HYBRID_SAFE_EVENT/  
- RUNTIME_INFO_EVENT/  

---

# 📚 /docs  
All documentation for version 3.1.0:

- README.md  
- SECURITY.md  
- ARCHITECTURE_3.1.md  
- WORKFLOW_3.1.md  
- MODULE_MAP_3.1.md  
- KNOWLEDGE_PACKS_3.1.md  
- HEALTH_ASSISTANT_3.1.md  
- VISION_ENGINE_3.1.md  
- RUNTIME_CORE_3.1.md  
- ROADMAP_3.x.md  
- HYBRID_SAFE_POLICY_3.1.md  

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
