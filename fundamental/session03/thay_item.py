favs = ['girl xinh','girl cute',"girl vui tinh"]
# for i in  range(len(favs)):

for i, fav in enumerate(favs):
    print(i + 1, fav, sep=". ")
position = int(input("Nhap position can thay:"))
# TODO : input validation
new_fav = input("Replacing fav?")
favs[position - 1] = new_fav
for i, fav in enumerate(favs):
    print(i + 1, fav, sep=". ")
