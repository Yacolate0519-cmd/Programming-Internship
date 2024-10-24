def find_sublist(nums,target):
    result = []
    for i in range(len(nums)):
        total = 0
        for j in range(i+1 , len(nums)):
            total += nums[j]
            if total >= target:
                result.append(nums[i:j+1])
    return result

nums = [2,1,5,1,3,2]
target = 7
print(find_sublist(nums,target))