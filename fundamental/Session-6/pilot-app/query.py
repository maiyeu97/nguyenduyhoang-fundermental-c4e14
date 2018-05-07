from mlab import mlab_connect
from models.service import Service
from flask import Flask, render_template

mlab_connect()

id_to_find = "5a362cd5181900136f1607f3"
# beth= Service.objects(id= id_to_find).fisrt() #regula
beth= Service.objects().with_id(id_to_find) #only id
if beth is None:
    print("Not Found")
else:
    print(beth.name)
    # beth.delete()    # delete
    beth.update(set_occupied = False) #inc
    beth.reload()
    print(beth.set_occupied)

# all_services = Service.objects()

# first_service = all_services[1]
# print(first_service.name)
