favs = ['xinh','cute',"vui tinh",2014]
for i, fav in enumerate(favs):
    print(i + 1, fav, sep=". ")
fav = input("Nhap noi dung can xoa:")
# TODO: input validation
if fav in favs:
    favs.remove(fav)
    for i, fav in enumerate(favs):
        print(i + 1, fav, sep=". ")
else:
    print("not found")
