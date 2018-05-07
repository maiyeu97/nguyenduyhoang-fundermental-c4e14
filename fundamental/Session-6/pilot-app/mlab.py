import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds159866.mlab.com:59866/muadongkhonglanh

host = "ds159866.mlab.com"
port = 59866
db_name = "muadongkhonglanh"
user_name = "admin"
password = "admin"


def mlab_connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
