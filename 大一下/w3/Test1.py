class BankAccount:
    def __init__(self , name , balance , billing = 0):
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
        print('--' * 30 )
        print(f'帳戶持有者:{self.name}, 餘額: {self.balance}')
        print('--' * 30 )
    
    def history_billing(self):
        print('None')
    
class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self , owner , initial_balance = 0 , billing = 0):
        new_customer = BankAccount(owner , initial_balance , billing)
        self.accounts[owner] = new_customer
    
    def get_account(self , owner):
        if owner in self.accounts:
            self.accounts[owner].search_balance()
        else:
            print('查無帳戶')
        
    def deposit(self , owner , amount):
        if owner in self.accounts:
            self.accounts[owner].deposit(amount)
    
    def withdraw(self , owner , amount):
        if owner in self.accounts:
            self.accounts[owner].withdraw(amount)
    
    def display_accounts(self):
        print('--' * 30 + '\n帳戶列表')
        for account in self.accounts.values():
            print(account.name)
        print('--' * 30)
    
    def transfer(self , owner , receive , amount):
        if owner in self.accounts and receive in self.accounts:
            owner_account = self.accounts[owner]
            receive_account = self.accounts[receive]

            if owner_account.balance >= amount:
                owner_account.withdraw(amount)
                receive_account.deposit(amount)
                print('轉帳成功')
            else:
                print('餘額不足')
        else:
            print('查無帳戶')        
        
        
if __name__ == '__main__':
    system = BankSystem()
    while 1:
        control = int(input("1.創建帳戶\n2.存款\n3.提款\n4.查詢餘額\n5.轉帳\n6.顯示帳戶列表\n7.離開系統\n"))
        if control == 1:
            name , balance , billing = input('輸入資訊: ').split()
            balance = int(balance)
            billing = int(billing)
            system.create_account(name , balance , billing)
            
        elif control == 2:
            owner , amount = input('輸入存款人以及金額: ').split()
            amount = int(amount)
            system.deposit(owner , amount)
        
        elif control == 3:
            owner , amount = input("輸入提款人以及金額: ").split()
            amount = int(amount)
            system.withdraw(owner , amount)
        
        elif control == 4:
            owner = input('帳戶持有者姓名: ')
            system.get_account(owner)
        
        elif control == 5:
            owner , receive , amount = input('輸入轉款人以及收款人及金額: ').split()
            amount = int(amount)
            system.transfer(owner , receive , amount)
            
        elif control == 6:
            system.display_accounts()
            
        elif control == 7:
            break
        