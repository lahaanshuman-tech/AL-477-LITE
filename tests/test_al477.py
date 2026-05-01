import hashlib
from Crypto.Cipher import AES
from al477lite.al477_encoder import encode_payload
from al477lite.al477_decoder import decode_payload

def run_tests():
    print("=== AL-477 Lite Test Harness ===")

    # Test payloads
    test_payloads = [
        "hello al-477",
        "",
        "ASDFgrirnfien = ilu= als477",
        "🔥unicode🔥",
        "1234567890"*5  # longer payload
    ]

    for p in test_payloads:
        print(f"\n--- Testing payload: {repr(p)} ---")

        # Encode
        encoded = encode_payload(p)
        print("[ENCODED]", encoded)

        # Decode
        try:
            decoded, recipe = decode_payload(encoded)
            assert decoded == p, f"Mismatch! Expected {p}, got {decoded}"
            print("[DECODED PAYLOAD]", decoded)
            print("[RECIPE]", recipe)
        except Exception as e:
            print("[DECODE ERROR]", e)

        # SHA check
        sha_out = hashlib.sha256(encoded.encode()).hexdigest()
        print("[SHA256 of encoded]", sha_out)

        # AES check (demo only: encrypts gibberish, doesn’t decode)
        key = b"thisisakey123456"  # 16 bytes
        cipher = AES.new(key, AES.MODE_ECB)
        # Pad/truncate encoded string to 16 bytes for demo
        padded = encoded[:16].ljust(16, "0").encode()
        aes_out = cipher.encrypt(padded)
        print("[AES output]", aes_out.hex())

    print("\nAll tests completed.")

if __name__ == "__main__":
    run_tests()
