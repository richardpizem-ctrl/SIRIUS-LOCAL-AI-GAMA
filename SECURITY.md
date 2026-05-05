# 🔐 SIRIUS LOCAL AI GAMA – Security Policy

SIRIUS LOCAL AI GAMA is a fully offline, privacy‑first mobile AI runtime.  
This security policy explains how vulnerabilities should be reported and how they are handled.

---

# 🛡 1. Supported Versions

Only the latest stable version of GAMA receives security updates.

| Version | Supported |
|--------|-----------|
| **GAMA 1.x** | ✔ Yes |
| **GAMA 0.x** | ✖ No |

Older versions may contain unresolved vulnerabilities and should not be used in production environments.

---

# 🚨 2. Reporting a Vulnerability

If you discover a security vulnerability, please report it **privately**.

### ✔ Recommended method  
Open a **private GitHub issue** in this repository.

### ✔ Alternative contact  
Maintainer: **@richardpizem-ctrl**

Please include:

- clear description of the issue  
- steps to reproduce  
- potential impact  
- affected modules or files  
- logs or screenshots (if available)  

All reports will be reviewed as soon as possible.

---

# 🧭 3. Responsible Disclosure Guidelines

To protect users and contributors, please follow these rules:

### ✔ Do:
- report vulnerabilities privately  
- allow reasonable time for investigation  
- provide clear technical details  
- include reproduction steps  
- keep communication confidential  

### ✖ Do NOT:
- publicly disclose the vulnerability before it is fixed  
- exploit the vulnerability beyond what is necessary to demonstrate it  
- share the vulnerability with third parties  
- use the vulnerability to access unauthorized data  

---

# 🛠 4. How We Handle Vulnerabilities

When a vulnerability is reported:

1. **Acknowledgment** – Maintainer confirms receipt  
2. **Assessment** – Severity and impact are evaluated  
3. **Reproduction** – Issue is reproduced in a controlled environment  
4. **Fix Development** – Patch or mitigation is created  
5. **Verification** – Fix is tested  
6. **Release** – Security update is published  
7. **Disclosure** – A short summary may appear in the changelog  

---

# 🧱 5. Security Scope

This policy covers vulnerabilities related to:

- mobile runtime stability  
- offline reasoning engine  
- workflow engine  
- mobile vision engine  
- knowledge packs  
- identity & safety layers (SECURITY FAMILY Mobile)  
- file handling  
- memory handling  
- denial‑of‑service vectors  

It does **not** cover:

- feature requests  
- UI bugs  
- performance issues  
- expected behavior differences  

These should be reported via normal GitHub issues.

---

# 🔒 6. Safe Development Practices

Contributors must follow these principles:

- no cloud APIs  
- no telemetry  
- no remote code execution  
- no unsafe eval/exec  
- strict separation of UI and logic  
- no untrusted code execution  
- minimal dependencies  
- deterministic behavior  
- sandboxed processing  

---

# ❤️ 7. Thank You

Security researchers and contributors help keep  
**SIRIUS LOCAL AI GAMA safe, private, and fully offline**.

Your responsible reporting protects users worldwide.
