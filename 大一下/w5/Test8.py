class Person:
    def __init__(self , age = 0):
        self.__age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self , age):
        if age >= 0:
            self.__age = age
        else:
            print('Error')
    
 

if __name__ == '__main__':
    person = Person(30)
    print(person.age)
    