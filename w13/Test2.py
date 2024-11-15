import numpy as np
def convolution(data,kernel):
    image_height , image_width = 5,5
    kernel_height , kernel_width = 3,3
    output_height = image_height - kernel_width + 1
    output_width = image_height - kernel_width + 1
    output = np.zeros((output_height , output_width))
    for i in range(output_height):
        for j in range(output_width):
            temp = data[i : i + kernel_height][j : j + kernel_width]    
            output[i][j] = np.sum(temp * kernel)
    return output
    
m , n = map(int,input("輸入長和寬: ").split())

data = []

for _ in range(m):
    a = list(map(int,input().split()))
    data.append(a) 
print('-----')

kernel = [[1,0,-1],
          [1,0,-1],
          [1,0,-1]]

#印出matrix
# for i in range(m):
#     for j in range(n):
#         print(data[i][j],end =' ')
#     print()

print(convolution(data,kernel))