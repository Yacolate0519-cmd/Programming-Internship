class User:
    def __init__(self , name , password , email):
        self.name = name 
        self.__password = password
        self.email = email

    def set_password(self , password):
        self.__password = password

    def verify_password(self , password_attempt):
        return (self.__password == password_attempt)    

    def __str__(self):
        return (f'Name: {self.name}\nPass: {self.__password}\nEmail: {self.email}')


if __name__ == '__main__':
    user = User("Yacolate", "950519", "yacolate0519@gmail.com")
    print(user) #呼教__str__內容

    print("Change Password")
    user.password = "Test123"
    print(user.verify_password("Test123"))
    

