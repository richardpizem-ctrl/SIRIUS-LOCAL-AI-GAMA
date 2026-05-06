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

---

## GAMA 3.0
- Full Mobile Reasoning Engine  
- Advanced Knowledge Graphs  
- Multi‑intent routing  
- Complete offline autonomy
