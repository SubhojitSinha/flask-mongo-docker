from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)


def get_db():
    client = MongoClient(
        host='test_mongodb',
        port=27017,
        username='root',
        password='pass',
        authSource='admin'
    )
    return client['animal_db']

@app.route('/')
def ping_server():
    return "hello world"

@app.route('/animals')
def fetch_animals():
    db = get_db()
    _animals = db.animal_tb.find()
    animals = [{"id":animal["id"], "name":animal["name"], "type":animal["type"] } for animal in _animals]
    # return jsonify(list(_animals))
    return jsonify({"animals": animals})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)