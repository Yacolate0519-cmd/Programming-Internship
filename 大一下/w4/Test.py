import time
import os

class FoodItem:
    def __init__(self, name, category, price, size=None):
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

    def add_item(self, name, category, price, size=None):
        if name not in self.all_items:
            self.all_items[name] = FoodItem(name, category, price, size)
        else:
            print('已有此商品')

    def remove_item(self, name):
        if name in self.all_items:
            self.all_items.pop(name)
            print(f'已移除 {name}')
        else:  
            print(f'找不到商品 {name}')
        
    def change_price(self, name, price):
        if name in self.all_items:
            price = int(price)
            self.all_items[name].price = price
            print(f'餐點: {name}, 價格更新為: {price}')
        else:
            print('查無此餐點')

class Order:
    order_count = 1
    
    def __init__(self, customer_name, items, tableware=0, special=0):
        self.order_id = Order.order_count
        Order.order_count += 1
        self.customer_name = customer_name
        self.items = items
        self.time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.tableware = tableware
        self.special = special

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        print('--'*30)
        print(f'訂單編號: {self.order_id}, 客戶: {self.customer_name}, 時間: {self.time}')
        for item in self.items:
            print(f'{item.name}\t${item.price}')
        print(f'總價格: ${self.calculate_total()}')
        print('--'*30)

   

class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.orders = []

    def create_order(self, menu, shopping_list):
        items = []
        for name in shopping_list:
            if name in menu.all_items:
                items.append(menu.all_items[name])
            else:
                print(f'菜單中找不到 {name}')
        if items:
            new_order = Order(self.name, items)
            self.orders.append(new_order)
            print(f'訂單已建立，您的訂單編號為 {new_order.order_id}')
            return new_order.order_id, new_order.calculate_total()
        return None, 0

class FoodOrderingSystem:
    def __init__(self):
        self.menu = Menu()
        self.customers = {}
        self.orders = {}
    
    def create_customer(self, name, contact):
        if name in self.customers:
            print('使用者已存在')
        else:
            self.customers[name] = Customer(name, contact)
            print('客戶已新增')
    
    def find_customer(self , name):
        if name in self.customers:
            customer = self.customers[name]
            print('--'*30)
            print(f'顧客資訊: \n姓名: {customer.name}\n聯絡方式: {customer.contact}')
            print('--'*30)
        else:
            print('查無此顧客')

    def create_order(self, name, shopping_list):
        if name not in self.customers:
            print('請先建立客戶')
            return
        order_id, total_price = self.customers[name].create_order(self.menu, shopping_list)
        if order_id:
            self.orders[order_id] = self.customers[name].orders[-1]

    def show_orders(self):
        if not self.orders:
            print('目前無訂單')
        else:
            for order in self.orders.values():
                order.show_order()
    
    def find_order(self, order_id):
        order_id = int(order_id)
        if order_id in self.orders:
            self.orders[order_id].show_order()
        else:
            print('查無此訂單')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    system = FoodOrderingSystem()
    menu = system.menu

    menu.add_item('漢堡', '主餐', 100)
    menu.add_item('薯條', '點心', 40)
    menu.add_item('可樂', '飲料', 45, '中杯')

    while True:
        control = input("1.Admin(管理員)\n2.Member(會員)\n3.離開系統\n")
        if control == '1':
            clear()
            while True:
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
                    name = input('輸入客戶姓名: ')
                    '''
                    查詢客戶資料
                    '''
                    system.find_customer(name)

                elif control == '3':
                    clear()
                    while 1:
                        control = input('1.瀏覽所有訂單\n2.取消訂單\n3.Exit\n')
                        if control == '1':
                            system.show_orders()

                        elif control == '2':
                            id = int(input('輸入訂單編號: '))
                            if id in system.orders:
                                system.orders.pop(id)
                            else:
                                print('查無此訂單')

                        elif control == '3':
                            break

                elif control == '4':
                    break

        elif control == '2':
            clear()
            name, contact = input('請輸入姓名以及聯絡方式: ').split()
            if name not in system.customers:
                system.create_customer(name, contact)
                while True:
                    control = input('1.觀看菜單\n2.挑選商品\n3.送出訂單\n4.Exit\n')
                    if control == '1':
                        menu.show_menu()
                    elif control == '2':
                        shopping_list = input('輸入商品名稱: ').split()
                        system.create_order(name, shopping_list)
                    elif control == '3':
                        print('訂單已送出')
                    elif control == '4':
                        break
            else:
                print('顧客已存在')

            
        elif control == '3':
            break
    print('🍔感謝使用🍟')
