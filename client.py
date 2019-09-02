import socket

target_host = 'localhost' # IP do servidor tcp.
target_port = 7000 # Porta do servidor tcp.

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
msg = input('Envie uma MSG ao SERVIDOR: ') # Mensagem a ser enviada para o servidor.
client.send(msg.encode('utf-8'))
response = client.recv(4096) # Resposta do Servidor.
print(response)
