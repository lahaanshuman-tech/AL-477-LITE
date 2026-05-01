from al477lite.al477_encoder import encode_payload
from al477lite.al477_decoder import decode_payload

def main():
    print("=== AL-477 Lite Demo ===")
    print("Choose an option:")
    print("1. Encode")
    print("2. Decode")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        payload = input("Enter your payload to encode: ")
        encoded = encode_payload(payload)
        print("\n[ENCODED OUTPUT]")
        print(encoded)

    elif choice == "2":
        encoded = input("Enter your encoded string to decode: ")
        decoded_payload, recipe, signature = decode_payload(encoded)
        print("\n[DECODED OUTPUT]")
        print(f"Payload: {decoded_payload}")
        print(f"Recipe: {recipe}")
        print(f"Signature: {signature}")

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
