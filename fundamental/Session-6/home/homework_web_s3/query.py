from mlab import mlab_connect
from models.service import River
from flask import Flask, render_template

mlab_connect()

# continents = River.objects(continent ='Africa')
# print(continents)

continents1000 = River.objects(continent ='S. America', length__gte= 1000)
print(continents1000)
