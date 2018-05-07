nums = [2, 23, 64, 98, 29, 10, 94]
n = int(input("nhap so ban tim:"))
lo = nums[0]
hi = len(nums)
while hi 
    mid = (lo + hi)/2
    num = nums[mid]
    if n == num:
        found = True
        print("found")
        break
    elif n < num:
        hi = mid + 1
        print("left")
    else:
        lo = mid
        print("right")
