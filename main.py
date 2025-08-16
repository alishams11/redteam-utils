import argparse   
from core import obfuscator  

def main():
    parser = argparse.ArgumentParser(description="RedTeam Utils - C2 & Payload Tools") 

    parser.add_argument("--obfuscate", nargs="+", help="Enable obfuscation methods (base64, xor, replace)")

    args = parser.parse_args()  

    print("=== RedTeam Utils ===")

    if args.obfuscate:   
        cmd = "whoami"   
        encoded = obfuscator.obfuscate(cmd, args.obfuscate)
        print(f"[*] Original: {cmd}")
        print(f"[*] Obfuscated: {encoded}")
    else:
        print("[*] Tool under development...")

if __name__ == "__main__":
    main()
