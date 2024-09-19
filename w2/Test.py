total = int(input("輸入總秒數:"))
second = total % 60
minute1 = total // 60
minute2 = minute1 
hour = minute2  // 60
minute1 = minute2 % 60

print(hour,"小時",minute1,"分鐘",second,"秒")