# 🤝 Contributing to SIRIUS LOCAL AI GAMA — Version 3.1.0

Thank you for your interest in contributing to **SIRIUS LOCAL AI GAMA**, the fully offline, hybrid‑safe mobile AI runtime of the SIRIUS ecosystem.

GAMA follows the core SIRIUS principles:

- 100% offline  
- deterministic  
- family‑safe  
- privacy‑first  
- modular and extensible  
- no cloud, no telemetry  
- ARM‑optimized  
- safety‑aware  
- hybrid‑safe (3.x / 3.1.x)  
- SUL‑compliant  

This document explains how to contribute safely and effectively to **GAMA 3.1.0**.

---

# 🧩 1. Project Philosophy

All contributions must respect the core SIRIUS principles:

- **Offline‑first** — no cloud APIs, no remote servers  
- **Deterministic behavior** — no randomness affecting output  
- **Safety** — must comply with SECURITY FAMILY rules  
- **Modularity** — each feature must be isolated and replaceable  
- **Transparency** — clear documentation and predictable behavior  
- **Performance** — optimized for ARM mobile devices  
- **Explainability** — no opaque logic, no hidden behavior  
- **Hybrid‑safe** — strict separation of offline and online data  
- **SUL Compliance** — respect for SIRIUS Unified License 3.x  
- **Event Lifecycle 3.1** — all modules must follow unified event schema  

---

# 📁 2. Repository Structure (Updated for 3.1.0)

```
/runtime_mobile        – core runtime, dispatcher, context manager (3.1)
/modules               – functional modules (vision, schoolwork, health…)
/vision                – Vision Engine 3.1 (OCR, scene, detection)
/security              – Security Family 3.1
/knowledge_packs       – offline structured knowledge packs (v3.1)
/bridge                – LAN Offline Bridge 3.1
/health                – Health Assistant 3.1
/diagnostics           – diagnostics modules (battery, thermal, storage…)
/context               – runtime context + metadata v3.1
/events                – unified event architecture 3.1.x
/ui                    – mobile UI components
/docs                  – documentation
/build                 – Android/iOS build configs
```

---

# 🛠 3. How to Contribute

## ✔️ Step 1: Open an Issue  
Before writing code, open an issue describing:

- what you want to add or fix  
- why it is needed  
- how it fits into GAMA 3.1 architecture  
- which module(s) it affects  
- expected behavior and safety considerations  
- hybrid‑safe implications  
- event metadata impact (3.1.x)  

This ensures alignment with the roadmap and architecture.

---

## ✔️ Step 2: Fork the Repository  
Create your own fork and work in a feature branch:

```
feature/<module-name>
fix/<bug-name>
improvement/<area>
module/<new-module>
```

---

## ✔️ Step 3: Follow Coding Standards  
All contributions must:

- be fully offline unless explicitly hybrid‑safe  
- avoid external dependencies  
- avoid cloud libraries  
- avoid telemetry  
- follow modular structure  
- include documentation  
- include tests (if applicable)  
- follow deterministic logic  
- comply with SECURITY FAMILY rules  
- comply with hybrid‑safe rules (3.1.x)  
- include event metadata (3.1 standard)  
- respect SUL 3.x licensing boundaries  
- follow unified result schema v3.1  

---

## ✔️ Step 4: Submit a Pull Request  
A PR must include:

- clear description  
- reference to the issue  
- explanation of architecture impact  
- test results (if applicable)  
- documentation updates  
- safety considerations  
- hybrid‑safe considerations  
- performance notes (if relevant)  

Maintainers will review the PR for:

- safety  
- determinism  
- offline and hybrid‑safe compliance  
- architecture compatibility  
- performance impact  
- module isolation  
- event metadata correctness  
- SUL 3.x compliance  

---

# 🔐 4. SECURITY FAMILY Requirements (Mandatory)

All contributions must respect:

- OWNER / FAMILY / STRANGER identity levels  
- restricted mode for unknown users  
- child‑safe behavior  
- no unsafe or harmful outputs  
- no bypassing of safety layers  
- no remote code execution  
- no dynamic imports  
- no privileged module escalation  
- low‑trust data handling rules  
- hybrid‑safe quarantine rules (3.1.x)  

Any PR violating these rules will be rejected.

---

# 📦 5. Knowledge Packs Contributions (v3.1)

Knowledge Packs must be:

- fully offline  
- curated  
- deterministic  
- safe for all ages  
- optimized for mobile storage  
- modular and replaceable  
- validated using pack integrity checker v3.1  
- include metadata.json with priority + compatibility flags  
- follow PACK_QUERY / PACK_INFO / PACK_LOOKUP / PACK_SUGGEST standards  

---

# 🧠 6. Reasoning Engine Contributions

Reasoning modules must:

- be symbolic or rule‑based  
- avoid LLMs or cloud models  
- be transparent and explainable  
- be deterministic  
- be optimized for ARM  
- support rule chaining (3.1.x)  
- support example‑based fallback reasoning  
- respect hybrid‑safe boundaries  
- follow unified event lifecycle v3.1  

---

# 🧪 7. Testing Requirements

Before submitting a PR:

- test on Android (required)  
- test on iOS (recommended)  
- test offline mode  
- test restricted mode  
- test hybrid‑safe behavior (if applicable)  
- test performance on low‑end devices  
- test event metadata correctness  
- test module isolation  
- test unified result schema v3.1  

---

# 🧱 8. Module Requirements (Updated for 3.1.0)

Every new module must:

- include a clear entry point  
- follow the unified event architecture 3.1.x  
- include diagnostics logging  
- include safety flags  
- include metadata versioning  
- support deterministic execution  
- be isolated (no cross‑module side effects)  
- respect hybrid‑safe quarantine rules  
- avoid direct access to offline core unless permitted  
- follow unified result schema v3.1  

---

# 📜 9. Code of Conduct

All contributors must follow the **SIRIUS LOCAL AI GAMA Code of Conduct (3.1.0)**.  
Respectful, safe, and professional behavior is required.

---

# 📬 10. Contact

For questions or guidance:

- open a GitHub issue  
- or contact the maintainer: **@richardpizem-ctrl**

---

# 🚀 Thank You

Your contributions help build the world’s first **fully offline, hybrid‑safe mobile AI assistant**.  
Together we are creating something unique, safe, and powerful.
