class FoodItem:
    def __init__(self , name , category , price , size = None):
        self.name = name
        self.category = category
        self.price = price
        self.size = size

class Menu:
    def __init__(self):
        self.all_items = {}

    def show_menu(self):
        print('--' * 30)
        print(f'餐點\t種類\t價格\t大小')
        print('--' * 30)
        for name, item in self.all_items.items():
            size = item.size if item.size else "N/A"
            print(f'{item.name}\t{item.category}\t{item.price}\t{size}')
        print('--' * 30)

    def add_item(self , name , category , price , size = None):
        if name not in self.all_items:
            self.all_items[name] = FoodItem(name , category , price , size)
        else:
            print('已有此商品')

    def remove_item(self , name):
        if name in self.all_items:
            self.all_items.pop(name)
            print(f'已移除 {name}')
        else:  
            print(f'找不到商品 {name}')
        
    def change_price(self , name , price):
        if name in self.all_items:
            self.all_items[name].price = price
            print(f'餐點: {name}, 價格更新為: {price}')
        else:
            print('查無此餐點')

import time
class Order:
    def __init__(self , customer_name , items , tableware = 0 , special = 0):
        self.customer_name = customer_name
        self.items = items
        self.time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.tableware = tableware
        self.special = special
    
    def create_order(self , name , shoppingList):
        self.items[name] = shoppingList

    def show_order(self , name):
        print(self.items[name])
        total = 0
        for i in self.items:
            total += i.price

    def cancel_order(self , name):
        self.items.pop(name)

class Customer:
    def __init__(self , name , contact):
        self.name = name
        self.contact = contact

    def create_order(self , name , shoppingList):
        new_order = Order(name , shoppingList)
        new_order.self.orderings[name] = shoppingList

    def show_order(self , name):
        Order.show_order(name)

    def cancel_order(self , name):
        Order.cancel_order(name)
        

class FoodItemSystem:
    def __init__(self):
        self.menu = Menu()
        self.orders = []
    
    def create_order(self , name , shopping_list):
        new_order = Order(name , shopping_list)
        if new_order in self.orders:
            print('使用者存在')
        else:
            self.orders.append(new_order)
        

    def show_orders(self):
        if not self.orders:
            print('目前無訂單')
        else:
            for order in self.orders:
                Order.show_order()

import os 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')    

if __name__ == '__main__':

    system = FoodItemSystem()
    menu = system.menu

    menu.add_item('漢堡' , '主餐' , 100)
    menu.add_item('薯條' , '點心' , 40)
    menu.add_item('可樂', '飲料' , 45 , '中杯')

    while 1:
        control = input("1.Admin(管理員)\n2.Member(會員)\n3.離開系統\n")
        if control == '1':
            #Admin  
            clear()
            while 1:
                control = input('1.Menu_manage\n2.Customer_manage\n3.Order_manage\n4.Exit\n')
                if control == '1':
                    clear()
                    while 1:
                        control = input('1.Show_Menu\n2.Add_or_remove\n3.Change_price\n4.Exit\n')
                        if control == '1':
                            menu.show_menu()

                        elif control == '2':
                            clear()
                            while 1:
                                control = input('1.Add_item\n2.Remove_item\n3.Exit\n')
                                if control == '1':
                                    name , category , price = input('請輸入餐點名稱、種類、價格: ').split()
                                    size = input('若商品為飲料，請輸入大小，若不輸入，預設為N/A: ')
                                    price = int(price)
                                    menu.add_item(name , category , price , size if size else None)
                                    #這邊寫說使用GPT 詢問如何讓使用者自選要不要輸入size

                                elif control == '2':
                                    name = input('輸入商品名稱: ')
                                    menu.remove_item(name)

                                elif control == '3':
                                    break

                        elif control == '3':
                            name , price = input('輸入商品以及更改後的價格: ').split()
                            menu.change_price(name , price)

                        elif control == '4':
                            break

                elif control == '2':
                    #Customer_manage
                    clear()
                    while 1:
                        control = input('1.客戶資料\n2.建立訂單\n3.瀏覽訂單\n4.取消訂單\n5.Exit\n')
                        if control == '1':
                            pass

                        elif control == '2':
                            pass

                        elif control == '3':
                            pass

                        elif control == '4':
                            pass

                        elif control == '5':
                            break

                elif control == '3':
                    while 1:
                        control = input('1.建立訂單\n2.瀏覽訂單\n3.取消訂單\n4.Exit\n')
                        if control == '1':
                            pass

                        elif control == '2':
                            pass

                        elif control == '3':
                            pass

                        elif control == '4':
                            break
                    
                elif control == '4':
                    break

        elif control == '2':
            #Member
            clear()
            
            name , contact = input('請輸入姓名以及聯絡方式: ').split()
            if name not in system.orders:
                system.create_order(name , contact)

            while 1:
                control = input('1.觀看菜單\n2.挑選商品\n3.送出訂單\n4.Exit\n')
                if control == '1':
                    menu.show_menu()
                
                elif control == '2':
                    shopping_list = input('輸入商品名稱: ').split()
                    system.create_order(name , shopping_list)
                
                elif control == '3':
                    pass

                elif control == '4':
                    break

        elif control == '3':
            break
    print('🍔感謝使用🍟')
