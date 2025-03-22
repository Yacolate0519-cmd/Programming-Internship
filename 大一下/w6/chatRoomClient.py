import socket
import threading

name = ""

def recv(socket1 , addr):
    global name
    socket1.sendto(name.encode('utf-8') , addr)
    while 1:
        recvMsg = socket1.recv(1024).deocde('utf-8')
        print(recvMsg)
        if recvMsg.lower() == 'clientexit'.lower():
            break

def send(socket1 , addr):
    global name 
    while 1:
        sendMsg = input()
        socket1.sendto(sendMsg.encode('utf-8') , addr)
        if sendMsg.lower() == 'exit':
            break

def main():
    global name
    name = input('Enter your name: ')        
    print('--' * 5 , name , '--' * 5)
    client_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_DGRAM)
    serverAddr = "10.144.252.228"
    port = 1688
    server = (serverAddr , port)
    try:
        print('Server started')
        tr = threading.Thread(target = recv,
                              args = (client_socket , server),
                              daemon = True)
        
        ts = threading.Thread(target = recv,
                              args = (client_socket , server))
        
        tr.start()
        ts.start()
        tr.join()
        ts.join()
    
    except OSError as e:
        print(e)
        print('Server stopped')

    except Exception as e:
        print(e)
    client_socket.close()

if __name__ == '__main__':
    print('Welcome to chat room!')
    main()
    print('The chat room is closed.')
        
