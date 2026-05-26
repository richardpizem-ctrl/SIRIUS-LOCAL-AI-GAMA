# 🛡 GAMA Security Family — Version 3.2.0

The Security Family is the **central safety subsystem** of the SIRIUS LOCAL AI GAMA 3.x ecosystem.  
It enforces deterministic safety rules, restricted‑mode behavior, sandbox isolation,  
low‑trust data handling, hybrid‑safe protections, PACK_SUGGEST safety, VisionEngineV3 safety routing,  
and unified result schema v3.2.

Version **3.2.0** introduces improved restricted‑mode enforcement,  
**Metadata v3.2**, **EV3.2 security events**, PACK_SUGGEST v3.2 safety rules,  
VisionEngineV3 event safety, expanded diagnostics, hybrid‑safe enforcement v3.2,  
and reduced false‑positive triggers.

---

# 🎯 Responsibilities
- behavioral monitoring  
- safety rule enforcement  
- blocking unsafe operations  
- parental/child mode support  
- restricted‑mode enforcement v3.2  
- sandbox isolation  
- low‑trust data handling  
- output safety validation  
- anomaly detection  
- PACK_SUGGEST safety filtering  
- VisionEngineV3 event safety  
- integration with Runtime Core 3.2  
- unified SECURITY_EVENT (EV3.2)  
- unified result schema v3.2  

---

# 🧩 Modes (v3.2)
- **Owner Mode**  
- **Teen Mode**  
- **Child Mode**  
- **Restricted Mode (v3.2)**  
- **Auto‑Adaptive Mode**  

Restricted Mode v3.2 is **non‑bypassable**, automatically triggered by:
- low‑trust inputs  
- unsafe content  
- anomaly detection  
- sandbox violations  
- PACK_SUGGEST unsafe patterns  
- unsafe SCENE / DETECT / OCR / HOMEWORK events  

---

# 📤 Output (v3.2)
- allow / deny decisions  
- security flags  
- restricted_mode flag  
- sandbox_enforced flag  
- trust_level  
- behavior logs  
- anomaly reports  
- quarantine flags  
- PACK_SUGGEST safety flags  
- VisionEngineV3 safety flags  
- metadata v3.2  
- unified result schema v3.2  

---

# 🛡️ BEHAVIORAL SAFETY POLICY (v3.2) — UPDATED

GAMA 3.2 formalizes all safety mechanisms into a unified **Behavioral Safety Policy**,  
ensuring deterministic, safe, family‑friendly execution across all modules.

## 🔐 1. Behavioral Determinism (v3.2)
- no hallucinations  
- no unverified claims  
- if uncertain → respond “I don’t know”  
- deterministic reasoning sequences  
- reasoning_trace v3.2  
- EV3.2 metadata tagging  
- unified result schema v3.2  

## 👨‍👩‍👧 2. Family‑Safe Mode (v3.2)
- child‑safe content  
- blocking sensitive topics  
- safe offline explanations  
- limited reasoning for minors  
- school explanations without risky content  

## 🔍 3. Local Ethical Filters (v3.2)
- all filters run locally  
- no cloud requests  
- no external APIs  
- no data transmission  
- no remote logging  
- PACK_SUGGEST safety filtering  
- VisionEngineV3 unsafe‑content filtering  

## 🧱 4. Module Safety Sandbox (v3.2)
- event‑level sandboxing  
- module isolation  
- no dynamic operations  
- no cross‑module privilege escalation  
- low‑trust data isolation  
- hybrid‑safe enforcement  
- PACK_SUGGEST sandbox rules  
- VisionEngineV3 sandbox rules  

## 🚫 5. Behavioral Limits (v3.2)
Security Family will **never** allow:
- medical, legal, or dangerous advice  
- harmful content generation  
- identity inference  
- autonomous decisions  
- manipulation or persuasion  

## 📜 6. Auditability (v3.2)
- reasoning_trace v3.2  
- security_trace  
- restricted_mode events  
- sandbox_enforced events  
- PACK_SUGGEST logs  
- VisionEngineV3 safety logs  
- deterministic repeatable outputs  

---

# 🏷 Version
**GAMA Security Family — v3.2.0**  
(fully aligned with Runtime 3.2.0, VisionEngineV3, and Unified Event Architecture 3.2.x)

---

# 🔄 Security Flow (v3.2.0)

1. Runtime sends a SECURITY_EVENT (EV3.2).  
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
9. Apply VisionEngineV3 safety rules for SCENE / DETECT / OCR / HOMEWORK events.  
10. Log the event in Security Diagnostics.  
11. Update behavior profile (if enabled).  
12. Apply quarantine rules for low‑trust data.  
13. Return final decision to Runtime.  

---

# 🧱 Security Components (v3.2)

## 1. Behavior Monitor v3.2
Tracks user actions and system events.
- action classification  
- frequency analysis  
- anomaly detection  
- mode‑specific behavior rules  
- hybrid‑input behavior tracking  
- PACK_SUGGEST safety detection  
- VisionEngineV3 unsafe‑content detection  
- escalation triggers  
- trust_level updates  

---

## 2. Safety Rules Engine v3.2
Evaluates actions against security policies.
- rule matching  
- violation detection  
- severity scoring  
- allow/deny logic  
- rule chaining v3.2  
- safety‑intent detection  
- restricted‑mode triggers  
- PACK_SUGGEST unsafe pattern detection  
- VisionEngineV3 unsafe pattern detection  

---

## 3. Mode Controller v3.2
Determines active security mode.
- Owner / Teen / Child / Restricted  
- automatic mode switching  
- behavior‑based escalation  
- restricted‑mode hardening  
- sandbox enforcement  
- PACK_SUGGEST safety escalation  
- VisionEngineV3 safety escalation  

---

## 4. Operation Filter v3.2
Blocks or allows system operations.
- file access control  
- network restrictions  
- command filtering  
- sensitive operation blocking  
- module‑level privilege isolation  
- event‑level sandboxing  
- hybrid‑safe enforcement  
- PACK_SUGGEST safety filtering  
- VisionEngineV3 safety filtering  

---

## 5. Behavior Profile Manager v3.2
Maintains long‑term behavior patterns.
- habit learning  
- deviation detection  
- adaptive restrictions  
- profile updates  
- anomaly‑based cooldowns  
- child‑safe behavior shaping  
- PACK_SUGGEST behavior tracking  
- VisionEngineV3 behavior tracking  

---

## 6. Security Diagnostics Logger v3.2
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
- VisionEngineV3 safety logs  
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

# 🔁 Security Execution Cycle (v3.2.0)

1. Runtime sends SECURITY_EVENT (EV3.2).  
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

# 🟫 NEW IN VERSION 3.2.0
- metadata v3.2  
- event versioning EV3.2  
- unified result schema v3.2  
- PACK_SUGGEST safety v3.2  
- VisionEngineV3 safety integration  
- improved restricted‑mode enforcement  
- improved sandbox enforcement  
- hybrid‑safe enforcement v3.2  
- low‑trust classification v3.2  
- rule chaining v3.2  
- module privilege isolation v3.2  
- diagnostics expansion v3.2  
- reduced false‑positive triggers  

---

# ✔ GAMA Security Family 3.2 — COMPLETE  
Fully aligned with the SIRIUS LOCAL AI GAMA 3.2.x ecosystem.
