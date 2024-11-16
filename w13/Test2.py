import numpy as np

def convolution(data, kernel):
    img_size = data.shape[0]
    kernel_size = kernel.shape[0]
    print(f'data_shape = {data.shape[0]}')
    print(f'kernel_shape = {kernel.shape[0]}')
    new_img_size = img_size - kernel_size + 1
    new_img = np.zeros((new_img_size , new_img_size))
    
    for i in range(new_img_size):
        for j in range(new_img_size):
            value = 0
            for k in range(kernel_size):
                for l in range(kernel_size):
                    value += data[i+k][j+l] * kernel[k][l]
                new_img[i][j] = value
    return new_img

# 輸入圖像尺寸
m, n = map(int, input("輸入長和寬: ").split())

# 讀取圖像數據
data = []
for _ in range(m):
    a = list(map(int, input().split()))
    data.append(a)

print('----------')

for i in range(m):
    for j in range(n):
        print(data[i][j], end = ' ')
    print()

# 轉換為 NumPy 陣列
data = np.array(data)

# 定義 kernel
kernel = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

# 印出結果
print('-----')
print(convolution(data, kernel))

    