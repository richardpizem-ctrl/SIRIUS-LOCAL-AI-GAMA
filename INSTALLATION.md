# 📦 SIRIUS LOCAL AI GAMA – Installation Guide  
**Version:** 3.4.0  
**Platform:** Android / iOS  
**Runtime:** 100% offline, modular, privacy‑first  
**Architecture:** Fully aligned with Runtime 3.4, Event Engine 3.4, VisionEngineV3, Hybrid‑Safe Pipeline 3.4

---

# 🔧 Requirements

## Mobile OS
- Android 8.0+
- iOS 14+

## Hardware
- CPU: ARM64  
- RAM: 2 GB minimum (4 GB recommended)  
- Storage: 50–250 MB depending on installed packs  

## Runtime Dependencies
- SIRIUS Local AI Core Runtime 3.4  
- VisionEngineV3 (optional)  
- Knowledge Packs 3.4 (optional)  
- Embedded Python modules (bundled)  
- Deterministic Event Engine 3.4  
- Hybrid‑Safe Pipeline 3.4

---

# 📥 Installation Steps

## 1. Download the GAMA Package
Download the latest **SIRIUS LOCAL AI GAMA 3.4.0** release from the official repository.  
The package includes:
- `/runtime/` – Core Runtime 3.4  
- `/vision/` – VisionEngineV3  
- `/packs/` – Knowledge Packs 3.4  
- `/config/` – System configuration  
- `/python/` – Embedded Python modules  

## 2. Extract the Package
Unzip the downloaded archive into your device’s application directory.  
All modules are self‑contained and require no internet access.

## 3. Grant Local Permissions
To ensure full offline functionality:
- Enable local storage access  
- Enable camera access (for VisionEngineV3)  
- Disable battery optimization (recommended)

No network permissions are required.

## 4. Launch the Runtime
Start the app.  
The system automatically:
- Loads Runtime 3.4  
- Initializes Event Engine 3.4  
- Activates Hybrid‑Safe Pipeline  
- Registers VisionEngineV3 (if installed)  
- Loads Knowledge Packs 3.4  

Startup time: **0.2–0.6 s** depending on device.

---

# 🧩 Optional Components

## VisionEngineV3
Enables:
- Deterministic OCR  
- Homework extraction  
- Safe semantic metadata  
- Vision Flow v3 scenes  

## Knowledge Packs 3.4
Add domain‑specific reasoning:
- Math  
- Languages  
- Schoolwork  
- Family Safety  
- Local Rules  

## Security Engine 3.4
Provides:
- SchoolMode v2  
- StrangerMode v2  
- TimeLimits v2  
- Family Behavior Rules  
- Optional Health Assistant v1.1  

---

# 📚 Documentation Included
- `RUNTIME_3.4.md` – Core Runtime  
- `SECURITY_3.4.md` – Security Engine  
- `VISION_3.4.md` – VisionEngineV3  
- `EVENTS_3.4.md` – Event Types 3.4  
- `KNOWLEDGE_PACKS_3.4.md` – Pack system  
- `CHANGELOG.md` – Version history  

---

# 🏁 Done
SIRIUS LOCAL AI GAMA 3.4 is now fully installed and ready to run.  
100% offline. 100% secure. 100% yours.
