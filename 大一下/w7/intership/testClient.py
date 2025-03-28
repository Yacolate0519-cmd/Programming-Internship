import socket
import threading

name = ''

def recv(sock , addr):
    global name
    sock.sendto(name.encode('utf-8') , addr)
    while 1:
        recvMsg = sock.recv(1024).decode('utf-8')
        if recvMsg.lower() == 'exit':
            break
        else:
            print(f'Server: {recvMsg}')

def send(sock , addr):
    global name
    while 1:
        sendMsg = input()
        sock.sendto((sendMsg).encode('utf-8') , addr)
        if sendMsg.lower() == 'exit':
            break

if __name__ == "__main__":
    print("Welcome to chat room!")
    name = input("Enter your name: ")
    server = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
    try:
        host = '10.22.75.52'
        port = 1024
        tr = threading.Thread(target = recv , args = (server , (host , port)), daemon = True)
        ts = threading.Thread(target = send , args = (server , (host , port)))
        tr.start()
        ts.start()
        tr.join()
        ts.join()

    except OSError as e:
        print(e)
        print("Server stopped")
    
    except Exception as e:
        print(e)
    print('The chat room is closed')

        