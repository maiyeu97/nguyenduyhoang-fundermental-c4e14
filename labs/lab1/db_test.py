from pymongo import MongoClient

# 1. Connect to database
client =  MongoClient("mongodb://hoang12zx:hoangcon97@ds137141.mlab.com:37141/c4e14-hoangcon97")

# 2. Get default database
db = client.get_default_database()

# 3. Get collection
blog=db["mongo"]

# # 4. Insert document
# new_post = {
# 'title': "Hom nay troi dep"
# 'content'
# }
# blog.insert_one(new_post)
posts = blog.find() #GET ALL post in blog
# # print(post[0])
# # for post in posts:
# #     print(post[0])
# for post inposts:
    # print(post)
