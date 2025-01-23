data = list(int((input())))
# print(data)
def reverse(x):
    for i in range(len(data)):
        if data[i] == data[len(data) - i - 1]:
            continue
        else:
            return False
    return True

if reverse(data):
    print("True")
else:
    print("False")
