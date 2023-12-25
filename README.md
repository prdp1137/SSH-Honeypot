# SSH-Honeypot

## Overview
This is a simple SSH honeypot built with Python. This is a lightweight honeypot tool designed to emulate an SSH server, attracting potential attackers and capturing their activities.

The honeypot logs connection attempts, authentication requests, and other relevant information for analysis.

## Setup
1. Install required dependencies:
```bash
pip install -r requirements.txt
```
2. Run the honeypot
```bash
sudo python3 honeypot.py -l 0.0.0.0 -p 22
```

## Sample Logs
```
{'timestamp': '2023-12-25 20:25:21.117837', 'message': 'Got a connection!', 'ip': '127.0.0.1', 'sessionID': 'ae65f12f-44bf-4c9f-9850-353f32786ac6'}
{'timestamp': '2023-12-25 20:25:23.102249', 'message': 'SSH negotiation failed.', 'sessionID': 'ae65f12f-44bf-4c9f-9850-353f32786ac6'}
{'timestamp': '2023-12-25 15:15:27.213175', 'message': 'Got a connection!', 'ip': '127.0.0.1', 'sessionID': '5b36d44a-5e22-4664-8c26-1d6aca5ff037'}
{'timestamp': '2023-12-25 15:15:30.933291', 'message': 'User tried to authenticate!', 'username': 'randomuser', 'password': 'randompassword', 'sessionID': '5b36d44a-5e22-4664-8c26-1d6aca5ff037'}
{'timestamp': '2023-12-25 15:15:30.945785', 'ip': '127.0.0.1', 'message': 'Authentication successful!', 'sessionID': '5b36d44a-5e22-4664-8c26-1d6aca5ff037'}
{'timestamp': '2023-12-25 15:16:09.580090', 'message': 'Got a connection!', 'ip': '127.0.0.1', 'sessionID': 'c2af045e-6f56-4258-b8b0-b710f3a8343f'}
```

### Configuration
Modify the banner variable in the script to emulate different SSH server environments.
```bash
export OS_BANNER=SSH-2.0-OpenSSH_7.4p1 Debian-10+deb9u2
```

### Logging
All events, including connection attempts and authentication details, are logged to the honeypot.log file.

## Disclaimer
This honeypot is intended for educational and research purposes only. Use it responsibly and in compliance with applicable laws and regulations.

Special thanks to the Paramiko library for SSH protocol implementation.
---
Feel free to contribute, report issues, or provide feedback to enhance the functionality and security of this SSH honeypot.
