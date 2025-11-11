#!/usr/bin/env bash
set -euo pipefail

RUST_FILE=${1:-examples/hello.rs}
CPP_FILE=out.cpp
ASM_FILE=out.asm
BIN_FILE=out

echo "⚙️ Transpiling $RUST_FILE → C++"
python3 transpile_rust_to_cpp.py "$RUST_FILE" > "$CPP_FILE"

echo "⚙️ Compiling $CPP_FILE → NASM (assembly)"
g++ -S -masm=intel "$CPP_FILE" -o "$ASM_FILE"

echo "⚙️ Assembling & Linking"
g++ "$CPP_FILE" -o "$BIN_FILE"

echo "✅ Done. Run ./out or open $ASM_FILE"
