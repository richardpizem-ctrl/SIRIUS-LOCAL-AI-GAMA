# 🧩 GAMA Knowledge Packs

Knowledge Packs provide offline knowledge modules used by the GAMA Runtime and NL Router.

---

# 🎯 Purpose
- enable offline reasoning  
- provide structured knowledge  
- support schoolwork mode  
- enhance general assistant capabilities  
- reduce dependency on online sources  
- ensure deterministic, explainable reasoning  
- allow modular domain expansion  

---

# 🗂 Types of Knowledge Packs
- math  
- language  
- science  
- history  
- geography  
- general knowledge  
- logic & reasoning  
- safety & rules  
- custom user packs  

---

# 🏗 Structure
Each pack contains:

- **metadata.json** — pack info, version, subject, language  
- **knowledge.json** — structured facts, definitions, formulas  
- **rules.json** — logic rules, transformations, validation  
- **examples.json** — demonstrations, patterns, similarity samples  

---

# 🏷 Version
**GAMA Knowledge Packs — v1.0.0**  
(fully compatible with Runtime 2.0.0 and prepared for 3.0.0‑pre)

---

# 🔄 Knowledge Pack Flow

1. Runtime requests a knowledge pack based on task category.  
2. Pack Loader checks if the pack exists locally.  
3. If missing, fallback pack is used.  
4. metadata.json is parsed to identify pack type and version.  
5. knowledge.json is loaded into memory.  
6. rules.json is applied to structure reasoning.  
7. examples.json is used for pattern matching.  
8. Pack returns structured knowledge to the Runtime.  
9. Runtime uses the knowledge to complete the task.  
10. Diagnostics log the pack usage.  

---

# 🧩 Knowledge Pack Components

## 1. Pack Loader
Responsible for loading packs from local storage.
- path resolution  
- version checking  
- fallback handling  
- memory caching  
- pack integrity validation (NEW)  
- pack compatibility check for Runtime 3.x (NEW)  

## 2. Metadata Parser
Reads metadata.json and extracts:
- pack type  
- version  
- subject  
- language  
- dependencies  
- minimum runtime version (NEW)  
- pack priority (NEW)  

## 3. Knowledge Engine
Processes knowledge.json.
- structured facts  
- definitions  
- formulas  
- timelines  
- entities  
- domain‑specific schemas (NEW)  

## 4. Rule Engine
Applies rules.json to guide reasoning.
- pattern matching  
- logic rules  
- transformation rules  
- validation rules  
- rule chaining (NEW)  
- rule priority (NEW)  

## 5. Example Engine
Uses examples.json for:
- demonstrations  
- pattern inference  
- similarity matching  
- offline reasoning support  
- example‑based fallback reasoning (NEW)  

## 6. Diagnostics Logger
Tracks pack usage.
- pack name  
- version  
- load time  
- errors  
- fallback usage  
- rule hits (NEW)  
- example hits (NEW)  

---

# 🔁 Knowledge Pack Execution Cycle

1. Runtime requests a specific knowledge pack.  
2. Pack Loader locates the pack in local storage.  
3. Metadata Parser reads metadata.json.  
4. Knowledge Engine loads knowledge.json into memory.  
5. Rule Engine applies rules.json to guide reasoning.  
6. Example Engine loads examples.json for pattern matching.  
7. Pack compiles structured knowledge output.  
8. Output is returned to the Runtime.  
9. Diagnostics Logger records pack usage.  
10. System waits for the next pack request.  

---

# 🟪 NEW IN VERSION 2 → PREPARED FOR VERSION 3
- pack validation  
- pack priority  
- runtime compatibility flags  
- rule chaining  
- example‑based fallback  
- diagnostics expansion  
- unified PACK_QUERY event  
- unified PACK_INFO event  
- auto‑load support  
- pack integrity checks  
