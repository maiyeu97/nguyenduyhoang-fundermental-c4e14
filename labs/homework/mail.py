from gmail import GMail, Message
from random import choice
import datetime
import time

html_contents =[
'''<h>Hom nay em bi {{sickness}} em xin nghi hom nay !</h>'''
]
sickness_list = [
    "cam lanh",
    "sot cao",
    "ebola",
    "thuong han"
]
html_content_template = choice(html_contents)
sickness = choice(sickness_list)
html_content = html_content_template.replace("{{sickness}}", sickness)
gmail = GMail('hoang12zx@gmail.com', 'hoangcon97')
message = Message("Don xin nghi om", to="hoang12zx@gmail.com", html=html_content)

While True:
    if now.hour == 7:
        send = gmail.send(message)
    else:
        break
