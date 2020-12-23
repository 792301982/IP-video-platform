"""
The flask application package.
"""

from flask import Flask

#from flask_socketio import SocketIO
app = Flask(__name__)
#app.config['SECRET_KEY'] = '159'
#socketio = SocketIO(app)

import FlaskWebProject2.views
