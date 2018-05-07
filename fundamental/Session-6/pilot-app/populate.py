from mlab import mlab_connect
from models.service import Service
from faker import Faker
from random import choice, randint

service_faker = Faker()
mlab_connect()
Service.drop_collection()
for _ in range(30):
    service = Service(name= service_faker.name(),
                    yob=randint(1995, 2000),
                    gender =randint(0, 1),
                    height=randint(140, 170),
                    occupied=choice([False, True]),
                    phone="12345")
    service.save()
