import socket
import threading

name = ''
running = True 

def recv(sock, addr):
    global name, running
    sock.sendto(name.encode('utf-8'), addr)
    sock.settimeout(1)  

    while running:
        try:
            recvMsg, _ = sock.recvfrom(1024)
            recvMsg = recvMsg.decode('utf-8').strip()
            print(recvMsg)
            if recvMsg.lower() == 'exit':
                running = False
                break
        except socket.timeout:
            continue
        except:
            break

def send(sock, addr):
    global running
    while running:
        sendMsg = input()
        sock.sendto(sendMsg.encode('utf-8'), addr)
        if sendMsg.lower() == 'exit':
            running = False
            break

def main():
    global name
    name = input('Enter your name: ')
    print('--'*5 + name + '--'*5)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '192.168.1.110'
    port = 1024
    server = (host, port)

    try:
        print('📡 Connecting to server...')
        tr = threading.Thread(target=recv, args=(client, server), daemon=True)
        ts = threading.Thread(target=send, args=(client, server))
        tr.start()
        ts.start()
        ts.join()  
        client.close()
        tr.join()  

    except OSError as e:
        print(e)
        print("Server stopped")

    except Exception as e:
        print(e)

if __name__ == '__main__':
    print("Welcome to chat room")
    main()
    print("The chat room is closed")
