# 🔐 SIRIUS LOCAL AI GAMA – Security Policy (v2.0.0)

SIRIUS LOCAL AI GAMA is a fully offline, privacy‑first mobile AI runtime.  
This security policy defines how vulnerabilities are reported, validated, and resolved in version **2.0.0**.

---

# 🛡 1. Supported Versions

Only the latest stable version of GAMA receives security updates.

| Version | Supported |
|--------|-----------|
| **GAMA 2.x** | ✔ Yes |
| **GAMA 1.x** | ✖ No |
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
- exploit the vulnerability beyond what is necessary  
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
7. **Disclosure** – A short summary appears in the changelog  

---

# 🧱 5. Security Scope (Updated for 2.0.0)

This policy covers vulnerabilities related to:

- mobile runtime stability  
- offline reasoning engine  
- workflow engine 2.0  
- mobile vision engine  
- knowledge packs  
- identity & safety layers (SECURITY FAMILY Mobile)  
- file handling  
- memory handling  
- denial‑of‑service vectors  
- module privilege isolation  
- event‑level sandboxing  
- hybrid input processing  
- diagnostics engine (NEW)  
- LAN Offline Bridge (NEW)  

It does **not** cover:

- feature requests  
- UI bugs  
- performance issues  
- expected behavior differences  

These should be reported via normal GitHub issues.

---

# 🔒 6. Safe Development Practices (Updated for 2.0.0)

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
- no dynamic imports  
- no privileged module escalation  
- strict validation of all external data  
- no network calls except LAN Offline Bridge (NEW)  
- no access to PC runtime without explicit pairing (NEW)  

---

# 🟪 6.5 Hybrid‑Safe Architecture (Preview for GAMA 4.0)

GAMA 4.0 introduces a **hybrid‑safe architecture** that preserves full offline security while allowing controlled, sanitized import of online data.

## 🟦 Secure Online Envoy (Isolated Online Agent)
- runs in a fully isolated sandbox  
- one‑way outbound access  
- fetches text, JSON, structured data  
- cannot access local files, models, or APIs  
- cannot send local data outward  
- always classified as **low‑trust**  

## 🟩 Quarantine Pipeline (Data Sanitization Layer)
All data returned by the envoy is processed through a strict quarantine:

- script & HTML removal  
- format validation  
- size limits  
- text cleaning  
- security filtering  
- only clean text + JSON allowed  
- integration with Security Family  

Offline modules **never** interact with untrusted data.

## 🟧 Offline Core Remains Fully Air‑Gapped
- inference offline  
- reasoning offline  
- knowledge packs offline  
- no cloud calls  
- no telemetry  
- no outbound data  

---

# 🛡 6.6 Security Family Integration (Updated)

Security Family enforces additional rules for hybrid‑safe mode:

- envoy data is always low‑trust  
- no remote code execution  
- no dynamic evaluation  
- no cross‑module privilege escalation  
- no direct access to runtime context  
- quarantine rejects unsafe data  
- all violations logged in Security Diagnostics  

---

# 🧪 6.7 Security Testing Requirements (Updated)

All contributors must ensure:

- static analysis of all modules  
- no unsafe dependencies  
- no network calls except LAN Offline Bridge  
- deterministic execution paths  
- reproducible builds  
- no hidden telemetry  
- no analytics libraries  
- no external SDKs  
- diagnostics logs must not contain sensitive data (NEW)  

---

# 🛡 6.8 Behavioral Safety Policy (v2.0) — NEW

GAMA 2.0 includes foundational behavioral safety mechanisms.  
This section formalizes them as part of the official security policy.

## 🔐 Behavioral Determinism
- no hallucinations  
- no unverified claims  
- if uncertain → respond “I don’t know”  
- deterministic reasoning sequences  
- safe fallback behavior  

## 👨‍👩‍👧 Family‑Safe Rules
- child‑safe content filters  
- blocking sensitive topics  
- safe offline explanations  
- limited reasoning for minors  

## 🔍 Local Ethical Filters
- all filters run locally  
- no cloud requests  
- no external APIs  
- no data transmission  

## 🧱 Module Safety Sandbox
- event‑level sandboxing  
- module isolation  
- no dynamic operations  
- no access outside allowed scope  

## 🚫 Behavioral Limits
- no medical, legal, or dangerous advice  
- no harmful content generation  
- no autonomous decisions  
- no manipulation or persuasion  

## 📜 Auditability
- reasoning traces  
- security logs  
- transparent decision steps  
- deterministic repeatable outputs  

---

# ❤️ 7. Thank You

Security researchers and contributors help keep  
**SIRIUS LOCAL AI GAMA safe, private, and fully offline**.

Your responsible reporting protects users worldwide.

