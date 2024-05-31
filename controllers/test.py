# from models.yt_scrap_model import db_details, test_insert
from flask import jsonify
from models.Models import Account, User, RequestLogs, SchedulerData, BaseModel
from configs.database import DB
from bson import ObjectId
import random

def hello_world():
    return '<h1>Hello World</h1>'

def insert_test():
    print("Start")
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
    print("End")
    return str(id)

def find_all():
    account = Account()
    data = account.find_all({"name": "kalu"})
    print(data)
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
    data = {}
    return str({
        'id1' : Account().count(data),
        'id2' : User().count(data),
        'id3' : RequestLogs().count(data),
        'id4' : SchedulerData().count(data)
    })

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

def test_q():
    data = Account().delete_by_id("66582377a5d873d8b0b1e6e3")
    print(type(data))
    return str(data)

def insert_test_thread():
    print("Start")
    account = Account()
    id = account.insert_on_thread([{
        'name'    : "Avijit",
        'email'   : "TestEmailNew",
        'password': "TestPasswordXX"
    },{
        'name'    : "Subhojit",
        'email'   : "Email2",
        'password': "TestPassword"
    }])

    print("End")
    return f"insert_on_thread: {random.randint(1, 10)}"

def update_test_thread():
    print("Start")
    Account().update_on_thread({'name':"Subhojit"},{'name':"Subhojit Sinha"})
    print("End")
    return f"update_test_thread: {random.randint(1, 10)}"
def delete_test_thread():
    print("Start")
    Account().delete_on_thread({'name':"Avijit"})
    print("End")
    return f"delete_on_thread: {random.randint(1, 10)}"