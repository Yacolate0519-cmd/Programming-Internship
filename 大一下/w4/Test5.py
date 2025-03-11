# 使用Setter修改私有屬性
import hashlib

class User:
    def __init__(self , name , password , email):
        self.name = name 
        self.__password = password
        self.email = email

    def set_password(self , newPassword):
        if self.verify_password(newPassword):
            print("error, 新密碼不可與舊密碼相同")
        else:
            self.__password = newPassword
            print('修改成功')

    def get_password(self):
        return self.__password

    def __hashPW(self , password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self , password_attempt):
        return self.__hashPW(self.__password) == self.__hashPW(password_attempt)

    def __str__(self):
        return (f'Name: {self.name}\nPass: {self.__password}\nEmail: {self.email}')


if __name__ == '__main__':
    user = User("Yacolate", "950519", "yacolate0519@gmail.com")
    print(user)
    print(user.get_password())

    print(user.get_password())
    
    user.set_password("950519")
    user.set_password("Test123")