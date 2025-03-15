import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('10.22.17.84',12345))
server_socket.listen()
print('Server started, waitting for connections...')

client_socket , addr = server_socket.accept()
print(f'Connection established from {addr}')
send_message = "Hello, client! I am the server".encode('utf-8')
client_socket.send(send_message)

try:
    while 1:
        recv_message = client_socket.recv(1024).decode('utf-8')
        print(f'client: {recv_message}')
        if recv_message.lower() == 'exit':
            break

except Exception as e:
    print(e)

server_socket.close()
print("Server Closed")