import base64

def base64_encode(data: str) -> str:
    return base64.b64encode(data.encode()).decode()

def xor_encode(data: str, key: int = 42) -> str:
    return ''.join(chr(ord(c) ^ key) for c in data)

def string_replace(data: str, replacements: dict) -> str:
    for old, new in replacements.items():
        data = data.replace(old, new)
    return data

def obfuscate(data: str, methods: list) -> str:
    """
    Apply multiple obfuscation methods in order.
    Example methods: ["base64", "xor", "replace"]
    """
    result = data
    for m in methods:
        if m == "base64":
            result = base64_encode(result)
        elif m == "xor":
            result = xor_encode(result)
        elif isinstance(m, dict):  # {"replace": {"ls": "dir"}}
            if "replace" in m:
                result = string_replace(result, m["replace"])
    return result
