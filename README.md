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
