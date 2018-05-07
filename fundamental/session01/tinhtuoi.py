# Ham thoi gian:
import time

yob = input("Nhap nam sinh cua ban:")
year = time.localtime()
age = year[0] - int(yob)

print("tuoi cua toi la:", age)
