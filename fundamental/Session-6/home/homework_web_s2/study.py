1. Khong co id trung lap
2. id, name, yob, gender, phone, height, occupied

Find_id?
find_1 = docs.objects.get(id="5a362c56ff9a0608286a2045")
find_2 = docs.objects(id="5a362c56ff9a0608286a2045")
remove?
docs.objects(query = ?).delete()
Ex: docs.objects(name= "Nam").delete()
