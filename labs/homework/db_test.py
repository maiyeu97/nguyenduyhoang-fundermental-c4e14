from pymongo import MongoClient
client =  MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")
db = client.get_default_database()
data = db["posts"]
post = {
    'title': "Leonardo da Vinci",
    'author': "Hoàng Ngyễn",
    'content': 'Dù chỉ nắm vững một kiến thức nào đó, cũng đều có ích cho trí óc, nó sẽ ném đi những thứ vô dụng nhưng giữ lại những thứ có ích'
}
data.insert_one(post)
# data.remove(post)
