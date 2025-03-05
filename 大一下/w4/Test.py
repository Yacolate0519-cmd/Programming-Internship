class FoodItem:
    def __init__(self , name , price):
        self.name = name
        self.price = price

class Menu(FoodItem):
    def __init__(self):
        self.all_items = {}    

    def show_menu(self):
        print('--'*30)
        print('餐點\t價錢')
        print('--'*30)
        for key , value in self.all_items.items():
            print(key , '\t' , value)
        print('--'*30)

    def add_item(self , name , price):
        if name not in self.all_items.keys():
            self.all_items[name] = price
        else:
            print('Item already exist')

    def remove_item(self , name):
        if name in self.all_items.keys():
            self.all_items.pop(name)

    def change_itme_price(self , name , price):
        self.all_items[name] = price

import time
class Order:
    def __init__(self , name , items , time = time.strftime("%Y-%m-%d %H:%M:%S") , tableware  = 0, special_service = 0):
        self.name = name 
        self.items = items
        self.time = time 
        self.tableware = tableware
        self.special_service = special_service

class FoodOrderingSystem(Menu , Order):
    def __init__(self):
        self.orderings = {}

    def show_menu(self):
        menu.show_menu()

    def add_item(self , name , price):
        menu.add_item(name , price)

    def remove_item(self , name):
        menu.remove_item(name)

    def create_ordering(self , name , shoppingList):
        new_order = Order(name , shoppingList)
        self.orderings[new_order.name] = shoppingList 

    def search_ordering(self , name):
        if name in self.orderings:
            print(f'顧客名稱: {name}')
            print(f'Shopping Cart: {self.orderings[name]}')

    def update_ordering(self , name , shoppingList):
        if name in self.orderings:
            self.orderings[name] = shoppingList

    def remove_ordering(self , name):
        self.orderings.pop(name)
    
    def show_all_ordering(self):
        if not self.orderings:
            print('無訂單')
        else:
            for key , value in self.orderings.items():
                print('--'*30)
                print(f'訂單客戶: {key}, 訂單: {value}')
                print('--'*30)



class Customer(FoodOrderingSystem):
    def __init__(self , name , contact):
        self.name = name
        self.contact = contact
    
    def create_ordering(self, name, shoppingList):
        return super().create_ordering(name, shoppingList)
    
    def remove_item(self, name):
        return super().remove_item(name)
    
    def update_ordering(self, name, shoppingList):
        return super().update_ordering(name, shoppingList)
    
    def show_all_ordering(self):
        return super().show_all_ordering()

import os 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':

    menu = Menu()
    menu.add_item('漢堡', 100)
    menu.add_item('薯條', 50)
    menu.add_item('可樂', 45)

    print('-'*30)

    system = FoodOrderingSystem()
    
    system.add_item('測試', 100)
    system.remove_item('可樂')

    system.create_ordering('Yacolate' , ['漢堡','可樂'])
    system.search_ordering('Yacolate')

    print('Test')

    system.create_ordering('Gplee' , ['漢堡','薯條','可樂'])
    system.update_ordering('Gplee' , ['可樂','薯條','要餐具'])
    system.remove_ordering('Yacolate') 
    system.show_all_ordering()

    while 1:
        