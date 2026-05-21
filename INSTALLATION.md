# 📦 SIRIUS LOCAL AI GAMA – Installation Guide
**Version:** 3.1.0  
**Platform:** Android / iOS  
**Runtime:** 100% offline, modular, privacy‑first

---

## 🔧 Requirements

### **Mobile OS**
- Android 8.0+
- iOS 14+

### **Hardware**
- CPU: ARM64
- RAM: 2 GB minimum (4 GB recommended)
- Storage: 50–200 MB depending on installed packs

### **Runtime Dependencies**
- SIRIUS Local AI Core Runtime
- Vision Engine (optional)
- Knowledge Packs (optional)
- Embedded Python modules (bundled in the app)

---

## 📥 Installation (Android)

### **1. Download APK**
Download the latest build from GitHub Releases:

```
Releases → SIRIUS LOCAL AI GAMA → Assets → *.apk
```

### **2. Enable Unknown Sources**
Android → Settings → Security → *Install unknown apps*

### **3. Install the App**
Open the APK → Install

### **4. First Launch**
The app will automatically:
- initialize the runtime
- load all modules
- create the local context
- start the NL Router

---

## 🍏 Installation (iOS)

### **1. Open the project in Xcode**
```
File → Open → SIRIUS-LOCAL-AI-GAMA
```

### **2. Configure Signing**
Xcode → Signing & Capabilities → Team → your Apple ID

### **3. Build & Run**
Select your iPhone/iPad → Run

### **4. First Launch**
iOS will automatically create:
- local storage
- runtime context
- vision pipeline (if enabled)

---

## 📚 Installing Knowledge Packs

### **1. Copy packs into:**
```
/packs/
```

### **2. Restart the app**
Pack Manager will auto‑load them.

### **3. Verify installation**
Inside the app, type:

```
lookup: packs
```

---

## 👁 Installing Vision Engine

### **1. Copy model files into:**
```
/vision/models/
```

### **2. Enable Vision in config**
Edit `runtime_config.json`:

```json
{
  "vision_enabled": true
}
```

### **3. Restart the app**

---

## 🧪 Smoke Test (optional)

Run:

```bash
python tests/mobile_smoke_test.py
```

Expected output:

```
OCR RESULT: ok
Smoke test passed.
```

---

## 🛠 Troubleshooting

| Issue | Solution |
|-------|----------|
| Vision Engine not detected | Check `/vision/models/` |
| Packs not loading | Check `/packs/` + restart |
| Runtime crash | Delete `runtime_state/` |
| OCR not working | Missing model or camera permission |

---

## 🧩 Additional Documentation

- `README.md` – Overview  
- `ARCHITECTURE.md` – System design  
- `RUNTIME.md` – Runtime internals  
- `SECURITY.md` – Security Engine  
- `VISION.md` – Vision Engine  
- `EVENTS.md` – Event Types 3.1.0  
- `CHANGELOG.md` – Version history  

---

## 🏁 Done

SIRIUS LOCAL AI GAMA is now fully installed and ready to run.  
100% offline. 100% secure. 100% yours.
