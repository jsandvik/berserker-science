from flask import Flask
from sc_guide.models import Move

def create_app():
    app = Flask(__name__)
    return app