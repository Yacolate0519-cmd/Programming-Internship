n = int(input("輸入影片數量: "))
matrix = []

for i in range(n):
    matrix.append(list(input().split()))

Dic_sort = {}
for i in range(len(matrix)):
    data = 1
    for j in range(1,len(matrix[i])):
        data *= int(matrix[i][j])
        Dic_sort[matrix[i][0]] = data

print(Dic_sort)

print('---'*30)
rank = sorted(Dic_sort.items(), key=lambda item: item[1], reverse=True)

for key , value in rank:
    print(key)
