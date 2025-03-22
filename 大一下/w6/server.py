import socket
import threading

name = ""
def recv(sock , addr):
    global name
    sock.sendto(('Hi, ' + name).encode('utf-8'), addr)
    while 1:
        recvMsg = sock.recv(1024).decode('utf-8').strip()
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
    server = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
    host = "10.22.75.52"
    port = 12345
    try:
        server.bind((host , port))
        print('Server started')
        msg , clientAddr = server.recvfrom(1024)
        print(f'{msg.decode("utf-8")}\t Connection establised from {clientAddr}')
        tr = threading.Thread(target = recv , args = (server , clientAddr), daemon = True)
        ts = threading.Thread(target = send , args = (server , clientAddr))

        name = msg.decode('utf-8')
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