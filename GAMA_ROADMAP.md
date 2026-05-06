# 🚀 SIRIUS LOCAL AI GAMA – Roadmap

## GAMA 1.0 (Initial Release)
- Mobile Runtime Core  
- NL Router Mobile  
- Knowledge Packs Mobile  
- Vision Engine (OCR)  
- Schoolwork Mode Mobile  
- SECURITY FAMILY Mobile  

---

## GAMA 1.1 (Upcoming Enhancements)

### 🟪 1) Priority Score pre Knowledge Packs
- nové pole v metadata.json: `"priority": 0.0 – 1.0`
- umožní preferovať špecializované packy pred všeobecnými
- deterministické rozhodovanie pri PACK_LOOKUP
- fallback mechanizmus pri rovnakom skóre
- zlepšená presnosť odpovedí bez NLP klasifikácie

### 🟦 2) Native Image Preprocessing (Android/iOS)
**Android (CameraX / ML Kit):**
- auto-focus  
- auto-exposure  
- auto-white balance  
- document detection  
- perspective correction  
- stabilization  

**iOS (VisionKit / AVFoundation):**
- VNDocumentCameraViewController  
- auto-crop  
- auto-enhance  
- auto-deskew  
- noise reduction  

**Výsledok:**
- vyššia presnosť OCR  
- nižšia záťaž CPU  
- rýchlejšie spracovanie  
- čistejší vstup pre Vision Engine  

### 🟩 3) Vylepšenia Vision Engine Pipeline
- natívny preprocessing → GAMA Vision Engine → OCR → Reasoning  
- optimalizácia pre ARM  
- zníženie šumu a chýb v textoch  

### 🟧 4) Knowledge Pack Spec 2.0
- rozšírený metadata formát  
- kategorizácia packov  
- priority routing  
- príprava na Knowledge Graphs (GAMA 3.0)

---

## GAMA 2.0
- LAN Offline Bridge  
- Device Diagnostics Mobile  
- Scene Understanding  
- Workflow Engine Mobile 2.0  
- Health Assistant 2.0 (NEW)  
  - offline zdravotnícky modul  
  - OCR zdravotných dokumentov  
  - rozpoznávanie liekov a dávkovania  
  - prvá pomoc a triage logika  
  - rodinne bezpečné zdravotné odporúčania  
  - 100 % offline spracovanie  

---

## GAMA 3.0
- Full Mobile Reasoning Engine  
- Advanced Knowledge Graphs  
- Multi‑intent routing  
- Complete offline autonomy  

---

## GAMA 4.0 (Hybrid‑Safe Architecture)

### 🟪 Secure Online Envoy (Isolated Online Agent)
- sandboxovaný online agent  
- jednosmerný outbound prístup na internet  
- získavanie textu, JSON, štruktúrovaných dát  
- žiadny prístup k súborom, modelom ani systémovým API  
- žiadne odosielanie lokálnych dát von  
- funguje ako kuriér, nie ako súčasť AI

### 🟩 Quarantine Pipeline (Data Sanitization Layer)
- odstránenie skriptov a HTML  
- validácia formátu  
- kontrola veľkosti  
- čistenie textu  
- bezpečnostné filtre  
- povolené len: čistý text, JSON, štruktúrované dáta  
- offline jadro nikdy nepríde do kontaktu s nečistými dátami

### 🟧 Offline Core Remains Fully Air‑Gapped
- inference offline  
- reasoning offline  
- knowledge packs offline  
- žiadne cloudové volania  
- žiadna telemetria  
- žiadne odosielanie dát  

### 🟦 Why This Matters
- offline AI zostáva offline  
- používateľ má 100% súkromie  
- AI môže pracovať s aktuálnymi dátami  
- architektúra je bezpečná, modulárna, enterprise‑grade  
- rovnaký model ako air‑gapped systémy v kritickej infraštruktúre
