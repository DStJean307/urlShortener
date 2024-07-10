from flask import Blueprint
#Initialize main page blueprint
bp = Blueprint('main', __name__)

from app.main import routes
