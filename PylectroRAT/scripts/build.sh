

#!/bin/bash

# Build script for PlectroRAT
# This script prepares the payload for distribution

set -e

BUILD_DIR="build"
SRC_DIR="../src"

echo "[*] Cleaning up previous builds..."
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

echo "[*] Copying source files..."
cp -R "$SRC_DIR"/* "$BUILD_DIR"

echo "[*] Creating zip archive..."
cd "$BUILD_DIR"
zip -r plectro_payload.zip . > /dev/null
cd ..

echo "[*] Build complete. Output in $BUILD_DIR/plectro_payload.zip"