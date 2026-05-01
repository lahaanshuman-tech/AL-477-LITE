# AL-477 Lite Specification

This document defines the algorithmic specification for AL‑477 Lite.  
It is language‑agnostic and intended to guide collaborators porting the Lite version to other languages (Java, Rust, Go, C, C++, C#, JS, TS, etc.).

---

## 🔧 Overview
AL‑477 Lite is an educational encoder/decoder library. It demonstrates:
- Payload chunking
- Recipe generation
- Random signature embedding
- Layered Base64 encoding
- Systematic decoding of payload, recipe, and signature

---

## 🔄 Encoding Flow
1. **Input Payload**: Accept a string payload.
2. **Chunk Payload**: Split into manageable segments.
3. **Generate Recipe**: Record chunking details.
4. **Generate Signature**: Create a random signature string.
5. **Embed Signature**: Append signature to payload.
6. **Combine**: Payload + recipe + signature.
7. **Base64 Encode**: Encode the combined string.

---

## 🔄 Decoding Flow
1. **Base64 Decode**: Decode the input string.
2. **Extract Components**: Separate payload, recipe, and signature.
3. **Reconstruct Payload**: Use recipe to rebuild original payload.
4. **Return**: Payload, recipe, signature.

---

## 📦 Public API
- `encode_payload(input: str) -> str`  
  Returns encoded string containing payload, recipe, and signature.

- `decode_payload(encoded: str) -> (payload: str, recipe: str, signature: str)`  
  Returns decoded payload, recipe, and signature.

---

## ⚠️ Disclaimer
AL‑477 Lite is **educational only**.  
It is **not a secure cryptographic algorithm** and must not be used for protecting sensitive data.

---

## 📂 Reference Implementation
- Python package: `al477lite`
- Files:
  - `al477_encoder.py`
  - `al477_decoder.py`
  - `__init__.py`
  - `main.py`
