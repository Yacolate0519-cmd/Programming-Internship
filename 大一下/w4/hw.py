class CStudent:
    
    total_student = 0

    def __init__(self , id , name , department , email , birthday , courses):
        self.id = id 
        self.name = name
        self.department = department
        self.__email = email
        self.__birthday = birthday
        self.__courses = courses
        self.add_total_student()

    def __str__(self):
        return ('--'*30+'\n'+f'ID : {self.id}\nName: {self.name}\nDepartment: {self.department}\nEmail: {self.__email}\nBirthday: {self.__birthday}\nCourses: {self.__courses}\n'+'--'*30)

    @staticmethod 

    def decrease_student():
        CStudent.total_student -= 1

    def __del__(self):
        CStudent.decrease_student()

    @classmethod
    def add_total_student(cls):
        cls.total_student += 1 

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self , new_email):
        if new_email == self.__email:
            print('新信箱不可與舊信箱相同')
        else:
            self.__email = new_email
    
    @property
    def birthday(self):
        return self.__birthday
    
    @birthday.setter
    def birthday(self , date):
        if date == self.__birthday:
            print('新日期不可與舊日期相同')
        else:
            self.__birthday = date
    
    @property 
    def courses(self):
        return self.courses
    
    def update_courses(self , control , course , score = None):
        if control == 'add':
            if course not in self.__courses:
                self.__courses[course] = score
            else:
                print('此科目已存在，您是否想要更新成績')

        elif control == 'update':
            if course in self.__courses:
                self.__courses[course] = score
            else:
                print('此科目不存在')

        elif control == 'remove':
            if course in self.__courses:
                self.__courses.pop(course)
            else:
                print('此科目不存在')

        else:
            print('輸入錯誤')
            



if __name__ == '__main__':
    student1 = CStudent('S109102345' , '張三' , 'IECS' , 'zs100232@gmail.com' , '2000-02-02' ,
                        {'基礎程式' : 95 , '數學' : 88 , '專題實務' : 75})

    student2 = CStudent('S109104533' , '李四' , 'IECS' , 'ktr002222@gmail.com' , '2004-03-22',
                        {'基礎程式' : 65 , '數學' : 98 , '專題實務' : 88 , '大數據分析' : 75})
    student3 = CStudent('S109123346' , '王五' , 'EE' , 'zs1543232@gmail.com' , '1999-04-22',
                        {'基礎程式' : 65 , '數學' : 98 , '專題實務' : 88 , '大數據分析' : 75})
    student4 = CStudent('S109102355' , '趙雲' , 'CE' , 'zkkse0252@gmail.com' , ' 2001-05-10',
                        {'基礎程式' : 65 , '數學' : 98 , '專題實務' : 88 , '大數據分析' : 75})
    student5 = CStudent('S109102785' , '李白' , 'AI' , 'zsf23s3d@gmail.com' , '2002-06-04',
                        {'基礎程式' : 65 , '數學' : 98 , '專題實務' : 88 , '大數據分析' : 75})
    
    print(student1)
    
    print('--'*13+'添加國文成績以及修改生日日期'+'--'*14)

    student1.birthday = '2006-05-19'
    student1.update_courses('add' , '國文' , 100)
    print(student1)

    print('--'*13+'更新基礎程式成績'+'--'*14)
    student1.update_courses('update' , "基礎程式" , 100)
    print(student1)

    print('--'*13+'移除專題成績'+'--'*14)
    student1.update_courses('remove' , '專題實務')
    print(student1)
    print('\n')
    print('--'*13+'使用靜態方法修改類別屬性'+'--'*14)
    print(f'目前學生總數: {CStudent.total_student}')
    print('--修改--')
    del student1
    print(f'目前學生總數: {CStudent.total_student}')
    