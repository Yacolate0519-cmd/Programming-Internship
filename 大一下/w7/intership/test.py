import socket
import threading

def recv_msg(sock):
    while True:
        try:
            msg, _ = sock.recvfrom(2048)
            msg = msg.decode('utf-8').strip()
            print(msg)

            if "獲勝" in msg or "被擊敗" in msg:
                break  
            
        except Exception as e:
            print(f"[接收錯誤] {e}")
            break

def send_input(sock, server_addr):
    while True:
        try:
            user_input = input()
            sock.sendto(user_input.encode('utf-8'), server_addr)

            if user_input.lower() == "exit":
                break
        except Exception as e:
            print(e)
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_ip = '192.168.1.110' 
    server_port = 1024
    server_addr = (server_ip, server_port)

    client.sendto("join".encode('utf-8'), server_addr)

    recv_thread = threading.Thread(target=recv_msg, args=(client,), daemon=True)
    recv_thread.start()

    send_input(client, server_addr)

    client.close()
    print("❎ 離開對戰")

if __name__ == '__main__':
    print("🎮 連線中，請稍後...")
    main()
