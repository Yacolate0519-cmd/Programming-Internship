import socket

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(('10.22.75.52' , 1024))

def receive_and_print():
    try:
        data = client.recv(1024).decode('utf-8') 
        if not data:
            return False
        print(data)
        return data
    except:
        return False

while True:
    data = receive_and_print()
    if data is False:
        break

    if '決定你想要的角色' in data:
        choice = input('輸入角色代號: ')
        client.send(choice.encode('utf-8'))

    elif '選擇技能' in data:
        skill_input = input('輸入技能代號: ')
        client.send(skill_input.encode('utf-8'))

    elif '感謝遊玩' in data:
        print('🍎' + '=='*30 + '🍎')
        break

client.close()

