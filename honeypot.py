import socket
import sys
import threading
import paramiko
import datetime
import uuid
import argparse
import os

if not os.path.exists('.host.key'):
    host_key = paramiko.RSAKey.generate(2048)
    host_key.write_private_key_file('.host.key')
else:
    host_key = paramiko.RSAKey(filename='.host.key')

logFile = 'honeypot.log'

osBanner = os.environ.get('OS_BANNER', 'SSH-2.0-OpenSSH_7.4p1 Debian-10+deb9u2')

class Server(paramiko.ServerInterface):
    def __init__(self, session_id):
        self.event = threading.Event()
        self.session_id = session_id

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        log = {
            'timestamp': str(datetime.datetime.now()),
            'message': 'User tried to authenticate!',
            'username': username,
            'password': password,
            'sessionID': self.session_id,
        }
        print(log)
        with open(logFile, 'a') as f:
            f.write(str(log) + '\n')
        return paramiko.AUTH_SUCCESSFUL

def handle_client(client, session_id):
    try:
        bhSession = paramiko.Transport(client)
        bhSession.banner_timeout = 30
        bhSession.local_version = osBanner
        bhSession.add_server_key(host_key)

        server = Server(session_id)
        try:
            bhSession.start_server(server=server)
        except paramiko.SSHException as x:
            log = {
                'timestamp': str(datetime.datetime.now()),
                'message': 'SSH negotiation failed.',
                'sessionID': session_id,
            }
            print(log)
            with open(logFile, 'a') as f:
                f.write(str(log) + '\n')
        chan = bhSession.accept(20)
        log = {
            'timestamp': str(datetime.datetime.now()),
            'ip': client.getpeername()[0],
            'message': 'Authentication successful!',
            'sessionID': session_id,
        }
        print(log)
        with open(logFile, 'a') as f:
            f.write(str(log) + '\n')
        bhSession.close()
    except Exception as e:
        try:
            bhSession.close()
        except:
            pass

def main():
    parser = argparse.ArgumentParser(description='SSH Honeypot')
    parser.add_argument('-l', '--listen', help='Listen on [host] for incoming connections. Default: 0.0.0.0', default='0.0.0.0')
    parser.add_argument('-p', '--port', help='Port to listen on for incoming connections. Default: 2222', default=2222)

    args = parser.parse_args()

    server = args.listen
    ssh_port = int(args.port)

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((server, ssh_port))
        sock.listen(100)
        print('[+] Listening for connections on {}:{}'.format(server, ssh_port))
    except Exception as e:
        print('[-] Listen failed: {}'.format(str(e)))
        sys.exit(1)

    while True:
        try:
            client, addr = sock.accept()
            session_id = str(uuid.uuid4())
            log = {
                'timestamp': str(datetime.datetime.now()),
                'message': 'Got a connection!',
                'ip': addr[0],
                'sessionID': session_id,
            }
            print(log)
            with open(logFile, 'a') as f:
                f.write(str(log) + '\n')
            client_handler = threading.Thread(target=handle_client, args=(client, session_id))
            client_handler.start()
        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == '__main__':
    main()
