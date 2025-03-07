# 使用Getter來獲取私有屬性
import hashlib

class User:
    def __init__(self , name , password , email):
        self.name = name 
        self.__password = password
        self.email = email

    def set_password(self , password):
        self.__password = password

    def get_password(self):
        return self.__password

    def verify_password(self , password_attempt):
        return self.__password == self.__hashPW(password_attempt)  

    def __str__(self):
        return (f'Name: {self.name}\nPass: {self.__password}\nEmail: {self.email}')


if __name__ == '__main__':
    user = User("Yacolate", "950519", "yacolate0519@gmail.com")

    print(user.get_password())