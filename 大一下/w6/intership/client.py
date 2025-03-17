import socket
import time
client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client_socket.connect(('10.22.75.52' , 1024))

message = '1'
client_socket.send(message.encode('utf-8'))
# time.sleep(2)
move = input('輸入技能')
client_socket.send(move.encode('utf-8'))
# time.sleep(2)
move = input('輸入技能')
client_socket.send(move.encode('utf-8'))
# time.sleep(2)
move = input('輸入技能')
client_socket.send(move.encode('utf-8'))
# time.sleep(2)
move = input('輸入技能')
client_socket.send(move.encode('utf-8'))



client_socket.close()

