import numpy as np


def convolution(image , kernel):
    image_size = len(image)
    kernel_size = len(kernel)
    new_image_size = image_size - kernel_size + 1
    new_image = np.zeros((kernel_size,kernel_size))
    
    for i in range(new_image_size):
        for j in range(new_image_size):
            value = 0
            for k in range(kernel_size):
                for l in range(kernel_size):
                    value += image[i + k][j + l] * kernel[k][l]
                new_image[i][j] = value
    return new_image
m , n = map(int,input("Enter the size of matrix: ").split())

image = []
for _ in range(m):
    a = list(map(int,input().split()))
    image.append(a)
    
#印出輸入矩陣
# for i in range(m):
#     for j in range(n):
#         print(image[i][j], end = ' ')
#     print()
while 1:
    k = int(input("Input the size of kernel: "))
    if k % 2 == 0 or k > min(m,n):
        continue
    else:
        break
#輸入kernel
kernel = []
for _ in range(k):
    a = list(map(int,input().split()))
    kernel.append(a)


print(convolution(image,kernel))
# print(f'image_size = {len(image)}')
# print(f'kernel_size = {len(kernel)}')