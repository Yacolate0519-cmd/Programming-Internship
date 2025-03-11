class Book:
    def __init__(self , title , author , isbn , pages , available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pages = pages
        self.available = available

    def book_info(self):
        print(f'Title = {self.title},\nAuthor = {self.author}\nIsbn = {self.isbn}\nPages = {self.pages}\nAvailable = {self.available}')

    def borrow_book(self):
        if self.available:
            print('已借閱')
            self.available = False
        else:
            print('此書不可借閱')

    def return_book(self):
        self.available =  True
        print("歸還成功")

Harry_Potter = Book('eposide 1' , 'JK' , '123456789' , 365 , False)
Harry_Potter.book_info()