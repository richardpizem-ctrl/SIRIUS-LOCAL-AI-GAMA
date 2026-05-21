# 🛡 GAMA Security Family — Version 3.1.0

The Security Family is the **central safety subsystem** of the SIRIUS LOCAL AI GAMA 3.x ecosystem.  
It enforces deterministic safety rules, restricted‑mode behavior, sandbox isolation,  
low‑trust data handling, hybrid‑safe protections, PACK_SUGGEST safety, and unified result schema v3.1.

Version **3.1.0** introduces improved restricted‑mode enforcement,  
**Metadata v3.1**, **EV3.1 security events**, PACK_SUGGEST safety rules,  
expanded diagnostics, hybrid‑safe enforcement v3.1, and reduced false‑positive triggers.

---

# 🎯 Responsibilities
- behavioral monitoring  
- safety rule enforcement  
- blocking unsafe operations  
- parental/child mode support  
- restricted‑mode enforcement v3.1  
- sandbox isolation  
- low‑trust data handling  
- output safety validation  
- anomaly detection  
- PACK_SUGGEST safety filtering  
- integration with Runtime Core 3.1  
- unified SECURITY_EVENT (EV3.1)  
- unified result schema v3.1  

---

# 🧩 Modes (v3.1)
- **Owner Mode**  
- **Teen Mode**  
- **Child Mode**  
- **Restricted Mode (v3.1)**  
- **Auto‑Adaptive Mode**  

Restricted Mode v3.1 is **non‑bypassable**, automatically triggered by:
- low‑trust inputs  
- unsafe content  
- anomaly detection  
- sandbox violations  
- PACK_SUGGEST unsafe patterns  

---

# 📤 Output (v3.1)
- allow / deny decisions  
- security flags  
- restricted_mode flag  
- sandbox_enforced flag  
- trust_level  
- behavior logs  
- anomaly reports  
- quarantine flags  
- PACK_SUGGEST safety flags  
- metadata v3.1  
- unified result schema v3.1  

---

# 🛡️ BEHAVIORAL SAFETY POLICY (v3.1) — UPDATED

GAMA 3.1 formalizes all safety mechanisms into a unified **Behavioral Safety Policy**,  
ensuring deterministic, safe, family‑friendly execution across all modules.

## 🔐 1. Behavioral Determinism (v3.1)
- no hallucinations  
- no unverified claims  
- if uncertain → respond “I don’t know”  
- deterministic reasoning sequences  
- reasoning_trace v3.1  
- EV3.1 metadata tagging  
- unified result schema v3.1  

## 👨‍👩‍👧 2. Family‑Safe Mode (v3.1)
- child‑safe content  
- blocking sensitive topics  
- safe offline explanations  
- limited reasoning for minors  
- school explanations without risky content  

## 🔍 3. Local Ethical Filters (v3.1)
- all filters run locally  
- no cloud requests  
- no external APIs  
- no data transmission  
- no remote logging  
- PACK_SUGGEST safety filtering  

## 🧱 4. Module Safety Sandbox (v3.1)
- event‑level sandboxing  
- module isolation  
- no dynamic operations  
- no cross‑module privilege escalation  
- low‑trust data isolation  
- hybrid‑safe enforcement  
- PACK_SUGGEST sandbox rules  

## 🚫 5. Behavioral Limits (v3.1)
Security Family will **never** allow:
- medical, legal, or dangerous advice  
- harmful content generation  
- identity inference  
- autonomous decisions  
- manipulation or persuasion  

## 📜 6. Auditability (v3.1)
- reasoning_trace v3.1  
- security_trace  
- restricted_mode events  
- sandbox_enforced events  
- PACK_SUGGEST logs  
- deterministic repeatable outputs  

---

# 🏷 Version
**GAMA Security Family — v3.1.0**  
(fully aligned with Runtime 3.1.0 and Unified Event Architecture 3.1.x)

---

# 🔄 Security Flow (v3.1.0)

1. Runtime sends a SECURITY_EVENT (EV3.1).  
2. Security Family identifies active mode:  
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
7. Apply restricted‑mode or sandbox if required.  
8. Apply PACK_SUGGEST safety rules if applicable.  
9. Log the event in Security Diagnostics.  
10. Update behavior profile (if enabled).  
11. Apply quarantine rules for low‑trust data.  
12. Return final decision to Runtime.  

---

# 🧱 Security Components (v3.1)

## 1. Behavior Monitor v3.1
Tracks user actions and system events.
- action classification  
- frequency analysis  
- anomaly detection  
- mode‑specific behavior rules  
- hybrid‑input behavior tracking  
- PACK_SUGGEST safety detection  
- escalation triggers  
- trust_level updates  

---

## 2. Safety Rules Engine v3.1
Evaluates actions against security policies.
- rule matching  
- violation detection  
- severity scoring  
- allow/deny logic  
- rule chaining v3.1  
- safety‑intent detection  
- restricted‑mode triggers  
- PACK_SUGGEST unsafe pattern detection  

---

## 3. Mode Controller v3.1
Determines active security mode.
- Owner / Teen / Child / Restricted  
- automatic mode switching  
- behavior‑based escalation  
- restricted‑mode hardening  
- sandbox enforcement  
- PACK_SUGGEST safety escalation  

---

## 4. Operation Filter v3.1
Blocks or allows system operations.
- file access control  
- network restrictions  
- command filtering  
- sensitive operation blocking  
- module‑level privilege isolation  
- event‑level sandboxing  
- hybrid‑safe enforcement  
- PACK_SUGGEST safety filtering  

---

## 5. Behavior Profile Manager v3.1
Maintains long‑term behavior patterns.
- habit learning  
- deviation detection  
- adaptive restrictions  
- profile updates  
- anomaly‑based cooldowns  
- child‑safe behavior shaping  
- PACK_SUGGEST behavior tracking  

---

## 6. Security Diagnostics Logger v3.1
Records all security‑related events.
- allowed actions  
- blocked actions  
- rule violations  
- mode changes  
- anomaly reports  
- quarantine rejections  
- sandbox_enforced events  
- restricted_mode events  
- PACK_SUGGEST safety logs  
- envoy‑related violations  

---

# 🟪 Secure Online Envoy & Quarantine Pipeline (v4 Preview)

GAMA v4 introduces a **hybrid‑safe extension** of the Security Family,  
allowing controlled online data retrieval while keeping the AI core fully offline.

## 🟦 Secure Online Envoy (Isolated Online Agent)
- isolated sandbox process  
- outbound‑only internet  
- fetches text, JSON, structured data  
- no access to local files, models, or APIs  
- no local data ever sent outward  
- always treated as **low‑trust**  

## 🟩 Quarantine Pipeline (Security Integration)
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

## 🟧 Enforcement
If anomaly detected:
- quarantine rejects data  
- Security Family logs violation  
- Runtime receives `"deny"`  

---

# 🔁 Security Execution Cycle (v3.1.0)

1. Runtime sends SECURITY_EVENT (EV3.1).  
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

# 🟫 NEW IN VERSION 3.1.0
- metadata v3.1  
- event versioning EV3.1  
- unified result schema v3.1  
- PACK_SUGGEST safety rules  
- improved restricted‑mode enforcement  
- improved sandbox enforcement  
- hybrid‑safe enforcement v3.1  
- low‑trust classification v3.1  
- rule chaining v3.1  
- module privilege isolation v3.1  
- diagnostics expansion v3.1  
- reduced false‑positive triggers  

---

# ✔ GAMA Security Family 3.1 — COMPLETE  
Fully aligned with the SIRIUS LOCAL AI GAMA 3.1.x ecosystem.
