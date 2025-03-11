class Character:
    def __init__(self , name , health):
        self.name = name
        self.__health = health

    @property
    def health(self):
        return f'{self.name} 的血量為: {self.__health}'

    @health.setter
    def health(self , new_health):
        self.__health = new_health

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self , new_name):
        self.name = new_name

    
class Fire(Character):
    def __init__(self , name , health , type):
        super().__init__(name , health)
        self.__type = type

if __name__ == '__main__':
    dragon = Fire('Dragon' , 150 , 'Fire')
    

