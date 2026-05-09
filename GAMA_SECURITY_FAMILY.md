# 🛡 GAMA Security Family — Version 2.0.0

Security Family provides behavioral monitoring, safety rules, and protection for the GAMA 2.0 system.  
Version 2.0.0 introduces **low‑trust data handling**, **output safety validation**, and **anomaly‑based restrictions**.

---

# 🎯 Responsibilities
- behavior monitoring  
- safety rule enforcement  
- blocking dangerous operations  
- parental/child mode support  
- integration with Runtime and Router  
- output safety validation  
- low‑trust data handling  
- anomaly‑based restrictions  

---

# 🧩 Modes
- **Owner Mode**  
- **Teen Mode**  
- **Child Mode**  
- **Restricted Mode**  
- **Auto‑Adaptive Mode** (optional)  

---

# 📤 Output
- allow / deny decisions  
- security flags  
- behavior logs  
- anomaly reports  
- quarantine flags  

---

# 🛡️ BEHAVIORAL SAFETY POLICY (v2.0) — NEW

GAMA 2.0 already includes foundational safety mechanisms (restricted mode, child‑safe filters, sandboxing).  
This section formalizes them into a **Behavioral Safety Policy**, ensuring GAMA is safe for families, children, and everyday users.

## 🔐 1. Behavioral Determinism (v2)
- no hallucinations  
- no unverified claims  
- if uncertain → responds “I don’t know”  
- deterministic reasoning sequences  
- reasoning trace for schoolwork  

## 👨‍👩‍👧 2. Family‑Safe Mode (v2)
- child‑safe content  
- blocking sensitive topics  
- safe offline explanations  
- limited reasoning for minors  
- school explanations without risky content  

## 🔍 3. Local Ethical Filters (v2)
- all filters run locally  
- no cloud requests  
- no external APIs  
- no data transmission  
- no remote logging  

## 🧱 4. Module Safety Sandbox (v2)
- event‑level sandboxing  
- module isolation  
- no dynamic operations  
- no access outside allowed scope  
- low‑trust data handling  

## 🚫 5. Behavioral Limits (v2)
- no medical, legal, or dangerous advice  
- no harmful content generation  
- no autonomous decisions  
- no manipulation or persuasion  

## 📜 6. Auditability (v2)
- reasoning_trace for schoolwork  
- event logs for safety decisions  
- transparent decision steps  
- deterministic repeatable outputs  

---

# 🏷 Version
**GAMA Security Family — v2.0.0**  
(compatible with GAMA Runtime 2.0, prepared for 3.0.0‑pre, extended in 4.0)

---

# 🔄 Security Flow (v2.0.0)

1. Runtime sends a security‑relevant event or user action.  
2. Security Family identifies the active mode:  
   - Owner  
   - Teen  
   - Child  
   - Restricted  
3. Behavior Monitor evaluates the action.  
4. Safety Rules Engine checks for violations.  
5. If safe:  
   - allow the action  
   - return `"allow"`  
6. If unsafe:  
   - block the action  
   - return `"deny"` + security flags  
7. Log the event in the Security Diagnostics Log.  
8. Update behavior profile (if enabled).  
9. Apply quarantine rules if data is external.  
10. Return final decision to the Runtime.  

---

# 🧱 Security Components

## 1. Behavior Monitor
Tracks user actions and system events.
- action classification  
- frequency analysis  
- anomaly detection  
- mode‑specific behavior rules  
- hybrid‑input behavior tracking  
- escalation triggers  

## 2. Safety Rules Engine
Evaluates actions against security policies.
- rule matching  
- violation detection  
- severity scoring  
- allow/deny logic  
- rule chaining  
- safety‑intent detection  

## 3. Mode Controller
Determines active security mode.
- Owner / Teen / Child / Restricted  
- automatic mode switching (optional)  
- behavior‑based mode escalation  
- restricted‑mode hardening  

## 4. Operation Filter
Blocks or allows system operations.
- file access control  
- network restrictions  
- command filtering  
- sensitive operation blocking  
- module‑level privilege isolation  
- event‑level sandboxing  

## 5. Behavior Profile Manager
Maintains long‑term behavior patterns.
- learning user habits  
- detecting deviations  
- adaptive restrictions  
- profile updates  
- anomaly‑based cooldowns  
- child‑safe behavior shaping  

## 6. Security Diagnostics Logger
Records all security‑related events.
- allowed actions  
- blocked actions  
- rule violations  
- mode changes  
- anomaly reports  
- quarantine rejections  
- envoy‑related violations  

---

# 🟪 NEW IN GAMA v4 — Secure Online Envoy & Quarantine Pipeline (Preview)

GAMA v4 introduces a **hybrid‑safe extension** of the Security Family, enabling controlled online data retrieval while keeping the entire AI core fully offline.

## 🟦 Secure Online Envoy (Isolated Online Agent)
- runs in a fully isolated sandbox  
- one‑way outbound internet access  
- fetches text, JSON, structured data  
- no access to local files, models, or system APIs  
- no local data ever sent outward  
- treated as **untrusted external input**  

## 🟩 Quarantine Pipeline (Security Family Integration)
All envoy data passes through strict sanitization:
- script & HTML removal  
- format validation  
- size limits  
- text cleaning  
- security filtering  
- only clean text + JSON allowed  

Security Family ensures **no untrusted data** reaches:
- Runtime  
- Router  
- Reasoning Engine  
- Knowledge Packs  
- Vision Engine  

## 🟧 Security Family Enforcement
Security Family applies additional rules:
- envoy data = **low‑trust**  
- no remote code execution  
- no dynamic imports  
- no system operations  
- no cross‑module privileges  

If anomaly detected:
- quarantine rejects data  
- Security Family logs violation  
- Runtime receives `"deny"`  

---

# 🔁 Security Execution Cycle (v2.0.0)

1. Runtime sends a user action or system event.  
2. Mode Controller determines active mode.  
3. Behavior Monitor analyzes context.  
4. Safety Rules Engine evaluates policies.  
5. If safe → Operation Filter allows action.  
6. If unsafe → Operation Filter blocks action.  
7. Behavior Profile Manager updates patterns.  
8. Security Diagnostics Logger records event.  
9. Decision returned to Runtime.  
10. System waits for next event.  

---

# 🟫 NEW IN VERSION 2 → PREPARED FOR VERSION 3.0.0‑pre
- safety‑intent detection  
- rule chaining  
- module privilege isolation  
- event‑level sandboxing  
- hybrid‑input behavior tracking  
- anomaly‑based restrictions  
- restricted‑mode hardening  
- unified SECURITY event metadata  
- envoy low‑trust classification  
- quarantine integration
