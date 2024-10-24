nums = [1,2,3,4,5,6]

data = []

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        data.append(nums[i]**2)
print(data)    
    