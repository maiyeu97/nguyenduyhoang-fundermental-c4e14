# n = int(input("Nhap so hang:"))
# m = int(input("Nhap so cot:"))
from random import randint
n = randint(1, 20)
m = randint(1, 20)
for j in range(m):
    for i in range(n):
        if (i +j)%2 == 0:
            print("*", end=" ")
        else:
            print("x", end=" ")
    print()
