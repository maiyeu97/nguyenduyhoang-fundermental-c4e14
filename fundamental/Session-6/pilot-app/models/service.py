from mongoengine import Document, StringField, IntField, BooleanField
class Service(Document):
    name = StringField()
    yob = StringField()
    gender = IntField() #: Female,  1: Female
    height = StringField() # cm
    phone = StringField()
    occupied = BooleanField()

    def __str__(self):
        return self.name
