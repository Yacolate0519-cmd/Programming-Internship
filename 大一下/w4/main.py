class Menu:
    def __init__(self):
        self.main = {'漢堡' : 80 , '薯條' : 60}
        self.beverage = {'可樂' : 45}
        self.dessert = {'蛋糕' : 100}

    def show_menu(self):
        print(f'主食: {self.main}')
        print(f'飲料: {self.beverage}')
        print(f'甜點: {self.dessert}')

    def add(self , item , price):
        self.main[item] = price

    def remove(self , item):
        self.main.pop(item)

    def change(self , item , price):
        self.main[item] = price

class FoodItem(Menu):
    pass

class Customer:
    def __init__(self):
        self.customers = {}
    
    def create_customer(self , name , contact):
        self.customers[name] = contact
        
    def show_customers(self):
        print('--' * 30)
        for i in self.customers.items():
            print(i)
        print('--' * 30)
        

class FoodOrderingSystem:
    def __init__(self):
        self.menus = {}
        menu = Menu()
        self.menus[] = menu
        
    def show_menu(self):

        self.menus.show_menu()

    def add_remove(self , temp):
        temp = int(temp)
        if temp == 1:
            pass

    def order(self):
        pass

    def search_order(self):
        pass


if __name__ == '__main__':

    system = FoodOrderingSystem()
    system.show_menu()



    # user = int(input("輸入使用者身份(請輸入代號): 1.admin 2.member\n"))

    # system = FoodOrderingSystem()

    # if user == 1:
    #     while 1:
    #         control = int(input('1.菜單與訂單管理(修理、新增)\n2.會員管理\n3.管理訂單\n4.離開系統\n'))
    #         if control == 1:
    #             system.show_menu()

    #         if control == 2:
    #             pass
            
    #         if control == 3:
    #             temp = input("1.新增\n2.刪除\n3.調整價格\n")
    #             system.add_remove(temp)

    #         if control == 4:
    #             break
            
            

    # if user == 2:
    #     pass

