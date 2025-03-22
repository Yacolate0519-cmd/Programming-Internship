import socket
import threading

name = ""
def recv(sock , addr):
    global name
    sock.sendto(('Hi, ' + name).encode('utf-8'), addr)
    while 1:
        recvMsg = sock.recv(1024).decode('utf-8')
        print(f'{name}: {recvMsg}')
        if recvMsg.lower() == 'exit'.lower():
            break

def send(sock , addr):
    global name
    while 1:
        sendMsg = input()
        sock.sendto((sendMsg).encode('utf-8') , addr)
        if sendMsg.lower() == 'exit':
            break


if __name__ == "__main__":
    print('Welcome to chat room!')
    name = input('Enter your name: ')
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        host = '10.22.104.114'
        port = 12345
        tr = threading.Thread(target = recv , args = (server , (host , port)), daemon = True)
        ts = threading.Thread(target = send , args = (server , (host , port)))
        tr.start()
        ts.start()
        tr.join()
        ts.join()
        
    except OSError as e:
        print(e)
        print('Server stopped')

    except Exception as e:
        print(e)
    server.close()
    print('The chat room is closed')    