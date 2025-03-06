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

import os 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':

    menu = Menu()
    menu.add_item('漢堡' , 100)
    menu.add_item('薯條' , 40)
    menu.add_item('可樂' , 45)

    while 1:
        system = FoodOrderingSystem()
        control = input('1.Admin\n2.Memeber\n3.Exit\n')
        if control == '1':
            pass
        elif control == '2':
            while 1:
                control = input('1.購物車\n2.Choose Ordering\n3.Send Ordering\n4.Exit\n')
                if control == '1':
                    pass
                
                elif control == '2':
                    while 1:
                        control = input('1.Show Menu\n2.Add_or_remove Item\n3.Ordering\n4.Exit\n')
                        if control == '1':
                            menu.show_menu()

                        elif control == '2':
                            control = input('1.Add_Item\n2.Remove_Item\n3.Update_item\n4.Search_Ordering\n5.quit\n') 
                            if control == '1':
                                menu.add_item()

                            elif control == '2':
                                menu.remove_item()

                            elif control == '3':
                                menu.update_ordering()

                            elif control == '4':
                                menu.search_ordering()

                            elif control == '5':
                                break   
                        
                        elif control == '3':
                            pass

                        elif control == '4':
                            break


                elif control == '3':
                    pass
                
                elif control == '4':
                    break

        elif control == '3':
            break
    print('🍔感謝使用🍟')