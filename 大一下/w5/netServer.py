import socket

server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_socket.bind(('10.22.75.52' , 1024))
server_socket.listen()
print(f'Server is listening on port 12345, waitting for connection')

client_socket , addr = server_socket.accept()
print(f'Connection from {addr}')

message = client_socket.recv(1024).decode('utf-8')
print(f'Received message: {message}')

response = 'Received message'

client_socket.send(response.encode('utf-8'))
client_socket.close()

server_socket.close()
print("Server closed")
