nums = [0,1,2,2,3,0,4,2]
left = 0
right = len(nums) - 1 
val = 2

while left < right:
    if nums[left] == val:
        nums[left] , nums[right] = nums[right] , nums[left]
    while nums[left] != val:
        left += 1
    while nums[right] == val:
        right -= 1
count = 0
for i in nums:
    if i != val:
        count += 1
print(count)