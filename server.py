import socket
import threading

bind_ip = 'localhost' # IP do Servidor TCP
bind_port = 7000 # Porta do Servidor TCP

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5) # Limite de conexoes com o servidor
print(f'[*] Escutando {bind_ip}:{bind_port}')

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f'- [*] Recebido: {request.decode()}') # Mensagem recebida do cliente.
    print('-' * 30)
    msg1 = f'Mensagem do cliente: {addr[0]}'
    msg2 = f' ACK! - Recebido pelo servidor.'
    client_socket.send(msg1.encode('utf-8'))
    client_socket.send(msg2.encode('utf-8'))
    client_socket.close()

while True:
    client, addr = server.accept()
    print(f'Conexão aceita de: {addr[0]}, {addr[1]}')
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

