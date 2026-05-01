# Porting Guide for AL-477 Lite

This document provides guidelines for porting AL‑477 Lite into other programming languages.  
The goal is to maintain algorithmic consistency while adapting to language‑specific idioms.

---

## 🔧 Reference Implementation
- Primary reference: Python package `al477lite`
- Files:
  - `al477_encoder.py`
  - `al477_decoder.py`
  - `__init__.py`
  - `main.py`

---

## 🔄 Core Algorithm
All ports must implement the following steps:

### Encoding
1. Accept input payload (string).
2. Chunk payload into segments.
3. Generate recipe describing chunking.
4. Generate random signature string.
5. Append signature to payload.
6. Combine payload + recipe + signature.
7. Base64 encode the combined string.

### Decoding
1. Base64 decode input string.
2. Separate payload, recipe, and signature.
3. Reconstruct payload using recipe.
4. Return payload, recipe, signature.

---

## 📦 Required API
Each port must expose:

- `encode_payload(input: str) -> str`  
  Returns encoded string containing payload, recipe, and signature.

- `decode_payload(encoded: str) -> (payload: str, recipe: str, signature: str)`  
  Returns decoded payload, recipe, and signature.

---

## 🌐 Language-Specific Notes
- **Java**:  
  - Use `Base64` from `java.util` for encoding/decoding.  
  - Organize into classes: `Encoder`, `Decoder`, `Main`.  
  - Provide a menu‑driven CLI for testing.

- **C**:  
  - Use standard libraries for string manipulation.  
  - Implement Base64 manually or via lightweight library.  
  - Focus on memory safety and buffer management.

- **Rust**:  
  - Use `base64` crate.  
  - Implement payload/recipe/signature as structs.  
  - Ensure strong typing for clarity.

- **Go**:  
  - Use `encoding/base64` package.  
  - Keep functions simple and idiomatic.  
  - Provide a command‑line interface for demo.

---

## 📑 Documentation
Each port must include:
- `README.md` with usage examples.
- `SPEC.md` reference to algorithm flow.
- `CHANGELOG.md` noting differences from Python version.
- `CONTRIBUTING.md` updated with porting notes.

---

## ⚠️ Disclaimer
AL‑477 Lite is **educational only**.  
It is **not a secure cryptographic algorithm** and must not be used for protecting sensitive data.

---

## ✅ Checklist for Port Maintainers
- [ ] Implement encoding and decoding flow.  
- [ ] Match API signatures.  
- [ ] Add documentation and examples.  
- [ ] Test against Python reference outputs.  
- [ ] Update `CHANGELOG.md` with port details.  
