import socket

target_host = 'localhost'
target_port = 7000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
msg = input('Envie uma MSG ao SERVIDOR: ')
client.send(msg.encode('utf-8'))
response = client.recv(4096)
print(response)
