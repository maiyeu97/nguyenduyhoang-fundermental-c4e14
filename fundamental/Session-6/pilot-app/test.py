from mlab import mlab_connect
from models.service import Service
from flask import Flask, render_template

mlab_connect()

female_heigths = Service.objects(female = 0, height__gte= 160)
print(female_heigths)

first_female_160 = Service.objects(female = 0, height__gte= 160).fisrt()
print(first_female_160)

# avail_f_160 =
