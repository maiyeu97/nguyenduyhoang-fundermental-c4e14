nums = [9, 34, 26, 23, 86, 49]
x = int(input("Enter number:"))
found = False
# FIND FIST:
# FIND ALL:
for index, num in enumerate(nums):
    if num == x:
        found_idex = index
        found = True
        break
if not found:
    print("Not Found")
else:
    print("Found {0} at {1}".format(x, index))
