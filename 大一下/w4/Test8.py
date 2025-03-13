class Person:
    member = 0
    def __init__(self , name , balance):
        self.name = name
        self.balance = balance
        Person.increase_member()

    @classmethod
    def get_member(cls):
        print(cls.member)

    @staticmethod
    def increase_member():
        Person.member += 1
    
    @staticmethod
    def decrease_member():
        Person.member -= 1

    def __del__(self):
        Person.decrease_member()
    
'''
新增__del__方法修改學生人數
'''

if __name__ == '__main__':
    p1 = Person('ycolate' , 500)
    Person.get_member()
    del p1
    p2 = Person("Gplee" , 500)
    Person.get_member()
