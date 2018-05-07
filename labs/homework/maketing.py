from pymongo import MongoClient
client =  MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")
db = client.get_default_database()
customers = db["customers"]
datas = customers.find()
# print(datas[0])
for post in datas:
    value = (post['ref'])
    print(value)
