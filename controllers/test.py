# from models.yt_scrap_model import db_details, test_insert
from flask import jsonify
from models.Models import Account, User, RequestLogs, SchedulerData, BaseModel
from configs.database import DB
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

def find_name(name):
    account = Account()
    data    = account.find_all({"name": name})
    return str(data)

def update_name(id, name):
    account = Account()
    data    = account.update({"_id": ObjectId(id)}, {'name': name})
    return str(data)

def delete_doc(id):
    account = Account()
    data    = account.delete({"_id": ObjectId(id)})
    # data    = account.delete({"name": "Subhojit"})
    return str(data)

def count_all():
    account = Account()
    data    = account.count({"name": "Avijit"})
    return str(data)

def distint_by_field(field):
    account = Account()
    data    = account.distinct(field)
    return str(data)

def insert_all():
    data=[{
        'name'    : "Avijit",
        'email'   : "TestEmailNew",
        'password': "TestPasswordXX"
    },{
        'name'    : "Subhojit",
        'email'   : "Email2",
        'password': "TestPassword"
    }]

    return {
        'id1' : Account().insert(data),
        'id2' : User().insert(data),
        'id3' : RequestLogs().insert(data),
        'id4' : SchedulerData().insert(data)
    }

def test_query():
    # DB        = BaseModel('accounts')
    # data      = DB.collection.find({"name":"Avijit"})
    db          = DB()
    data        = db.accounts.find({"name":"Avijit"})
    return_data = []

    for field in data:
        field['_id'] = str(field['_id'])
        return_data.append(field)

    return str(return_data)
