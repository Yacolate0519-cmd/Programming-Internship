class BankAccount:
    def __init__(self , name , balance = 0 , billing = 0):
        self.name = name
        self.balance = balance
        self.billing = billing

    def deposit(self , amount):
        self.balance += amount

    def withdraw(self , amount):
        total = self.balance - amount
        if total < 0:
            print('餘額不足')
        else:
            self.balance -= amount

    def search_balance(self):
        return (f'帳戶持有人: {self.name},餘額: {self.balance}')

    def history(self):
        pass

class BankSystem:
    def __init__(self):
        self.accounts = []
    
    def create_account(self , owner , initial_balance = 0):
        new_customer = BankAccount(owner , initial_balance)
        self.accounts.append(new_customer)

    def get_account(self , owner):
        for account in self.accounts:
            if account.name == owner:
                BankAccount.search_balance()
            else:
                print('查無此人')

    def deposit(self , owner , amount):
        for account in self.accounts:
            if account.name == owner:
                BankAccount.deposit(amount)
            else:
                print('查無此人')

    def withdraw(self , amount):
        pass

    def transfer(self , owner , receive , amount):
        pass

    def display_account(self):
        pass

if __name__ == '__main__':
    system = BankSystem()
    control = int(input('1.創建帳戶\n2.存款\n3.提款\n4.查詢餘額\n5.轉帳6.查詢帳戶\n7.離開系統\n'))
    while 1:
        if control == 1:
            name , balance = input('輸入帳戶名稱以及金額: ').split()
            system.create_account(name , balance)

        elif control == 2:
            pass

        elif control == 3:
            pass

        elif control == 4:
            pass

        elif control == 5:
            pass

        elif control == 6:
            pass

        elif control == 7:
            break