nums = [3,3]
target = 6
pop_index = []
for i in range(len(nums)):
    print(target)
    if target >= nums[-i + len(nums)-1]:
        print('loop')
        target -= nums[-i + len(nums)-1]
        print(target)
        print('Index:',nums.index(nums[-i + len(nums)-1]))
        print()
        pop_index.append(nums.index(nums[-i + len(nums)-1]))
pop_index.sort()
print(pop_index)

