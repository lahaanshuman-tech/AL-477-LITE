import base64

def decode_recipe(encoded_recipe, signature):
    decoded = base64.b64decode(encoded_recipe).decode()
    if signature in decoded:
        return decoded.replace(signature, "")
    return None

def decode_payload(encoded_digest):
    decoded = base64.b64decode(encoded_digest).decode()

    # Split out payload, recipe, and signature
    if "::SEP::" in decoded and "::SIG::" in decoded:
        payload, rest = decoded.split("::SEP::", 1)
        encoded_recipe, signature = rest.split("::SIG::", 1)
        recipe = decode_recipe(encoded_recipe, signature)
        return payload, recipe, signature
    else:
        return decoded, None, None
