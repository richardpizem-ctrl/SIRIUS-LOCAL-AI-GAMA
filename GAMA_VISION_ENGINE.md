# 🔍 GAMA Vision Engine (OCR)

The Vision Engine provides offline OCR and image understanding for GAMA.

---

# 🎯 Responsibilities
- text extraction from images  
- document scanning  
- math OCR  
- handwriting support (basic)  
- preprocessing and cleanup  
- scene context detection (NEW)  
- OCR quality scoring (NEW)  
- hybrid input merging (NEW)  
- deterministic image pipeline (NEW)  

---

# 📝 Input Types
- photos  
- screenshots  
- scanned documents  
- camera frames (live capture) (NEW)  
- hybrid inputs (image + text) (NEW)  

---

# 📤 Output
- extracted text  
- structured OCR blocks  
- confidence scores  
- OCR quality metadata (NEW)  
- detected content type (math / text / mixed) (NEW)  

---

# 🏷 Version
**GAMA Vision Engine — v1.0.0**  
(prepared for Vision 2.0 and Runtime 3.0.0‑pre)

---

# 🔄 Vision Engine Flow

1. Receive image input from the Runtime.  
2. Preprocess the image:  
   - resize  
   - denoise  
   - contrast enhancement  
   - grayscale conversion  
   - auto‑deskew (NEW)  
   - perspective correction (NEW)  
   - document boundary detection (NEW)  
3. Detect text regions.  
4. Run OCR on detected regions.  
5. Parse OCR output into structured blocks.  
6. Apply math OCR rules (if math content detected).  
7. Apply handwriting heuristics (basic support).  
8. Merge hybrid inputs if text + OCR present (NEW).  
9. Generate final OCR result with confidence scores.  
10. Add OCR quality score + metadata (NEW).  
11. Return structured OCR output to the Runtime.  
12. Log OCR event for diagnostics.  

---

# 🧩 Vision Engine Components

## 1. Image Preprocessor
Handles all image cleanup before OCR.
- resizing  
- denoising  
- sharpening  
- grayscale conversion  
- contrast enhancement  
- auto‑deskew (NEW)  
- perspective correction (NEW)  
- document detection (NEW)  
- native preprocessing support (Android/iOS) (NEW)  

## 2. Text Region Detector
Finds areas in the image that contain text.
- bounding box detection  
- region segmentation  
- noise filtering  
- multi‑scale region detection (NEW)  
- math‑region detection (NEW)  

## 3. OCR Core
Performs the actual text recognition.
- character recognition  
- line grouping  
- block segmentation  
- confidence scoring  
- ARM‑optimized OCR pipeline (NEW)  
- fallback OCR mode for low‑quality images (NEW)  

## 4. Math OCR Engine
Specialized logic for mathematical expressions.
- symbol detection  
- formula reconstruction  
- layout interpretation  
- fraction + exponent parsing (NEW)  
- equation normalization (NEW)  

## 5. Handwriting Heuristics
Basic support for handwritten text.
- stroke pattern detection  
- heuristic matching  
- fallback recognition  
- handwriting confidence scoring (NEW)  

## 6. Output Formatter
Converts raw OCR output into structured blocks.
- paragraphs  
- lines  
- tokens  
- confidence metadata  
- OCR quality score (NEW)  
- detected content type (NEW)  

## 7. Diagnostics Logger
Tracks OCR events.
- preprocessing steps  
- detected regions  
- recognition accuracy  
- errors and fallbacks  
- OCR quality score (NEW)  
- math detection logs (NEW)  
- handwriting detection logs (NEW)  

---

# 🔁 Vision Engine Execution Cycle

1. Runtime sends an image to the Vision Engine.  
2. Image Preprocessor cleans and normalizes the image.  
3. Text Region Detector identifies areas containing text.  
4. OCR Core performs text recognition on detected regions.  
5. Math OCR Engine processes mathematical expressions (if detected).  
6. Handwriting Heuristics attempt recognition of handwritten text.  
7. Hybrid input merging (if text + OCR present).  
8. Output Formatter structures the OCR result into blocks.  
9. Final OCR output is returned to the Runtime.  
10. Diagnostics Logger records the OCR event.  
11. Vision Engine waits for the next image input.  

---

# 🟪 NEW IN VERSION 2 → PREPARED FOR VERSION 3.0.0‑pre
- native preprocessing (Android/iOS)  
- auto‑deskew + perspective correction  
- document boundary detection  
- hybrid input merging  
- OCR quality scoring  
- math‑region detection  
- handwriting confidence scoring  
- fallback OCR mode  
- extended diagnostics  
- unified VISION_ANALYZE event  
