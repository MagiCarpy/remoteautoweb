from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_restful import Api
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_key')
app.config["SQLALCHEMY_DATABASE_URI"]= os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///default.db')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

api = Api(app)

from DCW.resources.devicesAPI import DevicesAPI
api.add_resource(DevicesAPI, '/api/devices/')

from DCW import routes