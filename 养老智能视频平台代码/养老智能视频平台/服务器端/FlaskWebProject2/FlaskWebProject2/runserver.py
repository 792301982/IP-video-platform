"""
This script runs the FlaskWebProject2 application using a development server.
"""

from os import environ
from FlaskWebProject2 import app

if __name__ == '__main__':
    app.run('0.0.0.0', 80)
    #socketio.run(app,'0.0.0.0',5555)
