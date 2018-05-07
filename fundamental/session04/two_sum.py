nums = [-1, 5, 7, 1, -5]
for i in range(0, len(nums)-1):
    x1 = nums[i]
    x2 = 0
    found = False
    for j in range(i + 1, len(nums)):
        if x1 + nums[j] == 0:
            x2 = nums[j]
            found = True
            break
    if found:
        print("Found {0} and {1}".format(x1, x2))
