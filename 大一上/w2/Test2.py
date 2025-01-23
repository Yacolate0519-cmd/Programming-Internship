import math 

x1 = float(input("請輸入第一個科目的成績:"))
x2 = float(input("請輸入第二個科目的成績:"))
x3 = float(input("請輸入第三個科目的成績:"))
x4 = float(input("請輸入第四個科目的成績:"))

avg = (x1 + x2 + x3 + x4) / 4
std = math.sqrt(((x1-avg)**2+(x2-avg)**2+(x3-avg)**2+(x4-avg)**2)/4)

print("平均成績為:",round(avg,2))
print("成績的標準差為:",round(std,2))