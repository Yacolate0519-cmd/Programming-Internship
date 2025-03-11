class Bank:
    def __init__(self , name , balance = 0, type = '普通帳戶'):
        self.name = name
        self.balance = balance
        self.type = type

    def balance_inquiry(self):
        print(f'{self.type} {self.name} 的餘額為： {self.balance} 元')

    def deposit(self , quantity):
        self.balance += quantity

    def withdraw(self , quantity):
        self.balance -= quantity

if __name__ == '__main__':
    customer1 = Bank('Yacolate',1000)
    customer1.balance_inquiry()

    customer2 = Bank('Breaddown' , 10000000 , '企業帳戶')
    customer2.balance_inquiry()

    customer3 = Bank('Gplee' , 50000 , '儲蓄帳戶')
    customer3.balance_inquiry()

    print('--'*30)
    print('存錢')
    customer1.deposit(500)
    customer1.balance_inquiry()

    print('--'*30)
    print('提款')
    customer2.withdraw(5000)
    customer2.balance_inquiry()

