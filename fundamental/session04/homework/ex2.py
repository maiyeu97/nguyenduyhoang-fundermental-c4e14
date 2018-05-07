numbers = [1, 6, 8, 1, 2, 1, 5, 6]
x = int(input("ENTER A NUMBER:"))
n = 0
ex = False
found = False

for i in range(len(numbers)):
    if x == numbers[i]:
        found = True
         n += 1
        ex = True

if ex == True:
    print("{0} appears {1} time(s) in my list.".format(x, appear))
else:
    print("Not Found")
