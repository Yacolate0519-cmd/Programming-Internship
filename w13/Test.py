def decimal_to_binary(n):
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        result = str(n % 2) + result 
        n //= 2
    return result 

def binary_to_decimal(binary_str):
    decimal = 0  # 用來儲存十進位結果
    length = len(binary_str)

    # 從右到左逐位處理二進位數字
    for i in range(length):
        # 取得每一位的數字，將其轉換為整數
        bit = int(binary_str[length - 1 - i])
        # 計算該位的十進位值，並加入總和
        decimal += bit * (2 ** i)

    return decimal
a = '11'
b = '1'

A = binary_to_decimal(a)
B = binary_to_decimal(b)


data = int(A) + int(B)

print(data)

print(decimal_to_binary(data))