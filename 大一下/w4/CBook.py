class CBook:
    objcount = 0
    def __init__(self , title , publisher , cost_price , isbn):
        self.__profit_rate = 1.3
        self.title = title
        self.publisher = publisher
        self.__cost_price = cost_price
        self.__price = self.__cost_price * self.__profit_rate
        self.isbn = isbn
        self.pub_data = 'mmddyy'
        CBook.objCountAdd()
    
    @staticmethod
    def objCountAdd():
        CBook.objCount += 1

    @staticmethod
    def getObjCount():
        return CBook.objcount
    
    @property
    def profit_rate(self):
        return "No data"

    @profit_rate.setter
    def setPR(self , newProfitRate):
        self.__profit_rate = newProfitRate

    @profit_rate.getter
    def getPR(self):
        return self.__profit_rate
    
    @property
    def price(self):
        return self.__price
    
    def setTitle(self):
        return self.title
    