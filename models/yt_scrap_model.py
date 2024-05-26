from flask import Flask, jsonify
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
from os import environ

load_dotenv()

mongo_user = environ.get('MONGO_USERNAME')
mongo_pass = environ.get('MONGO_PASSWORD')
mongo_host = environ.get('MONGO_HOST')
mongo_port = environ.get('MONGO_PORT')
mongo_db   = environ.get('MONGO_DB')
mongo_url  = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}/{mongo_db}"
client     = MongoClient(mongo_url)
db         = client[mongo_db]

# app = Flask(__name__)

# class yt_scrap(db.Model):
#     __tablename__        = 'youtube_scrap'
#     id                   = db.Column(db.Integer, primary_key=True)
#     playlist_id          = db.Column(db.String(255), nullable=True)
#     playlist_url         = db.Column(db.Text, nullable=False)
#     download_type        = db.Column(db.Enum("audio", "video"), nullable=False, default="audio")
#     channel_id           = db.Column(db.String(255), nullable=False)
#     channel_name         = db.Column(db.String(255), nullable=False)
#     channel_url          = db.Column(db.Text, nullable=False)
#     video_id             = db.Column(db.String(255), nullable=False)
#     video_title_original = db.Column(db.Text, nullable=False)
#     video_title_final    = db.Column(db.Text, nullable=False)
#     video_url            = db.Column(db.Text, nullable=False)
#     video_duration       = db.Column(db.String(10), nullable=False)
#     meta_title           = db.Column(db.Text, nullable=False)
#     meta_artist          = db.Column(db.String(255), nullable=False)
#     meta_genre           = db.Column(db.String(255), nullable=False)
#     meta_album           = db.Column(db.String(255), nullable=False)
#     is_synced            = db.Column(db.Boolean, nullable=False, default=False)
#     need_cleaning        = db.Column(db.Boolean, nullable=False, default=False)
#     need_cleaning        = db.Column(db.Boolean, nullable=False, default=False)
#     meta_release_date    = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     collected_at         = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     synced_at            = db.Column(db.DateTime, nullable=False)
#     cleaned_at           = db.Column(db.DateTime, nullable=False)
#     artwork_collected_at = db.Column(db.DateTime, nullable=False)


def test_insert():
    user_id = db.users.insert_one({
        "name": "Test",
        "email": "TestEmail"
    }).inserted_id
    new_user = db.users.find_one({"_id": user_id})
    new_user["_id"] = str(new_user["_id"])

    return jsonify(new_user), 201

def db_details():
    return {
        'mongo_user' :mongo_user,
        'mongo_pass' :mongo_pass,
        'mongo_host' :mongo_host,
        'mongo_port' :mongo_port,
        'mongo_url'  :mongo_url,
    }
