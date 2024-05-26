# from models.yt_scrap_model import db_details, test_insert
from flask import jsonify
from models.Account import Account
from bson import ObjectId
def hello_world():
    return '<h1>Hello World</h1>'

def init_database():
    account = Account()
    id = account.insert([{
        'name'    : "Avijit",
        'email'   : "TestEmailNew",
        'password': "TestPasswordXX"
    },{
        'name'    : "Subhojit",
        'email'   : "Email2",
        'password': "TestPassword"
    }])
    print(id)
    return str(id)

def get_all():
    account = Account()
    data = account.get_all()
    return jsonify(data)

def get_all_3():
    account = Account()
    data = account.get_all(limit=3,skip=0)
    return jsonify(data)


def update_name(id, name):
    account = Account()
    data    = account.update({"_id": ObjectId(id)}, {'name': name})
    return str(data)