import socket

print(socket.gethostname())
myIP = socket.gethostbyname(socket.gethostname())
print(myIP)

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.connect((myIP , 1024))
print(s.getsockname()[0])