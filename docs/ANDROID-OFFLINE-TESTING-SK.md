# GAMA na Androide a plán prepojenia s BETA cez ENVOY

[English version](ANDROID-OFFLINE-TESTING.md)

Tento návod je pre testerov SIRIUS LOCAL AI. Opisuje overenie lokálnych znalostných dotazov v GAMA na Androide a plánovaný spôsob, akým by sa mobilná GAMA mohla cez ENVOY pýtať desktopovej BETA.

## Čo si pripraviť

- Android telefón s architektúrou ARM64 a lokálny testovací súbor `siriusgama-0.1.3-arm64-v8a-debug.apk` od správcu projektu.
- Označenie **0.1.3** patrí lokálnemu Android APK. Označenie **v3.4.0** na stránke [GAMA Releases](https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-GAMA/releases/tag/v3.4.0) patrí vydaniu runtime. Tento návod nepridáva APK do GitHub Releases.
- Testovací balík o vode bol overený v lokálnom projekte. Súbor `gama_water_kg.json` v čase písania nebol dostupný na predvolenej vetve repozitára. Pri reprodukcii použite uvedené APK alebo zodpovedajúce lokálne zdroje.

## Offline test GAMA

1. Nainštalujte APK. Zapnite režim lietadlo a vypnite Wi‑Fi.
2. Otvorte **SIRIUS GAMA**, zadajte otázku a stlačte **Opýtať sa**.
3. Porovnajte odpoveď a zobrazený zdroj s tabuľkou.

| Otázka | Očakávaný výsledok | Overenie |
| --- | --- | --- |
| Pri akej teplote mrzne čistá voda? | **0 °C**. Zdroj USGS Water Science School. | Android 0.1.3 offline a terminál |
| Čo vytvára jednorožec? | Správa, že aplikácia v školskom balíku nenašla odpoveď. | Android 0.1.3 offline a terminál |
| Pri akej teplote vrie voda pri normálnom atmosférickom tlaku? | **100 °C pri normálnom atmosférickom tlaku**. Zdroj USGS. | Terminál overil variant bez slova „voda“ |
| Čo vzniká pri kondenzácii vodnej pary? | **Kvapalná voda**. Zdroj NOAA. | Terminál overil variant bez diakritiky |
| Čo vytvára fotosyntéza? | **Kyslík a cukry**. Pri oboch výsledkoch sa zobrazí zdroj zo základného školského balíka GAMA. | Terminál pre 0.1.3 a Android 0.1.2 offline |

Výsledok z **15. novembra 2026** pre oba scenáre na telefóne s APK 0.1.3 je **PASS**. Do hlásenia uveďte verziu APK, zariadenie a verziu Androidu, stav pripojenia, presnú otázku, výsledok a zobrazený zdroj. Tento test je jedným podkladom pre [integračné issue GAMA #42](https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-GAMA/issues/42).

Zdroje balíka o vode: [USGS Water Science School](https://doi.org/10.3133/gip219) a [NOAA Water Cycle Activity](https://www.nesdis.noaa.gov/s3/2023-02/WaterCycleActivity-FullManual.pdf).

## Úloha BETA a ENVOY

[GAMA](https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-GAMA) používa mobilný runtime a lokálne znalostné balíky. [BETA Windows Preview v6.1.0](https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-BETA#readme) má samostatný slovenský a anglický znalostný graf. Keď lokálny dotaz v BETA odpoveď nenájde, používateľ môže schváliť voliteľné webové vyhľadávanie cez ENVOY.

README BETA uvádza **prepojenie GAMA a BETA cez ENVOY ako budúci míľnik**. Ako prvý spoločný test navrhujeme jeden dotaz z GAMA do lokálneho grafu BETA:

1. GAMA skúsi odpovedať z vlastných balíkov. Ak odpoveď chýba, používateľ môže schváliť jeden dotaz do BETA.
2. Po schválení ENVOY odošle dotaz na čítanie. BETA vráti výsledok zo svojho lokálneho grafu a zdroj, ak je pri fakte uložený.
3. Test pokryje aj odmietnutie a nedostupnú BETA. Pri odmietnutí sa požiadavka neodošle. Pri nedostupnej BETA aplikácia oznámi stav. Prvý spoločný scenár nevyužíva webové vyhľadávanie ani zápis do grafov.

Týmto testom sa má overiť plánované prepojenie. Výsledok Androidu 0.1.3 pokrýva vyššie uvedené lokálne scenáre.
