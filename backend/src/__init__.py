from flask import Flask  
from src.utilities.config import connect_db
from src.users.route import api_bp

def create_app():
    app = Flask(__name__)
    connect_db(app)
    app.register_blueprint(api_bp)
    return app

