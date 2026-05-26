# 📦 SIRIUS LOCAL AI GAMA – Installation Guide  
**Version:** 3.2.0  
**Platform:** Android / iOS  
**Runtime:** 100% offline, modular, privacy‑first  
**Architecture:** Fully aligned with Runtime 3.2, Event Engine 3.2, VisionEngineV3, Hybrid‑Safe Pipeline 3.2

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
- SIRIUS Local AI Core Runtime 3.2  
- VisionEngineV3 (optional)  
- Knowledge Packs 3.2 (optional)  
- Embedded Python modules (bundled)  
- Hybrid‑Safe Pipeline 3.2  

---

# 📥 Installation (Android)

## 1. Download APK
From GitHub Releases:

```
Releases → SIRIUS LOCAL AI GAMA → Assets → *.apk
```

## 2. Enable Unknown Sources
Android → Settings → Security → *Install unknown apps*

## 3. Install the App
Open the APK → Install

## 4. First Launch
The app will automatically:
- initialize Runtime Core 3.2  
- load all modules  
- create the local context  
- start NL Router 3.2  
- enable Hybrid‑Safe Pipeline  

---

# 🍏 Installation (iOS)

## 1. Open the project in Xcode
```
File → Open → SIRIUS-LOCAL-AI-GAMA
```

## 2. Configure Signing
Xcode → Signing & Capabilities → Team → your Apple ID

## 3. Build & Run
Select your device → Run

## 4. First Launch
iOS will automatically create:
- secure local storage  
- runtime context  
- VisionEngineV3 pipeline (if enabled)  
- hybrid‑safe sandbox  

---

# 📚 Installing Knowledge Packs (v3.2)

## 1. Copy packs into:
```
/packs/
```

## 2. Restart the app  
Pack Manager v3.2 will auto‑load them.

## 3. Verify installation  
Inside the app:

```
lookup: packs
```

---

# 👁 Installing VisionEngineV3 (OCR / Scene / Homework)

## 1. Copy model files into:
```
/vision/models/
```

## 2. Enable Vision in config
Edit `runtime_config.json`:

```json
{
  "vision_enabled": true,
  "vision_engine": "v3"
}
```

## 3. Restart the app  
VisionEngineV3 will initialize with:
- OCR v3.2  
- Scene v3.2  
- Homework detection v3.2  
- Hybrid‑Safe sandbox  

---

# 🧪 Smoke Test (optional)

Run:

```bash
python tests/mobile_smoke_test.py
```

Expected output:

```
OCR RESULT: ok
Hybrid-Safe: ok
Smoke test passed.
```

---

# 🛠 Troubleshooting (v3.2)

| Issue | Solution |
|-------|----------|
| VisionEngineV3 not detected | Check `/vision/models/` + restart |
| Packs not loading | Check `/packs/` + restart |
| Runtime crash | Delete `runtime_state/` |
| OCR not working | Missing model or camera permission |
| Hybrid‑Safe block | Check quarantine logs in `/logs/hybrid_safe/` |

---

# 🧩 Additional Documentation (3.2)

- `README.md` – Overview  
- `ARCHITECTURE_3.2.md` – System design  
- `RUNTIME_3.2.md` – Runtime internals  
- `SECURITY_3.2.md` – Security Engine  
- `VISION_3.2.md` – VisionEngineV3  
- `EVENTS_3.2.md` – Event Types 3.2  
- `KNOWLEDGE_PACKS_3.2.md` – Pack system  
- `CHANGELOG.md` – Version history  

---

# 🏁 Done

SIRIUS LOCAL AI GAMA 3.2 is now fully installed and ready to run.  
100% offline. 100% secure. 100% yours.
