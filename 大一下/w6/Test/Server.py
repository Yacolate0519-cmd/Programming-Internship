import socket
from colorama import init , Fore , Style
import random

init(autoreset = True)

def get_bar(current , max_value , length = 20 , color = Fore.GREEN):
    filled_length = int(length * current // max_value)
    bar = "█" * filled_length + '░' * (length - filled_length)
    return f'{color}[{bar}]{Style.RESET_ALL} {current}/{max_value}'

def get_status_bar(pokemon):
    hp_bar = get_bar(pokemon.hp , pokemon.max_hp , color = Fore.RED)
    fp_bar = get_bar(pokemon.fp , 60 if pokemon.fp <= 60 else pokemon.fp , color = Fore.BLUE)
    return f"{pokemon.name} HP: {hp_bar}\n{' '*len(pokemon.name)} FP: {fp_bar}"

class Pokemon:
    def __init__(self , name , hp , fp):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.fp = fp

    def take_damage(self , damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f'{self.name} 受到了{damage}點傷害，剩餘 HP: {self.hp}')
        if self.dead():
            print('葛屁了')

    def dead(self):
        if self.hp <= 0:
            return True
        return False
    
class PokemonType(Pokemon):
    def __init__(self , name , hp , fp , type):
        super().__init__(name , hp , fp)
        self.type = type

    def restraint(self , target):
        rate = {
            'fire' : {'grass' : 2 , 'water' : 0.5 , 'fire' : 1},
            'grass' : {'water' : 2 , 'fire' : 0.5 , 'grass' : 1},
            'water' : {'water' : 1 , 'fire' : 2 , 'grass' : 0.5} 
        }
        return rate.get(self.type , {}).get(target.type , 1.0)

    def attack(self , skill_name , target):
        if skill_name in self.skill:
            skill = self.skill[skill_name]
            if self.fp >= skill['require_fp']:
                damage = skill['damage'] * self.restraint(target)
                print(f"{self.name} 使用 {skill_name} 消耗魔力: {skill["require_fp"]}")
                target.take_damage(damage)
                self.fp -= skill['require_fp']  
            else:
                print('💢魔力不足無法施放💢')

class Charmander(PokemonType):
    def __init__(self , name , hp , fp , type):
        super().__init__(name , hp , fp , type)
        self.skill = {'抓傷': {'damage' : 20 , 'require_fp' : 0},
                      '火花' : {'damage' : 80 , 'require_fp' : 30}}

    

class Blastoise(PokemonType):
    def __init__(self , name , hp , fp , type):
        super().__init__(name , hp , fp , type)

        self.skill = {'水槍' : {'damage' : 55 , 'require_fp' : 40},
                      '水箭頭槌' : {'damage' : 40 , 'require_fp' : 15}}
        
class Bulbassaur(PokemonType):
    def __init__(self , name , hp , fp , type):
        super().__init__(name , hp , fp , type)
        self.skill = {'藤編' : {'damage' : 35 , 'require_fp' : 45},
                      '飛葉快刀' : {'damage' : 55 , 'require_fp' : 45}}
    
if __name__ == '__main__':
    def send_msg(msg):
        print(msg)  
        client.send(msg.encode('utf-8'))

    server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server.bind(('10.22.75.52' , 1024))
    server.listen()
    print('Server already start up...')

    client , addr = server.accept()
    print(f'Client: {client}')
    print(f'Addr: {addr}')

    characters = {
        'cha1' : Charmander('🔥小火龍' , 100 , 60 , 'fire' ) ,
        'cha2' : Blastoise('🌊傑尼龜' , 100 , 30 , 'water' ),
        'cha3' : Bulbassaur('🌿妙挖種子' , 100 , 90 , 'grass' )
    }

    start = '決定你想要的角色: \n1.小火龍\n2.傑尼龜\n3.妙蛙種子\n'
    client.send(start.encode('utf-8'))
    choose = client.recv(1024).decode('utf-8')

    cha = characters.get(f'cha{choose}', characters['cha1'])
    send_msg(f'已選擇角色: {cha.name}')
    
    enemy = random.choice([i for key , i in characters.items() if i != cha])
    send_msg(f'發現敵人: {enemy.name} , 血量: {enemy.hp}')

    while True:
        status = f"\n你的回合\n\n{get_status_bar(cha)}\n\n{get_status_bar(enemy)}\n\n"
        status += '選擇技能:\n'
        for i, skill_name in enumerate(cha.skill.keys(), 1):
            s = cha.skill[skill_name]
            status += f"{i}. {skill_name} (傷害: {s['damage']} , FP消耗: {s['require_fp']})\n"
        client.send(status.encode('utf-8'))

        choice = client.recv(1024).decode('utf-8')
        try:
            skill_name = list(cha.skill.keys())[int(choice) - 1]
            old_hp = enemy.hp
            cha.attack(skill_name, enemy)
            result = f"\n你使用了 {skill_name}，敵人從 {old_hp} → {enemy.hp}\n"
            send_msg(result)
        except Exception as e:
            send_msg('無效的技能選擇，請重新輸入')
            continue

        if enemy.dead():
            send_msg(f'{enemy.name} 已被擊敗，可收服\n' + '--'*15 + f'已收服 {enemy.name}' + '--'*15)
            break

        send_msg('\n敵人回合')
        enemy_skill = random.choice(list(enemy.skill.keys()))
        old_hp = cha.hp
        enemy.attack(enemy_skill , cha)
        send_msg(f"{enemy.name} 使用了 {enemy_skill}，你的血量從 {old_hp} → {cha.hp}")

        if cha.dead():
            send_msg(f'{cha.name} 已倒下，回家重練吧')
            break

        send_msg('--'*30)

    send_msg('\n\n\t\t\t\t⛳感謝遊玩⛳')
    client.close()
    server.close()