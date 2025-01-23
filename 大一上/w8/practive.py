def check(nums,target):
    data = []
    total = 0
    for i in range(len(nums)):
        total = 0
        for j in range(i + 1 , len(nums)):
            total += nums[j]
            if total >= target:
                data.append(nums[i:j+1])   
    return data

nums = [2,1,5,1,3,2]
target = 7

print(check(nums,target))