def input_grades():
    grades = []
    while 1:
        x = int(input("輸入成績(輸入負數以結束):"))
        if 0 <= x <= 100:
            grades.append(x)
        else:
            break
    return grades
print('輸入的成績: ',input_grades())