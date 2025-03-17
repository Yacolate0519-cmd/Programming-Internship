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

        #我覺得水箭龜有火箭頭槌有點鳥，所以我改名成水箭頭槌
        self.skill = {'水槍' : {'damage' : 55 , 'require_fp' : 40},
                      '水箭頭槌' : {'damage' : 40 , 'require_fp' : 15}}
        
class Bulbassaur(PokemonType):
    def __init__(self , name , hp , fp , type):
        super().__init__(name , hp , fp , type)
        self.skill = {'藤編' : {'damage' : 35 , 'require_fp' : 45},
                      '飛葉快刀' : {'damage' : 55 , 'require_fp' : 45}}
        
import os 
import random
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')   

import socket

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server_socket.bind(('10.22.75.52' , 1024))
    server_socket.listen()
    print('伺服器已啟動，等待玩家連線...')

    client_socket , addr = server_socket.accept()

    characters = {
    'cha1' : Charmander('🔥小火龍' , 100 , 60 , 'fire' ) ,
    'cha2' : Blastoise('🌊傑尼龜' , 100 , 30 , 'water' ),
    'cha3' : Bulbassaur('🌿妙挖種子' , 100 , 90 , 'grass' )
    }

    print('決定你想要的角色: \n1.小火龍\n2.傑尼龜\n3.妙蛙種子\n')
    choose = client_socket.recv(1024).decode('utf-8')
    print(choose)
    if choose == '1':
        cha = characters['cha1']

    elif choose == '2':
        cha = characters['cha2']

    elif choose == '3':
        cha = characters['cha3']
    # clear()
    print(f'已選擇角色: {cha.name}')
    enemy = random.choice([i for key , i , in characters.items() if i != cha])
    print(f'發現敵人: {enemy.name} , 血量: {enemy.hp}')
    
    while 1:
        print(f'你的回合 \n\n {cha.name} 剩餘HP: {cha.hp} 剩餘FP: {cha.fp}\n')
        print(f' {enemy.name} 剩餘HP: {enemy.hp} 剩餘FP: {enemy.fp}\n')
        print('選擇技能')
        for i , skill_name in enumerate(cha.skill.keys(),1):
            print(f'{i}. {skill_name} (傷害: {cha.skill[skill_name]['damage']} , FP消耗: {cha.skill[skill_name]['require_fp']})')
        
        print('輸入技能代號: ')

        choice = int(client_socket.recv(1024).decode('utf-8'))
        skill_list = list(cha.skill.keys())
        skill_name = skill_list[choice - 1]
        cha.attack(skill_name , enemy)

        if enemy.dead():
            print(f'{enemy.name}已被擊敗，可收服\n'+'--'*15 + f'已收服{enemy.name}' + '--'*15)
            break
        else:
            print(f'敵人得回合')
            enemy_skill = random.choice(list(enemy.skill.keys()))
            enemy.attack(enemy_skill , cha)

        if cha.dead():
            print(f'{cha.name}已倒下，回家重練')
            break

        print('--'*30)
print('\n\n\t\t\t\t⛳感謝遊玩⛳')


