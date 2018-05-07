# 2.1
size =[5, 7, 300, 90, 24, 50, 75]
m = int(max(size))   # Flock max in size
n = size.index(m)
for i, fav in enumerate(size):
    print(i + 1, fav, sep=". ")
#2.2*************************************************
print("Bạn muốn bán cừu!")
yes = ['y']
no = ['n']
fav = input("nhap y/n:")
if fav in yes:
    print("Flock max:",m)
    size.remove(m)
    for i, fav in enumerate(size):

        print(i + 1, fav, sep=". ")
# 2.3 ***********************************************
    default = 8
    default = True
    while True:
        default = int(input("Thay cho Flock max:"))
        if default != 8:
            print("Nhap lai(=8):")
        else:
            size.insert(n, default)
            size[n] = default
            break
    for i, fav in enumerate(size):
        print(i + 1, fav, sep=". ")
# 2.4************************************************
    print("Một ngày đẹp trời.")
    increase = int(input("Nhap increase:"))
    for i in range(len(fav)):
        print(i + 1, fav, sep=". ")
#**************************************************
elif fav in no:
    print("Thịt à.Thịt xong gọi nhé có chai rượu ngon nè.")
else:
    print("Nhap lai(y/n):")
