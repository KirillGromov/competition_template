from flask import Flask
from app.config import Configurations
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)

app.config.from_object(Configurations)



from .views import *
