import random
import base64
import secrets

def generate_signature(bits=256):
    """Generate a random signature (default 256-bit)."""
    sig_bytes = secrets.token_bytes(bits // 8)
    return base64.b64encode(sig_bytes).decode()

def chunk_payload(payload, seed=42):
    random.seed(seed)
    chunks = []
    i = 0
    while i < len(payload):
        size = random.choice([2, 4, 6])
        chunk = payload[i:i+size]
        chunks.append(chunk)
        i += size
    return chunks

def encode_recipe(recipe, signature):
    return base64.b64encode((recipe + signature).encode()).decode()

def encode_payload(payload):
    # Generate random signature each time
    signature = generate_signature()
    chunks = chunk_payload(payload)
    recipe = "|".join(chunks)
    encoded_recipe = encode_recipe(recipe, signature)

    # Embed signature directly into the combined string
    combined = payload + "::SEP::" + encoded_recipe + "::SIG::" + signature

    # Final obfuscation: encode whole thing again
    final_digest = base64.b64encode(combined.encode()).decode()
    return final_digest
