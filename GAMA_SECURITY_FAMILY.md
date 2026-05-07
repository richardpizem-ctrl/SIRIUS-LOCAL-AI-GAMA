# 🛡 GAMA Security Family

Security Family provides behavioral monitoring, safety rules, and protection for the GAMA system.

---

# 🎯 Responsibilities
- behavior monitoring  
- safety rule enforcement  
- blocking dangerous operations  
- parental/child mode support  
- integration with Runtime and Router  
- output safety validation (NEW)  
- low‑trust data handling (NEW)  
- anomaly‑based restrictions (NEW)  

---

# 🧩 Modes
- Owner Mode  
- Teen Mode  
- Child Mode  
- Restricted Mode  
- Auto‑Adaptive Mode (NEW – optional)  

---

# 📤 Output
- allow / deny decisions  
- security flags  
- behavior logs  
- anomaly reports (NEW)  
- quarantine flags (NEW)  

---

# 🏷 Version
**GAMA Security Family — v1.0.0**  
(prepared for GAMA 3.0.0‑pre and extended in GAMA 4.0)

---

# 🔄 Security Flow

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
9. Return final decision to the Runtime.  
10. Apply quarantine rules if data is external (NEW).  

---

# 🧱 Security Components

## 1. Behavior Monitor
Tracks user actions and system events.
- action classification  
- frequency analysis  
- anomaly detection  
- mode‑specific behavior rules  
- hybrid‑input behavior tracking (NEW)  
- escalation triggers (NEW)  

## 2. Safety Rules Engine
Evaluates actions against security policies.
- rule matching  
- violation detection  
- severity scoring  
- allow/deny logic  
- rule chaining (NEW)  
- safety‑intent detection (NEW)  

## 3. Mode Controller
Determines active security mode.
- Owner / Teen / Child / Restricted  
- automatic mode switching (optional)  
- behavior‑based mode escalation (NEW)  
- restricted‑mode hardening (NEW)  

## 4. Operation Filter
Blocks or allows system operations.
- file access control  
- network restrictions  
- command filtering  
- sensitive operation blocking  
- module‑level privilege isolation (NEW)  
- event‑level sandboxing (NEW)  

## 5. Behavior Profile Manager
Maintains long‑term behavior patterns.
- learning user habits  
- detecting deviations  
- adaptive restrictions  
- profile updates  
- anomaly‑based cooldowns (NEW)  
- child‑safe behavior shaping (NEW)  

## 6. Security Diagnostics Logger
Records all security‑related events.
- allowed actions  
- blocked actions  
- rule violations  
- mode changes  
- anomaly reports  
- quarantine rejections (NEW)  
- envoy‑related violations (NEW)  

---

# 🟪 NEW IN GAMA v4 — Secure Online Envoy & Quarantine Pipeline

GAMA v4 introduces a **hybrid‑safe extension** of the Security Family, enabling controlled online data retrieval while keeping the entire AI core fully offline and protected.

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

## 🟪 Why This Matters
- offline AI remains offline  
- online data is sanitized and isolated  
- Security Family becomes the **gatekeeper**  
- architecture matches air‑gapped enterprise systems  
- zero risk of RCE or data leakage  

---

# 🔁 Security Execution Cycle

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
