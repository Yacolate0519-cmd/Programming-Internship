# 讀取輸入數據
n = int(input("輸入影片數量: "))
data = []

for i in range(n):
    data = input().split()
    name = data[0]
    viewers = int(data[1])
    avg_watch_time = int(data[2])
    duration = int(data[3])
    relevance = int(data[4])
    
    recommand = viewers * avg_watch_time * duration * relevance
    data.append(data)

print(data)