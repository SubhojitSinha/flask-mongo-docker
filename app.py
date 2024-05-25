from flask import Flask, jsonify
from routes import bp_routes

app = Flask(__name__)

# Registering the blueprint
app.register_blueprint(bp_routes)














if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)