favs = ['xinh','cute',"vui tinh"]

for i, fav in enumerate(favs):
    print(i + 1, fav, sep=". ")
position = int(input("Nhap chi so can xoa:"))
# TODO: input validation
if position < 1 or position > len(favs):
    print("Our of range")
else:
    favs.pop(position - 1)
    for i, fav in enumerate(favs):
    print(i + 1, fav, sep=". ")
