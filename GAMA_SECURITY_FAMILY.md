# GAMA Security Family

Security Family provides behavioral monitoring, safety rules, and protection for the GAMA system.

## Responsibilities
- behavior monitoring
- safety rule enforcement
- blocking dangerous operations
- parental/child mode support
- integration with Runtime and Router

## Modes
- Owner Mode
- Teen Mode
- Child Mode
- Restricted Mode

## Output
- allow / deny decisions
- security flags
- behavior logs

## Version
GAMA Security Family — v1.0.0

## Security Flow

1. Runtime sends a security‑relevant event or user action.
2. Security Family identifies the active mode:
   - Owner Mode
   - Teen Mode
   - Child Mode
   - Restricted Mode
3. Behavior Monitor evaluates the action.
4. Safety Rules Engine checks for violations.
5. If safe:
   - allow the action
   - return "allow" decision
6. If unsafe:
   - block the action
   - return "deny" decision with security flags
7. Log the event in the Security Diagnostics Log.
8. Update behavior profile (if enabled).
9. Return final decision to the Runtime.

## Security Components

### 1. Behavior Monitor
Tracks user actions and system events.
- action classification
- frequency analysis
- anomaly detection
- mode‑specific behavior rules

### 2. Safety Rules Engine
Evaluates actions against security policies.
- rule matching
- violation detection
- severity scoring
- allow/deny decision logic

### 3. Mode Controller
Determines active security mode.
- Owner Mode
- Teen Mode
- Child Mode
- Restricted Mode
- automatic mode switching (optional)

### 4. Operation Filter
Blocks or allows system operations.
- file access control
- network restrictions
- command filtering
- sensitive operation blocking

### 5. Behavior Profile Manager
Maintains long‑term behavior patterns.
- learning user habits
- detecting deviations
- adaptive restrictions
- profile updates

### 6. Security Diagnostics Logger
Records all security‑related events.
- allowed actions
- blocked actions
- rule violations
- mode changes
- anomaly reports

---

# 🟪 NEW IN GAMA v4 — Secure Online Envoy & Quarantine Pipeline

GAMA v4 introduces a **hybrid‑safe extension** of the Security Family, enabling controlled online data retrieval while keeping the entire AI core fully offline and protected.

## 🟦 Secure Online Envoy (Isolated Online Agent)
- runs in a fully isolated sandbox  
- has **one‑way outbound** access to the internet  
- can fetch text, JSON, structured data  
- cannot access local files, models, or system APIs  
- cannot send any local data outward  
- treated as an **untrusted external source** by Security Family  

## 🟩 Quarantine Pipeline (Security Family Integration)
All data from the envoy is processed through a strict quarantine layer:

- script & HTML removal  
- format validation  
- size limits  
- text cleaning  
- security filtering  
- only clean text + JSON + structured data allowed  

Security Family ensures that **no untrusted data** ever reaches:

- Runtime  
- Router  
- Reasoning Engine  
- Knowledge Packs  
- Vision Engine  

## 🟧 Security Family Enforcement
Security Family applies additional rules:

- envoy data is always treated as **low‑trust**  
- no execution of remote code  
- no dynamic imports  
- no direct system operations  
- no cross‑module privileges  

If any anomaly is detected:

- quarantine rejects the data  
- Security Family logs the violation  
- Runtime receives a **deny** decision  

## 🟪 Why This Matters
- offline AI remains offline  
- online data is sanitized and isolated  
- Security Family becomes the **gatekeeper** for all external inputs  
- architecture matches air‑gapped enterprise systems  
- zero risk of remote code execution or data leakage  

---

## Security Execution Cycle

1. Runtime sends a user action or system event to Security Family.
2. Mode Controller determines the active security mode.
3. Behavior Monitor analyzes the action and context.
4. Safety Rules Engine evaluates the action against security policies.
5. If the action is safe:
   - Operation Filter allows the action
   - return "allow" decision
6. If the action is unsafe:
   - Operation Filter blocks the action
   - return "deny" decision with security flags
7. Behavior Profile Manager updates long‑term behavior patterns.
8. Security Diagnostics Logger records the event.
9. Decision is returned to the Runtime.
10. System waits for the next security event.
