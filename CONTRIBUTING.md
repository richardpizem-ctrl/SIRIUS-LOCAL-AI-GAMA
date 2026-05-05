# 🤝 Contributing to SIRIUS LOCAL AI GAMA

Thank you for your interest in contributing to **SIRIUS LOCAL AI GAMA**, the mobile offline AI runtime of the SIRIUS ecosystem.  
GAMA follows the same principles as the main SIRIUS runtime:

- 100% offline  
- deterministic  
- family‑safe  
- privacy‑first  
- modular and extensible  
- no cloud, no telemetry  

This document explains how to contribute safely and effectively.

---

# 🧩 1. Project Philosophy

All contributions must respect the core SIRIUS principles:

- **Offline‑first** — no cloud APIs, no remote servers  
- **Deterministic behavior** — no randomness that affects output  
- **Safety** — must comply with SECURITY FAMILY rules  
- **Modularity** — each feature must be isolated and replaceable  
- **Transparency** — clear documentation and predictable behavior  
- **Performance** — optimized for ARM mobile devices  

---

# 📁 2. Repository Structure

```
/runtime_mobile        – lightweight mobile runtime core
/modules               – mobile modules (OCR, schoolwork, reasoning, etc.)
/vision                – Mobile Vision Engine components
/security              – SECURITY FAMILY Mobile
/knowledge_packs       – compressed offline knowledge packs
/bridge                – LAN offline communication with PC runtime
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
- how it fits into GAMA architecture  

This ensures alignment with the roadmap.

---

## ✔️ Step 2: Fork the Repository  
Create your own fork and work in a feature branch:

```
feature/<module-name>
fix/<bug-name>
improvement/<area>
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

---

## ✔️ Step 4: Submit a Pull Request  
A PR must include:

- clear description  
- reference to the issue  
- explanation of architecture impact  
- test results (if applicable)  
- documentation updates  

Maintainers will review the PR for:

- safety  
- determinism  
- offline compliance  
- architecture compatibility  
- performance impact  

---

# 🔐 4. SECURITY FAMILY Requirements

All contributions must respect:

- OWNER / FAMILY / STRANGER identity levels  
- restricted mode for unknown users  
- child‑safe behavior  
- no unsafe or harmful outputs  
- no bypassing of safety layers  

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

---

# 🧠 6. Reasoning Engine Contributions

Reasoning modules must:

- be symbolic or rule‑based  
- avoid LLMs or cloud models  
- be transparent and explainable  
- be deterministic  
- be optimized for ARM  

---

# 🧪 7. Testing Requirements

Before submitting a PR:

- test on Android (required)  
- test on iOS (optional but recommended)  
- test offline mode  
- test restricted mode  
- test performance on low‑end devices  

---

# 📜 8. Code of Conduct

All contributors must follow the **SIRIUS LOCAL AI GAMA Code of Conduct**.  
Respectful, safe, and professional behavior is required.

---

# 📬 9. Contact

For questions or guidance:

- open a GitHub issue  
- or contact the maintainer: **@richardpizem-ctrl**

---

# 🚀 Thank You

Your contributions help build the world’s first **fully offline mobile AI assistant**.  
Together we are creating something unique, safe, and powerful.
