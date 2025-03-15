class Book:
    def __init__(self , title , price):
        self.title = title
        self.price = price

if __name__ == '__main__':
    book = Book('Python Programming' , 100)
    try:
        print(book.title)
        print(book.price)
        print(book.author)
        print(3 / 0)
    except AttributeError as e:
        print(e)
    
    except ZeroDivisionError as e1:
        print(e1)
    else:
        print('No expection')