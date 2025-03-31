# testServer.py
import socket
import threading

name = ''

def recv(sock, addr):
    global name
    # 傳送歡迎訊息
    sock.sendto(name.encode('utf-8'), addr)
    sock.sendto(("Hi, " + name).encode('utf-8'), addr)

    while True:
        try:
            recvMsg, _ = sock.recvfrom(1024)
            recvMsg = recvMsg.decode('utf-8').strip()
            print(f'{name}: {recvMsg}')
            if recvMsg.lower() == 'exit':
                break
        except:
            break

def send(sock, addr):
    while True:
        sendMsg = input()
        sock.sendto(sendMsg.encode('utf-8'), addr)
        if sendMsg.lower() == 'exit':
            break

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '0.0.0.0'  # 接受任何來源
    port = 1024

    try:
        server.bind((host, port))
        print("✅ Server started, waiting for connection...")

        msg, clientAddr = server.recvfrom(1024)
        name = msg.decode('utf-8')
        print(f'🟢 {name} connected from {clientAddr}')

        tr = threading.Thread(target=recv, args=(server, clientAddr), daemon=True)
        ts = threading.Thread(target=send, args=(server, clientAddr))

        tr.start()
        ts.start()
        tr.join()
        ts.join()

    except Exception as e:
        print(f'❌ Server error: {e}')

    server.close()
    print("🔴 Chat server closed.")
