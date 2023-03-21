# This is how flask knows what to do with itself

from flask import Flask

app = Flask(__name__)

from . import routes

# flask run will start the server