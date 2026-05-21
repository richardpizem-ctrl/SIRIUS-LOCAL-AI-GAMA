# 🧩 GAMA Knowledge Packs — Version 3.1.0

Knowledge Packs provide **offline structured knowledge modules** used by the GAMA Runtime, Unified Event System, Schoolwork Mode, and Reasoning Engine.  
Version **3.1.0** extends the 3.0 architecture with **PACK_SUGGEST**, improved deterministic routing,  
**Metadata v3.1**, stricter hybrid‑safe rules, and full compatibility with the **SIRIUS 3.1.x architecture**.

---

# 🎯 Purpose
- enable offline reasoning  
- provide structured, deterministic knowledge  
- support schoolwork mode  
- enhance general assistant capabilities  
- reduce dependency on online sources  
- ensure explainable, rule‑based reasoning  
- support hybrid reasoning (rules + examples)  
- integrate with unified event architecture 3.1  
- support pack priority and compatibility flags  
- support PACK_SUGGEST prefix search (new in 3.1)  

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

# 🏗 Structure (v3.1)
Each pack contains:

- **metadata.json** — pack info, version, subject, language, priority, compatibility flags, hybrid‑safe flags  
- **knowledge.json** — structured facts, definitions, formulas, timelines  
- **rules.json** — logic rules, transformations, validation, rule chaining  
- **examples.json** — demonstrations, patterns, similarity samples  

All components follow **Metadata v3.1** and **Pack Schema v3.1**.

---

# 🏷 Version
**GAMA Knowledge Packs — v3.1.0**  
(fully compatible with Runtime 3.1.0 and Unified Event Architecture 3.1.x)

---

# 🔄 Knowledge Pack Flow (v3.1.0)

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

# 🧩 Knowledge Pack Components (v3.1)

## 1. Pack Loader (v3.1)
Responsible for loading packs from local storage.

- path resolution  
- version checking  
- fallback handling  
- memory caching  
- pack integrity validation v3.1  
- pack compatibility flags  
- hybrid‑safe flags  
- auto‑load support  
- deterministic pack selection  
- PACK_SUGGEST prefix routing  

---

## 2. Metadata Parser (v3.1)
Reads metadata.json and extracts:

- pack type  
- version  
- subject  
- language  
- dependencies  
- minimum runtime version  
- pack priority (0.0 – 1.0)  
- compatibility flags v3.1  
- hybrid‑safe flags  
- deterministic routing hints  

---

## 3. Knowledge Engine (v3.1)
Processes knowledge.json.

- structured facts  
- definitions  
- formulas  
- timelines  
- entities  
- domain‑specific schemas  
- deterministic mapping  
- metadata v3.1 integration  
- hybrid‑safe filtering  

---

## 4. Rule Engine (v3.1)
Applies rules.json to guide reasoning.

- pattern matching  
- logic rules  
- transformation rules  
- validation rules  
- rule chaining v3.1  
- rule priority  
- hybrid reasoning support  
- Runtime 3.1 rule compatibility  
- deterministic rule selection  

---

## 5. Example Engine (v3.1)
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

## 6. Diagnostics Logger (v3.1)
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

---

# 🔁 Knowledge Pack Execution Cycle (v3.1.0)

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

# 🟪 NEW IN VERSION 3.1.0
- metadata v3.1  
- pack priority v3.1  
- compatibility flags v3.1  
- hybrid‑safe flags  
- PACK_SUGGEST (prefix search)  
- improved deterministic pack routing  
- unified result schema v3.1  
- rule chaining v3.1  
- example‑based fallback v3.1  
- diagnostics expansion v3.1  
- pack integrity checks v3.1  
- unified event architecture 3.1 integration  

---

# ✔ GAMA Knowledge Packs 3.1 — COMPLETE  
Fully aligned with the SIRIUS LOCAL AI GAMA 3.1.x ecosystem.
