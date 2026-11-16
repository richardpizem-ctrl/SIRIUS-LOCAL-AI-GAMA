# GAMA Android offline testing and the BETA–ENVOY integration plan

[Slovenská verzia](ANDROID-OFFLINE-TESTING-SK.md)

This guide helps testers reproduce local knowledge queries in SIRIUS GAMA for Android. It also describes how GAMA could query the desktop BETA knowledge graph through ENVOY.

## Get the test build

Use an ARM64 Android phone and obtain `siriusgama-0.1.3-arm64-v8a-debug.apk` from the project maintainer. **0.1.3** is the version of the local Android test build. **v3.4.0** identifies the published [GAMA runtime release](https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-GAMA/releases/tag/v3.4.0). The tested water pack, `gama_water_kg.json`, was part of the local Android build. To reproduce the test, use that APK or [build it from main](../INSTALLATION.md#build-a-debug-apk-from-source). The water pack and Android version update landed in [PR #49](https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-GAMA/pull/49).

## Run the offline test

1. Install the APK, enable airplane mode, and turn off Wi-Fi.
2. Open **SIRIUS GAMA**, enter one of the Slovak questions below, and tap **Opýtať sa** (Ask).
3. Compare the response and displayed source with the expected result.

| Enter this Slovak question | Meaning | Expected result | Verified in |
| --- | --- | --- | --- |
| Pri akej teplote mrzne čistá voda? | At what temperature does pure water freeze? | **0 °C**, with USGS Water Science School as the source. | Android 0.1.3 offline and terminal |
| Čo vytvára jednorožec? | What does a unicorn produce? | A message saying the school pack has no answer. | Android 0.1.3 offline and terminal |
| Pri akej teplote vrie pri normálnom atmosférickom tlaku? | At what temperature does water boil at standard atmospheric pressure? | **100 °C** at standard atmospheric pressure, with USGS as the source. | Terminal |
| Co vznika pri kondenzacii vodnej pary? | What forms when water vapor condenses? | **Kvapalná voda** (liquid water), with NOAA as the source. | Terminal |
| Čo vytvára fotosyntéza? | What does photosynthesis produce? | **Kyslík** (oxygen) and **cukry** (sugars), both attributed to the GAMA school pack. | Terminal for 0.1.3 and Android 0.1.2 offline |

Both Android 0.1.3 scenarios passed offline on **15 November 2026**. When reporting a test, include the APK version, device and Android version, network state, exact question, response, and displayed source. These results cover the scenarios above and contribute to the broader [GAMA integration testing issue #42](https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-GAMA/issues/42).

Water pack sources: [USGS Water Science School](https://doi.org/10.3133/gip219) and [NOAA Water Cycle Activity](https://www.nesdis.noaa.gov/s3/2023-02/WaterCycleActivity-FullManual.pdf).

## How BETA and ENVOY fit in

GAMA uses local knowledge packs on mobile. [BETA Windows Preview v6.1.0](https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-BETA#readme) uses separate Slovak and English knowledge graphs on the desktop. If the local graph has no answer, BETA can offer an optional web lookup through ENVOY, subject to user approval.

The BETA roadmap lists **connecting GAMA and BETA through ENVOY as a future milestone**. The proposed first integration test is a single read-only query from GAMA to BETA:

1. GAMA queries its local packs. If it finds no answer, it asks the user to approve a query to BETA.
2. After approval, ENVOY sends the query. BETA returns a result from its local graph and includes the source when the stored fact has one.
3. Test both denial and an unreachable BETA instance. If the user denies the request, GAMA sends nothing. If BETA is unreachable, GAMA reports that state. The first test keeps web lookup and graph writes out of scope.

The Android 0.1.3 results above verify the local query path. The proposed cross-device test will verify the ENVOY path separately.
