import socket
import threading

if __name__ == '__main__':
    socket_server = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
    host = '10.22.75.52'
    port = 12344
    socket_server.bind((host , port))
    print('Server started')
    clients = {}
    while True:
        try:
            msg , clientAddr = socket_server.recvfrom(1024)
            msg = msg.decode('utf-8')

            if not clientAddr in clients:
                print(f'{msg} -> Connection established from {clientAddr}')
                for addr in clients:
                    socket_server.sendto(f'[{msg}] joined.'.encode('utf-8') , addr)
                clients[clientAddr] = msg
                continue
            
            if msg.lower() == 'exit':
                client_name = clients[clientAddr]
                socket_server.sendto('clientexit'.encode('utf-8') , clientAddr)
                del clients[clientAddr]
                for client in clients:
                    socket_server.sendto(f'{client_name} left.'.encode('utf-8') , client)
                if len(clients) == 0:
                    print('The chat room is closed')
                    break
            
            else:
                msg = f'{clients[clientAddr]}: {msg}'
                print(msg)
                for addr in clients:
                    if addr != clientAddr:
                        socket_server.sendto(msg.encode('utf-8') , addr)
        
        except Exception as e:
            print(e)
