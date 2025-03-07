class Book:
    def __init__(self , title , publisher , price , isbn):
        self.__title = title
        self.publisher = publisher
        self.price = price
        self.isbn = isbn
        self.pub_date = "mmddyy"

    def __str__(self):
        return f'Title: {self.__title}\nprice: {self.price}'

    def setTitle(self, newTitle):
        self.__title = newTitle

    def getISBN(self):
        return self.isbn
    
    bk = property(getISBN , setTitle) #不傳東西就是前面 傳入內容就是後面

book1 = Book("python" , 'GoTop' , 483 , '123456789')
book1.__str__()
print('Book price is {}'.format(book1.price))
print('Book publication date is {}'.format(book1.pub_date))

book1.bk = 'Java Programming'
print(book1.bk)

print('--'*30)
print(book1.__str__())
