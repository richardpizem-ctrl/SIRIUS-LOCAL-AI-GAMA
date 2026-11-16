# SIRIUS LOCAL AI GAMA

GAMA is the mobile runtime in the SIRIUS LOCAL AI project. Its Android debug app answers supported Slovak questions from local knowledge packs and displays the source of each stored fact. The runtime repository also contains components for structured events, Vision Flow and schoolwork reasoning.

| What | Version and status |
| --- | --- |
| Published runtime | [v3.4.0 release](https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-GAMA/releases/tag/v3.4.0) |
| Android test build on `main` | **0.1.3**, ARM64 debug APK. Two offline scenarios were verified on a physical phone. |
| BETA integration | A GAMA-to-BETA query through ENVOY is a planned integration test. |
| iOS | The mobile architecture includes iOS as a target. This guide provides a verified test path for Android. |

## Quick Start

1. Obtain `siriusgama-0.1.3-arm64-v8a-debug.apk` from the maintainer or follow the [build instructions](INSTALLATION.md).
2. Install it on an ARM64 Android phone, enable airplane mode and turn off Wi-Fi.
3. Open **SIRIUS GAMA**, enter **Pri akej teplote mrzne čistá voda?**, and tap **Opýtať sa**. Expect **0 °C** with USGS Water Science School as the source.
4. See the [English tester guide](docs/ANDROID-OFFLINE-TESTING.md) or [slovenský návod](docs/ANDROID-OFFLINE-TESTING-SK.md) for the full test cases and expected outcomes.

## Documentation

| Topic | Start here |
| --- | --- |
| Architecture and code locations | [Architecture](GAMA_ARCHITECTURE.md), [folder structure](GAMA_FOLDER_STRUCTURE.md), [module map](GAMA_MODULE_MAP.md) |
| Runtime and input | [Runtime](GAMA_RUNTIME.md), [natural-language router](GAMA_NL_ROUTER.md) |
| Local content | [Knowledge packs](GAMA_KNOWLEDGE_PACKS.md), [knowledge graphs](GAMA_KNOWLEDGE_GRAPHS.md) |
| OCR and schoolwork | [Vision Engine](GAMA_VISION_ENGINE.md), [Schoolwork Mode](GAMA_SCHOOLWORK_MODE.md) |
| Security and contributions | [Security policy](SECURITY.md), [security tutorial](SECURITY_TUTORIAL.md), [Security Family](GAMA_SECURITY_FAMILY.md), [contributing](CONTRIBUTING.md), [code of conduct](CODE_OF_CONDUCT.md) |
| Project status | [Changelog](CHANGELOG.md), [roadmap](GAMA_ROADMAP.md), [project vision](GAMA_VISION.md), [historical milestone](GAMA_MILESTONE_3.0.0-PRE_SUMMARY.md) |

[BETA Windows Preview](https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-BETA) uses its own local knowledge graphs and offers optional web lookups through ENVOY with user approval. The [Android guide](docs/ANDROID-OFFLINE-TESTING.md#how-beta-and-envoy-fit-in) describes the proposed first cross-device test. Follow [issue #42](https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-GAMA/issues/42) for the broader integration work.

## Project identity and license

SIRIUS LOCAL AI GAMA is independent software. It has no connection to Hengbot's Sirius robot, the GAMA Simulation Platform, or similarly named hardware products. The project is distributed under the [MIT License](LICENSE).
