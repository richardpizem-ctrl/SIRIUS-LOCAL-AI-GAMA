# 🔐 SIRIUS LOCAL AI GAMA – Security Policy (v3.1.0)

SIRIUS LOCAL AI GAMA is a fully offline, privacy‑first mobile AI runtime.  
This security policy defines how vulnerabilities are reported, validated, and resolved in version **3.1.0**, aligned with the **Unified Event Architecture 3.1.x**, **Metadata v3.1**, **Restricted Mode v3.1**, **Sandbox Enforcement v3.1**, **PACK_SUGGEST safety**, and the **Hybrid‑Safe Pipeline**.

---

# 🛡 1. Supported Versions

Only the latest stable version of GAMA receives security updates.

| Version | Supported |
|--------|-----------|
| **GAMA 3.1.x** | ✔ Yes |
| **GAMA 3.0.x** | ✔ Yes (security fixes only) |
| **GAMA 2.x** | ✖ No (critical fixes only) |
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

# 🧱 5. Security Scope (Updated for 3.1.0)

This policy covers vulnerabilities related to:

- deterministic runtime core v3.1  
- unified event architecture 3.1.x  
- restricted mode v3.1  
- sandbox enforcement v3.1  
- hybrid‑safe pipeline  
- offline reasoning engine  
- workflow engine 3.1  
- vision engine 3.1  
- schoolwork mode 3.1  
- health assistant 3.1  
- knowledge packs 3.1  
- PACK_SUGGEST safety  
- module privilege isolation  
- event metadata engine v3.1  
- LAN Offline Bridge  
- diagnostics engine v3.1  
- low‑trust input handling  

It does **not** cover:

- feature requests  
- UI bugs  
- performance issues  
- expected behavior differences  

These should be reported via normal GitHub issues.

---

# 🔒 6. Safe Development Practices (Updated for 3.1.0)

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
- no network calls except LAN Offline Bridge  
- no access to PC runtime without explicit pairing  
- all hybrid inputs treated as **low‑trust**  
- PACK_SUGGEST safety enforcement  
- restricted/sandbox enforcement for all modules  

---

# 🟪 6.5 Hybrid‑Safe Architecture (Core of GAMA 4.0 — Adopted in 3.1)

GAMA 3.1 integrates the **hybrid‑safe foundation** of the upcoming 4.0 architecture.

## 🟦 Secure Online Envoy (Isolated Online Agent)
- runs in a fully isolated sandbox  
- outbound‑only access  
- fetches text, JSON, structured data  
- cannot access local files, models, or APIs  
- cannot send local data outward  
- always classified as **low‑trust**  
- PACK_SUGGEST safety rules applied  

## 🟩 Quarantine Pipeline (Data Sanitization Layer)
All data returned by the envoy is processed through a strict quarantine:

- script & HTML removal  
- format validation  
- size limits  
- text cleaning  
- security filtering  
- only clean text + JSON allowed  
- integration with Security Family 3.1  

Offline modules **never** interact with untrusted data.

## 🟧 Offline Core Remains Fully Air‑Gapped
- inference offline  
- reasoning offline  
- knowledge packs offline  
- no cloud calls  
- no telemetry  
- no outbound data  

---

# 🛡 6.6 Security Family Integration (v3.1)

Security Family enforces additional rules for hybrid‑safe mode:

- envoy data is always low‑trust  
- no remote code execution  
- no dynamic evaluation  
- no cross‑module privilege escalation  
- no direct access to runtime context  
- quarantine rejects unsafe data  
- PACK_SUGGEST violations logged  
- restricted mode v3.1 automatically enabled on anomalies  

---

# 🧪 6.7 Security Testing Requirements (Updated for 3.1.0)

All contributors must ensure:

- static analysis of all modules  
- no unsafe dependencies  
- no network calls except LAN Offline Bridge  
- deterministic execution paths  
- reproducible builds  
- no hidden telemetry  
- no analytics libraries  
- no external SDKs  
- diagnostics logs must not contain sensitive data  
- restricted/sandbox behavior must be testable  
- hybrid‑safe pipeline must be validated  
- PACK_SUGGEST safety must be validated  

---

# 🛡 6.8 Behavioral Safety Policy (v3.1)

GAMA 3.1 includes a fully formalized behavioral safety layer.

## 🔐 Behavioral Determinism
- no hallucinations  
- no unverified claims  
- if uncertain → respond “I don’t know”  
- deterministic reasoning sequences  
- safe fallback behavior  
- metadata v3.1 trace  
- unified result schema v3.1  

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
- restricted mode logs  
- sandbox enforcement logs  
- PACK_SUGGEST logs  
- deterministic repeatable outputs  

---

# ❤️ 7. Thank You

Security researchers and contributors help keep  
**SIRIUS LOCAL AI GAMA safe, private, and fully offline**.

Your responsible reporting protects users worldwide.
