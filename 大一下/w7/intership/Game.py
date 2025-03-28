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
    