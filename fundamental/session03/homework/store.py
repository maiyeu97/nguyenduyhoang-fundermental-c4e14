print("STORE")
items = ['T-shirt','Sweater']

for i, fav in enumerate(items):
    print(i + 1, fav, sep=". ")
fav = input("Nhap noi dung can them:")
if fav in items:
    print("Duplicate items")
else:
    items.insert(2, "Jeans")
    for i, fav in enumerate(items):
        print(i + 1, fav, sep=". ")
# RELACING

position = int(input("Nhap vao chi so can thay:"))
new_items = input("Noi dung thay the:")
items[position - 1] = new_items
for i, fav in enumerate(items):
        print(i + 1, fav, sep=". ")

# DELETE:
position = int(input("Nhap chi so can xoa:"))
# TODO: input validation
items.pop(position - 1)
for i, fav in enumerate(items):
    print(i + 1, fav, sep=". ")
