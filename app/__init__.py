from flask import Flask
from decouple import config
#Mongodb connection imports
import os
from flask import send_from_directory, render_template
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#Mongodb connection
URI = config('uri')
#Create a new client and connect to the server
client = MongoClient(URI, server_api=ServerApi('1'))
#Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#Function returns app
def create_app():
    #Get app name
    app = Flask(__name__)
    #Import main blueprint and register it
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    return app
