weight = int(input("請輸入體重(公斤):"))
height = float(input("請輸入身高(公尺):"))

BMI = weight / (height**2)

print("你的BMI值為:",round(BMI,2))