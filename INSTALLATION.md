# Install and test GAMA on Android

The published runtime release is [v3.4.0](https://github.com/richardpizem-ctrl/SIRIUS-LOCAL-AI-GAMA/releases/tag/v3.4.0). The Android debug app built from `main` has its own package version, **0.1.3**.

## Install the test APK

1. Obtain `siriusgama-0.1.3-arm64-v8a-debug.apk` from the maintainer or build it below.
2. Copy the APK to your ARM64 Android phone and open it from the Files app.
3. Launch **SIRIUS GAMA** and follow the [offline test guide](docs/ANDROID-OFFLINE-TESTING.md).

## Build a debug APK from source

Use a Linux or WSL environment with Buildozer and its Android toolchain available. Run these commands from the repository root:

```bash
buildozer android debug
ls -1 bin/*.apk
```

[`buildozer.spec`](buildozer.spec) defines the package version, ARM64 build, SDK/NDK settings, Python and Kivy requirements, and which source files are included. The expected filename for this configuration is `siriusgama-0.1.3-arm64-v8a-debug.apk`.

## Run the runtime smoke test

From the repository root:

```bash
PYTHONPATH=. python tests/mobile_smoke_test.py
```

The smoke test supplies a dummy vision engine. Use the on-device guide to reproduce the verified offline knowledge queries. A native iOS packaging workflow is outside this guide.
