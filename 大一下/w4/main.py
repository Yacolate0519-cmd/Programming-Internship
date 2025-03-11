class StudentCourse:
    def __init__(self , name , password , course_name , grade):
        self.name = name
        self.__password = password
        self.course_name = course_name
        self.__grade = grade

    def getter_password(self):
        return self.__password

    def setter_password(self , old_pass , new_pass):
        if old_pass != new_pass:
            print(self.__password)
            self.__password = new_pass
            print(f'密碼修改成功!\n{self.__password}')
        else:
            print("舊密碼不可與新密碼相同")

    def getter_grade(self , password):
        if password == self.__password:
            return f'Current grade: {self.__grade}'
        else:
            print('密碼錯誤\t不可查詢成績')
            return ''
        
    def setter_grade(self , password ,new_grade):
        if password == self.__password:
            if 0 <= new_grade <= 100:
                self.__grade = new_grade
                print('成績修改成功!')
            else:
                print('請輸入正確成績')
        else:
            print('密碼錯誤\t不可修改成績')

    def __str__(self):
        return f'{self.name} is taking [{self.course_name}] and has a grade of {self.__grade}'
    
if __name__ == '__main__':
    student = StudentCourse("Yacolate" , "950519" , "Data structer" , 50)

    print(student)
    student.setter_password('950519', "test123")

    print(student.getter_grade('test123'))

    print(student)
    student.setter_grade('test123',100)
    print(student)