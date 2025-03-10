class Character:
    def __init__(self , name ,health):
        self.name = name
        self.__health = health

    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self , blod):
        total = self.__health - blod
        if total < 0:
            print('Dead')
        else:
            self.__health = total


class Warrior(Character):
    def __init__(self , name ,health , attack_power):
        super().__init__(name , health)
        self.__attack_power = attack_power

    @property
    def attack_power(self):
        return f'{self.name} 的力量為: {self.__attack_power}'
    
    @attack_power.setter
    def attack_power(self , power):
        total = self.__attack_power - power
        if total < 0:
            self.__attack_power = 0
            print('累死了')
        else:
            self.__attack_power = total
            

class Mage(Character):
    def __init__(self , name , health , mana):
        super().__init__(name , health)
        self.__mana = mana


    def mana(self):
        return f'{self.name} 的魔力值為: {self.__mana}'
    
    def update_mana(self , new_mana):
        total = self.__mana - new_mana
        if total < 0:
            self.__mana = 0
            print('魔力值歸零，爆體死亡')
        else:
            self.__mana = total
   

if __name__ == '__main__':
    harry = Mage('Harry Potter' , 100 , 80)
    print(harry.mana)
    print('--'*15 + "施咒後" + "--"*15)
    harry.update_mana = 15
    print(harry.mana)
    print('--'*15 + "施展多個咒語後" + "--"*15)
    harry.mana = 100
    print(harry.mana)

    print('\n\n\n')

    caesar = Warrior("Caesar" , 150 , 90)
    print(caesar.attack_power)
    print('--'*15 + "打一場仗" + "--"*15)
    caesar.attack_power = 15
    print(caesar.attack_power)
    print('--'*15 + "打很多場仗" + "--"*15)
    caesar.attack_power = 100
    print(caesar.attack_power)