from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from os import environ

load_dotenv()

mongo_db   = environ.get('MONGO_DB')
mongo_host = environ.get('MONGO_HOST')
mongo_port = environ.get('MONGO_PORT')
mongo_user = environ.get('MONGO_USERNAME')
mongo_pass = environ.get('MONGO_PASSWORD')
mongo_url  = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}/{mongo_db}?authSource=admin"

app = Flask(__name__)
app.config["MONGO_URI"] = mongo_url

mongo = PyMongo(app)
db    = mongo.db

class BaseModel:

    collection_name = ''

    def __init__(self, collection_name):
        self.collection_name = collection_name

    def insert(self, data):
        if type(data) == dict:
            return db[self.collection_name].insert_one(data).inserted_id
        elif type(data) == list:
            return db[self.collection_name].insert_many(data).inserted_ids
        else:
            return None

    def update(self, search, data, update_all=False):
        if update_all:
            return db[self.collection_name].update_many(search, {'$set': data}).modified_count
        else:
            return db[self.collection_name].update_one(search, {'$set': data}).modified_count

    def get_all(self, limit=0, skip=0):
        data = db[self.collection_name].find()
        if limit > 0:
            data = data.limit(limit)
        if skip > 0:
            data = data.skip(skip)

        return_data = []
        for field in data:
            field['_id'] = str(field['_id'])
            return_data.append(field)

        return return_data

    def delete(self, search):
        return db[self.collection_name].delete_many(search).deleted_count

    def find_all(self, filter, skip=0, limit=0):
        data = db[self.collection_name].find(filter)
        if limit > 0:
            data = data.limit(limit)
        if skip > 0:
            data = data.skip(skip)

        return_data = []
        for field in data:
            field['_id'] = str(field['_id'])
            return_data.append(field)

        return return_data


    def find_one(self, filter):
        return db[self.collection_name].find_one(filter)

    def count(self, filter):
        return db[self.collection_name].count_documents(filter)

    def distinct(self, field):
        return db[self.collection_name].distinct(field)
