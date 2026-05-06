# 🏥 SIRIUS LOCAL AI GAMA – Health Assistant 2.0
Offline zdravotnícky modul pre GAMA 2.0.0  
Zameraný na bezpečné, rodinné a súkromné použitie bez diagnostiky.

---

## 🎯 Poslanie modulu
Health Assistant 2.0 prináša do SIRIUS LOCAL AI GAMA schopnosti:
- spracovania zdravotných dokumentov offline,
- poskytovania bezpečných zdravotných informácií,
- pomoci pri prvej pomoci,
- práce s liekmi a dávkovaním,
- rodinne bezpečného zdravotného správania.

Modul **neposkytuje diagnózy** a je navrhnutý tak, aby bol 100 % offline a bezpečný.

---

## 🧩 Architektúra modulu

### Súčasti:
- **HealthAssistantEntry** – hlavný vstupný bod
- **Health Knowledge Packs** – špecializované dátové balíky
- **Health OCR Pipeline** – OCR pre zdravotné dokumenty
- **First Aid Logic** – bezpečné offline postupy prvej pomoci
- **Medication Info Engine** – informácie o liekoch a dávkovaní

---

## 🧬 Event Types (rozšírenie MobileEventTypes)

| Event Type | Účel |
|-----------|------|
| `HEALTH_QUERY` | všeobecné zdravotné otázky |
| `HEALTH_DOC_OCR` | OCR zdravotných dokumentov |
| `HEALTH_FIRST_AID` | prvá pomoc a bezpečnostné postupy |
| `HEALTH_MEDICATION_INFO` | informácie o liekoch a dávkovaní |

---

## 🏗 HealthAssistantEntry – správanie

### 1) OCR zdravotných dokumentov
- recepty  
- lekárske správy  
- dávkovanie  
- alergické karty  

### 2) Informácie o liekoch
- dávkovanie  
- upozornenia  
- interakcie (bez diagnostiky)  

### 3) Prvá pomoc
- krvácanie  
- popáleniny  
- dusenie  
- bezvedomie  
- bezpečnostné postupy  

### 4) Zdravotné znalosti
- vysvetlenie pojmov  
- bezpečné odporúčania  
- rodinné zdravotné informácie  

---

## 📦 Health Knowledge Pack (špecifikácia)

*(sem doplníš JSON podľa potreby — štruktúra je pripravená)*

---

## 🔒 Bezpečnostné zásady
- modul **neposkytuje diagnózy**, iba informácie,
- všetko prebieha **offline**,
- obsah je **deterministický**,
- vhodné pre rodiny, deti a seniorov,
- žiadne rizikové odporúčania.

---

## 🗺 Integrácia do GAMA 2.0
Health Assistant 2.0 je súčasťou:
GAMA 2.0
LAN Offline Bridge

Device Diagnostics Mobile

Scene Understanding

Workflow Engine Mobile 2.0

Health Assistant 2.0 (NEW)


