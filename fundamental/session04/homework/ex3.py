prime = False

ex = int(input("Nhap so thu: "))
if ex < 2:
    print(ex, "Ko la so nguyen.")
elif ex == 2:
    print("2 .La so nguyen.")
for i in range(2, ex):
    if ex % i == 0:
        print(test, "Ko la so nguyen.")
        break
elif ex == i + 1:
        print(test, "La so nguyen.")
