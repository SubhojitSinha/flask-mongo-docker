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

def DB():
    return mongo.db