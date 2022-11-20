import socket

HOST = '192.168.1.65'
PORT = 8282

server = socket.socket()
server.bind((HOST, PORT))
print("[-] Servidor iniciado")
print("[-] Esperando pela conexão com o cliente...")

server.listen(1)
client, client_adrr = server.accept()
print(f'[+] {client_adrr} Cliente conectado no servidor!')

while True:
    command = input('Comando:')
    command = command.encode('windows-1252')
    client.send(command)
    print("Comando enviado!")
    output = client.recv(1024)
    output = output.decode('windows-1252')
    print(f"Resposta: {output}")
