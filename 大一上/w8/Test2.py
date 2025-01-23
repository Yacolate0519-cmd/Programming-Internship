def check(nums,ranges):
    result = set()
    for start , end in ranges:
        result.update(nums[start:end])
    return sorted(result)

nums = [10,20,30,40,50,60,70,80]
ranges = [(1,4),(3,6),(5,8)]

print(check(nums,ranges))