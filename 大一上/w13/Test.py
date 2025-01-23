import numpy as np

def convolution_2d(image, kernel):
    # 取得圖像和濾波器的尺寸
    img_height, img_width = image.shape
    kernel_height, kernel_width = kernel.shape

    # 計算輸出圖像的尺寸
    output_height = img_height - kernel_height + 1
    output_width = img_width - kernel_width + 1
    output = np.zeros((output_height, output_width))

    # 用雙層 for 迴圈執行卷積操作
    for i in range(output_height):
        for j in range(output_width):
            # 取出圖像中與濾波器大小相同的子矩陣
            region = image[i:i+kernel_height, j:j+kernel_width]
            # 對子矩陣與濾波器進行逐元素乘積並求和
            output[i, j] = np.sum(region * kernel)
    
    return output

# 測試範例
image = np.array([
    [2,1,0,2,3],
    [9,5,4,2,0],
    [2,3,4,5,6],
    [1,2,3,1,0],
    [0,4,4,2,8]
])

kernel = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

output = convolution_2d(image, kernel)
print("Output after convolution:\n", output)
