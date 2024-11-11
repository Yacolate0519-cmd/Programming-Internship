# 讀取輸入數據
n = int(input("輸入影片數量: "))
# data = []
matrix = []

for i in range(n):
    matrix.append(list(input().split()))
# rows = data.strip().split('\n')

# # print(rows)

# matrix = []
# for row in rows:
#     item = row.split()
#     matrix.append([item[0]]+list(map(int,item[1:])))

#print(matrix) 印出matrix


Dic_sort = {}

# for i in range(len(matrix)):
#     for j in range(1,len(matrix[i])):
#         Dic_sort[matrix[0]] = matrix[i][j]
# data = 1
# data = matrix[0][1] * matrix[0][2] * matrix[0][3]
# Dic_sort['A-FU'] = data
# print(Dic_sort)


for i in range(len(matrix)):
    data = 1
    for j in range(1,len(matrix[i])):
        data *= int(matrix[i][j])
        Dic_sort[matrix[i][0]] = data

# print(Dic_sort)

print('---'*30)
rank = sorted(Dic_sort,reverse = True)

for i in rank:
    print(i)