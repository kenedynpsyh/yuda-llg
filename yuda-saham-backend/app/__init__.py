from flask import Flask
from flask_cors import CORS
from app.cfg.configuration import configuration

def create_app():
    app = Flask(__name__)
    CORS(app,origins=["http://localhost:3000"])
    configuration(app)
    return app