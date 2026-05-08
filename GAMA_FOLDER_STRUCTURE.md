# 📁 SIRIUS LOCAL AI GAMA – Folder Structure  
Version: **2.0.0**

Toto je oficiálna priečinková štruktúra pre **SIRIUS LOCAL AI GAMA 2.0.0**, rozšírená o všetky nové moduly, ktoré vznikli v rámci verzie 2.0 a príprav na 3.0.0‑pre.

---

```
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
```

---

# 🟦 /runtime_mobile  
Hlavný mobilný runtime pre GAMA 2.0.  
Obsahuje:

- runtime_core.py  
- task_dispatcher.py  
- intent_router_link.py  
- module_manager.py  
- runtime_context_manager.py  
- event_metadata_engine.py  
- hybrid_input_normalizer.py  
- safety_execution_layer.py  

---

# 🟪 /modules  
Všetky funkčné moduly GAMA 2.0:

- **vision_engine_mobile**  
- **object_detection_mobile**  
- **scene_understanding_mobile**  
- **vision_fallback_mobile**  
- **schoolwork_mode_mobile**  
- **math_solver_mobile**  
- **step_by_step_engine**  
- **schoolwork_detector**  
- **knowledge_pack_integrator**  
- **health_assistant_mobile**  
- **diagnostics_mobile**  
- **security_family_mobile**  
- **workflow_engine_mobile_2**  
- **module_priority_resolver**  
- **pack_integrity_checker**  

---

# 🟩 /ui  
Mobilné UI komponenty:

- screens/  
- components/  
- dialogs/  
- animations/  
- hybrid_input_ui/  
- camera_ui/  

---

# 🟧 /vision  
Všetky Vision moduly:

- ocr_mobile/  
- object_detection_mobile/  
- scene_understanding_mobile/  
- analyze_mobile/  
- preprocessing_native/  
- vision_fallback_mobile/  
- vision_diagnostics/  

---

# 🟫 /security  
Bezpečnostné moduly:

- security_family_mobile/  
- behavior_monitor/  
- safety_rules_engine/  
- operation_filter/  
- mode_controller/  
- quarantine_pipeline/  
- envoy_low_trust_handler/  
- security_diagnostics/  

---

# 🟩 /knowledge_packs  
Všetky Knowledge Packy:

- cooking_pack/  
- repairs_pack/  
- school_pack/  
- household_pack/  
- logic_pack/  
- safety_rules_pack/  
- general_knowledge_pack/  
- metadata_specs/  
- pack_integrity_checker/  

---

# 🟫 /bridge  
LAN Offline Bridge + PC konektivita:

- lan_bridge/  
- pc_runtime_connector/  
- offline_sync_manager/  
- mobile_pc_event_bridge/  

---

# 🩺 /health  
Health Assistant 2.0:

- health_assistant_entry/  
- health_ocr_pipeline/  
- medication_info_engine/  
- first_aid_logic/  
- symptom_explanation_engine/  
- health_safety_layer/  
- health_diagnostics/  

---

# 🛠 /diagnostics  
Diagnostické moduly:

- battery_diagnostics/  
- thermal_diagnostics/  
- storage_diagnostics/  
- memory_diagnostics/  
- performance_logs/  
- event_logs/  
- rule_hits/  
- example_hits/  

---

# 🧠 /context  
Runtime Context v2:

- runtime_context_manager/  
- event_context/  
- metadata_store/  
- debug_logs/  

---

# 🔄 /events  
Event Architecture:

- event_dispatcher_mobile/  
- event_metadata_engine/  
- unified_events/  
- PACK_QUERY/  
- PACK_INFO/  
- VISION_ANALYZE/  
- VISION_SCENE/  
- SCHOOLWORK_EVENT/  
- SECURITY_EVENT/  

---

# 📚 /docs  
Všetka dokumentácia pre verziu 2.0.0:

- README.md  
- SECURITY.md  
- ARCHITECTURE.md  
- WORKFLOW.md  
- MODULE_MAP.md  
- KNOWLEDGE_PACKS.md  
- HEALTH_ASSISTANT.md  
- VISION_ENGINE.md  
- RUNTIME_CORE.md  
- ROADMAP.md  

---

# 🏗 /build  
Build systém pre mobilné platformy:

- android/  
- ios/  
- packaging/  
- versioning/  
- release/  

