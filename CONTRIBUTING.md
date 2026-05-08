# 🤝 Contributing to SIRIUS LOCAL AI GAMA — Version 2.0.0

Thank you for your interest in contributing to **SIRIUS LOCAL AI GAMA**, the fully offline mobile AI runtime of the SIRIUS ecosystem.

GAMA follows the core SIRIUS principles:

- 100% offline  
- deterministic  
- family‑safe  
- privacy‑first  
- modular and extensible  
- no cloud, no telemetry  
- ARM‑optimized  
- safety‑aware  

This document explains how to contribute safely and effectively to **GAMA 2.0.0**.

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

---

# 📁 2. Repository Structure (Updated for 2.0.0)

```
/runtime_mobile        – core runtime, dispatcher, context manager
/modules               – all functional modules (vision, schoolwork, health…)
/vision                – Vision Engine 2.0 (OCR, scene, detection)
/security              – Security Family 2.0
/knowledge_packs       – offline structured knowledge packs
/bridge                – LAN Offline Bridge (mobile ↔ PC)
/health                – Health Assistant 2.0
/diagnostics           – diagnostics modules (battery, thermal, storage…)
/context               – runtime context + metadata
/events                – unified event architecture
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
- how it fits into GAMA 2.0 architecture  
- which module(s) it affects  
- expected behavior and safety considerations  

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

- be fully offline  
- avoid external dependencies  
- avoid cloud libraries  
- avoid telemetry  
- follow modular structure  
- include documentation  
- include tests (if applicable)  
- follow deterministic logic  
- comply with SECURITY FAMILY rules  
- support hybrid input where relevant  
- include event metadata (2.0 standard)  

---

## ✔️ Step 4: Submit a Pull Request  
A PR must include:

- clear description  
- reference to the issue  
- explanation of architecture impact  
- test results (if applicable)  
- documentation updates  
- safety considerations  
- performance notes (if relevant)  

Maintainers will review the PR for:

- safety  
- determinism  
- offline compliance  
- architecture compatibility  
- performance impact  
- module isolation  
- event metadata correctness  

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

Any PR violating these rules will be rejected.

---

# 📦 5. Knowledge Packs Contributions

Knowledge Packs must be:

- fully offline  
- curated  
- deterministic  
- safe for all ages  
- optimized for mobile storage  
- modular and replaceable  
- validated using pack integrity checker  
- include metadata.json with priority + compatibility flags  

---

# 🧠 6. Reasoning Engine Contributions

Reasoning modules must:

- be symbolic or rule‑based  
- avoid LLMs or cloud models  
- be transparent and explainable  
- be deterministic  
- be optimized for ARM  
- support rule chaining (2.0+)  
- support example‑based fallback reasoning  

---

# 🧪 7. Testing Requirements

Before submitting a PR:

- test on Android (required)  
- test on iOS (recommended)  
- test offline mode  
- test restricted mode  
- test performance on low‑end devices  
- test hybrid input (if applicable)  
- test event metadata correctness  

---

# 🧱 8. Module Requirements (New in 2.0)

Every new module must:

- include a clear entry point  
- follow the unified event architecture  
- include diagnostics logging  
- include safety flags  
- include metadata versioning  
- support deterministic execution  
- be isolated (no cross‑module side effects)  

---

# 📜 9. Code of Conduct

All contributors must follow the **SIRIUS LOCAL AI GAMA Code of Conduct**.  
Respectful, safe, and professional behavior is required.

---

# 📬 10. Contact

For questions or guidance:

- open a GitHub issue  
- or contact the maintainer: **@richardpizem-ctrl**

---

# 🚀 Thank You

Your contributions help build the world’s first **fully offline mobile AI assistant**.  
Together we are creating something unique, safe, and powerful.
