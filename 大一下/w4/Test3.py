import hashlib

class User:
    def __init__(self , name , password , email):
        self.name = name 
        self.__password = self.__hashPW(password)
        self.email = email

    def set_password(self , password):
        self.__password = password

    def __hashPW(self , password):
        # hashlib.sha256 是一種加密方法
        return hashlib.sha256(password.encode()).hexdigest

    def verify_password(self , password_attempt):
        return self.__password == self.__hashPW(password_attempt)  

    def __str__(self):
        return (f'Name: {self.name}\nPass: {self.__password}\nEmail: {self.email}')


if __name__ == '__main__':
    user = User("Yacolate", "950519", "yacolate0519@gmail.com")
    print(user) #呼教__str__內容

    print("Change Password")
    
    # user.__hashPW("Test123")

    print(user.__password)# 私有屬性抓不到

    print(user)
