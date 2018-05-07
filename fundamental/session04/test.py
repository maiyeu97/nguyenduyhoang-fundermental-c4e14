# lol = ["Tuan Anh", 22, "Moc Chau", True, 4, 20]
# tuananh = {
# }
# dictionary

# tuananh = {
#     "name":"Tuan Anh"
# }

tuananh = {
    "name":"Tuan Anh",
    "age": 22,
    "home": "Moc Chau",
    "in_relationship": True,
    "project": 4
}
print(*tuananh)
# dictionary

# print(tuananh)
# print(tuananh["home"])
# x = True

tuananh["home"] = False
print(tuananh)

tuananh["project"] +=1
print(tuananh)

tuananh["extra_house"] = 20
print(tuananh)

del tuananh["in_relationship"]
print(tuananh)
