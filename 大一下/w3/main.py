class Student:
    def __init__(self , student_id , name , age , grades):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self , subject , grade):
        self.grades[subject] = grade

    def get_average(self):
        n = len(self.grades)
        total = 0
        for i in self.grades.values():
            total += i
        avg = total / n
        print(f'平均成績為: {avg}')

    def display_info(self):
        print('學生資訊: ')
        print(f'姓名: {self.name}')
        print(f'學號: {self.student_id}')
        print(f'年齡: {self.age}')
        

    def display_grades(self):
        print(f'學生: {self.name}')
        for key , value in self.grades.items():
            print(f'科目: {key}, 成績: {value}')
        print('--' * 30)


if __name__ == '__main__':
    students = {
        'D1345490': Student('D1345490' , '黃軍博' , 18 , {'Math': 100, 'English': 100}),
        'D1382890': Student('D1382890' , '張彥堂' , 23 , {'Math': 85, 'English': 90}),
        'D1345487': Student('D1345487' , '忘記了' , 18 , {'Math': 95 , 'English': 100})
    }

    while 1:
        control = int(input("1.新增或修改成績\n2.顯示學生平均成績\n3.顯示學生基本資訊與所有科目成績\n4.離開系統\n"))
        if control == 1:
            student_id , subject , grade = input('輸入修改學生學好、科目以及成績: ').split()
            grade = int(grade)
            student = students.get(student_id)

            if student:
                student.add_grade(subject , grade)
            else:
                print('查無此人')

        elif control == 2:
            student_id = input('輸入學號: ')
            student = students.get(student_id)
            if student:
                student.get_average()
            else:
                print('查無此人')

        elif control == 3:
            student_id = input('輸入學號: ')
            student = students.get(student_id)
            if student:
                student.display_info()
                student.display_grades()
            else:
                print('查無此人')

        elif control == 4:
            break
