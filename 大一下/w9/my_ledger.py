import pandas as pd 

from simple_ledger import SimpleLedger

class MyLedger(SimpleLedger):
    def __init__(self):
        super().__init__() 

    def list_transcations(self):
        df = pd.DataFrame(self.transcations , columns = ['Amount' , 'Description' , 'Date' , 'Category'])
        print(df)

    def record(self , amount , description , date , category):
        self.transcations.append((amount , description , date , category))

    def list_by_date(self , start , end):
        df = pd.DataFrame(self.transcations , columns = ['Amount' , 'Description' , 'Date' , 'Category'])
        range = (df['Date'] >= start) & (df['Date'] <= end)
        print(df.loc[range])

    def sum_by_category(self, category):
        df = pd.DataFrame(self.transcations, columns=['Amount', 'Description', 'Date', 'Category'])
        range = df[df['Category'] == category]
        total = range['Amount'].sum()
        return total


    def export_csv(self , filepath = 'result.csv'):
        df = pd.DataFrame(self.transcations, columns=['Amount', 'Description', 'Date', 'Category'])
        df.to_csv(filepath, index=False)

if __name__ == "__main__":
    test = MyLedger()
    test.record(82 , '開箱子' , "4/28" , '娛樂')
    test.record(75 , '早餐' , '4/29' , '飲食')
    test.record(150 , '晚餐' , '4/30' , '飲食')
    test.record(130 , '晚餐' , '4/31' , '飲食')
    test.record(65 , '火車' , '4/31' , '交通')
    test.record(30 , '公車' , '4/31' , '交通')

    while 1:
        print('--'*15)
        choice = int(input("1.新增交易\n2.查花費\n3.列明細\n4.輸出csv\n5.離開: "))
        if choice == 1:
            amount = float(input("金額: "))
            desc = input("描述: ")
            date = input("日期: ")
            cate = input('類別: ')
            test.record(amount, desc, date, cate)

        if choice == 2:
            print(f"目前花費: {test.get_balance()}")
        
        if choice == 3:
            print('--'*15)
            while 1:
                temp = int(input("1.全部明細: \n2.根據日期查詢: \n3.離開: "))
                if temp == 1:
                    print('--'*15)
                    test.list_transcations()
                    print('--'*15)

                if temp == 2:
                    print('--'*15)
                    start = input("開始日期: ")
                    end = input('結束日期: ')
                    test.list_by_date(start , end)
                    print('--'*15)
                if temp == 3:
                    break

        if choice == 4:
            test.export_csv()
            print('以輸出成csv檔')
        
        if choice == 5:
            print("感謝使用")
            break
