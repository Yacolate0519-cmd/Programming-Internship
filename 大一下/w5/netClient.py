import socket

client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client_socket.connect(('10.22.97.220' , 12345))
client_socket.send("Hello, server".encode('utf-8'))

response = client_socket.recv(1024).decode('utf-8')
print(f'Received response: {response}')

client_socket.close()
print('Client closed')