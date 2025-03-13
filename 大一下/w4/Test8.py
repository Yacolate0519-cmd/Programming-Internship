class Person:
    rate = 0.3
    def __init__(self , name , balance):
        self.name = name
        self.balance = balance
        self.set_new_rate()

    def set_new_rate(cls):
        cls.rate = 0.2
    
    def return_rate(cls):
        return cls.rate

'''
新增__del__方法修改學生人數
'''

if __name__ == '__main__':
    p1 = Person('yacolate' , 500)
    print(p1.return_rate())