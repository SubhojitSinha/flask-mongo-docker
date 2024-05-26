from flask import Flask, jsonify
from routes.routes import bp_routes
# from flask_migrate import Migrate
# from models.yt_scrap import db


def create_app():
    app = Flask(__name__)
    # app.config.from_object('config')
    # db.init_app(app)  # Initializing the database
    return app

app = create_app()  # Creating the app

# Registering the blueprint
app.register_blueprint(bp_routes)

# Initializing the migration
# migrate = Migrate(app, db)













if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)