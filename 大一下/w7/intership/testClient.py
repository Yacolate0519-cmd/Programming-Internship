# testClient.py
import socket
import threading

def recv(sock):
    while True:
        try:
            recvMsg, _ = sock.recvfrom(1024)
            print("👤 Server:", recvMsg.decode('utf-8').strip())
        except:
            break

def send(sock, addr):
    while True:
        sendMsg = input()
        sock.sendto(sendMsg.encode('utf-8'), addr)
        if sendMsg.lower() == 'exit':
            break

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '192.168.1.110'
    port = 1024
        
    try:
        name = input("請輸入你的名字：")
        client.sendto(name.encode('utf-8'), serverAddr)

        tr = threading.Thread(target=recv, args=(client,), daemon=True)
        ts = threading.Thread(target=send, args=(client, serverAddr))

        tr.start()
        ts.start()
        tr.join()
        ts.join()

    except OSError as e:
        print(e)
        print('Server already close')
    
    except Exception as e:
        print(e)
    print("The chat room already closed")
