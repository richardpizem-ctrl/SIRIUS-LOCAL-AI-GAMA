# 🧩 GAMA Knowledge Packs — Version 3.2.0

Knowledge Packs provide **offline structured knowledge modules** used by the GAMA Runtime, Unified Event System, Schoolwork Mode, and Reasoning Engine.  
Version **3.2.0** extends the 3.1 architecture with **deterministic PACK routing**,  
**Metadata v3.2**, improved hybrid‑safe enforcement, PACK_SUGGEST refinements,  
and full compatibility with the **SIRIUS 3.2.x architecture**.

This version is aligned with **Runtime Mobile 3.2.0**, **Event Engine 3.2**,  
and the new **VisionEngineV3** pipeline.

---

# 🎯 Purpose
- enable offline reasoning  
- provide structured, deterministic knowledge  
- support schoolwork mode  
- enhance general assistant capabilities  
- reduce dependency on online sources  
- ensure explainable, rule‑based reasoning  
- support hybrid reasoning (rules + examples)  
- integrate with unified event architecture 3.2  
- support pack priority and compatibility flags  
- support PACK_SUGGEST prefix search  
- enforce hybrid‑safe metadata rules  
- ensure deterministic PACK routing  

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
- household & repairs  
- custom user packs  

---

# 🏗 Structure (v3.2)
Each pack contains:

- **metadata.json** — pack info, version, subject, language, priority, compatibility flags, hybrid‑safe flags  
- **knowledge.json** — structured facts, definitions, formulas, timelines  
- **rules.json** — logic rules, transformations, validation, rule chaining  
- **examples.json** — demonstrations, patterns, similarity samples  

All components follow **Metadata v3.2** and **Pack Schema v3.2**.

---

# 🏷 Version
**GAMA Knowledge Packs — v3.2.0**  
(fully compatible with Runtime 3.2.0 and Unified Event Architecture 3.2.x)

---

# 🔄 Knowledge Pack Flow (v3.2.0)

1. Runtime receives a PACK_QUERY or PACK_SUGGEST event.  
2. Pack Loader locates the requested pack.  
3. metadata.json is parsed (priority, version, compatibility, hybrid‑safe flags).  
4. knowledge.json is loaded into memory.  
5. rules.json is applied to structure reasoning.  
6. examples.json is used for fallback or hybrid reasoning.  
7. Pack compiles deterministic structured output.  
8. Output is returned via PACK_INFO event.  
9. Diagnostics log pack usage, rule hits, example hits, and metadata validation.  

---

# 🧩 Knowledge Pack Components (v3.2)

## 1. Pack Loader (v3.2)
Responsible for loading packs from local storage.

- path resolution  
- version checking  
- fallback handling  
- memory caching  
- pack integrity validation v3.2  
- pack compatibility flags  
- hybrid‑safe flags  
- auto‑load support  
- deterministic pack selection  
- PACK_SUGGEST prefix routing  
- improved PACK priority scoring  

---

## 2. Metadata Parser (v3.2)
Reads metadata.json and extracts:

- pack type  
- version  
- subject  
- language  
- dependencies  
- minimum runtime version  
- pack priority (0.0 – 1.0)  
- compatibility flags v3.2  
- hybrid‑safe flags  
- deterministic routing hints  
- PACK_SUGGEST optimization hints  

---

## 3. Knowledge Engine (v3.2)
Processes knowledge.json.

- structured facts  
- definitions  
- formulas  
- timelines  
- entities  
- domain‑specific schemas  
- deterministic mapping  
- metadata v3.2 integration  
- hybrid‑safe filtering  
- improved fallback logic  

---

## 4. Rule Engine (v3.2)
Applies rules.json to guide reasoning.

- pattern matching  
- logic rules  
- transformation rules  
- validation rules  
- rule chaining v3.2  
- rule priority  
- hybrid reasoning support  
- Runtime 3.2 rule compatibility  
- deterministic rule selection  

---

## 5. Example Engine (v3.2)
Uses examples.json for:

- demonstrations  
- pattern inference  
- similarity matching  
- offline reasoning support  
- example‑based fallback reasoning  
- hybrid reasoning (rules + examples)  
- deterministic fallback selection  
- PACK_SUGGEST prefix matching  

---

## 6. Diagnostics Logger (v3.2)
Tracks pack usage.

- pack name  
- version  
- load time  
- errors  
- fallback usage  
- rule hits  
- example hits  
- pack integrity status  
- metadata validation results  
- PACK_SUGGEST usage  
- hybrid‑safe compliance  
- PACK priority routing logs  

---

# 🔁 Knowledge Pack Execution Cycle (v3.2.0)

1. Runtime receives PACK_QUERY or PACK_SUGGEST.  
2. Pack Loader locates the pack.  
3. Metadata Parser reads metadata.json.  
4. Knowledge Engine loads knowledge.json.  
5. Rule Engine applies rules.json.  
6. Example Engine loads examples.json.  
7. Pack compiles structured output.  
8. PACK_INFO event is returned to Runtime.  
9. Diagnostics Logger records usage.  
10. System waits for the next PACK_QUERY or PACK_SUGGEST.  

---

# 🟪 NEW IN VERSION 3.2.0
- metadata v3.2  
- pack priority v3.2  
- compatibility flags v3.2  
- hybrid‑safe flags v3.2  
- improved PACK_SUGGEST prefix search  
- deterministic PACK routing v3.2  
- unified result schema v3.2  
- rule chaining v3.2  
- example‑based fallback v3.2  
- diagnostics expansion v3.2  
- pack integrity checks v3.2  
- unified event architecture 3.2 integration  
- full compatibility with Runtime Mobile 3.2.0  

---

# ✔ GAMA Knowledge Packs 3.2 — COMPLETE  
Fully aligned with the SIRIUS LOCAL AI GAMA 3.2.x ecosystem.
