yob = int(input("nhap nam sinh cua ban"))
age = 2017 - yob

print("tuoi cua ban:",age)
if age < 10:
    print("baby")
elif age < 18:
    print("teenager")
else:
    print("adult")
