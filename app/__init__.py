from flask import Flask

app = Flask(__name__)

# GLOBAL VARIABLES
TEMP = "./temp/"
MAXREQ = 40
req = 0

# configure the app
app.config['TEMP'] = TEMP
app.config['MAXREQ'] = MAXREQ
app.config['req'] = req

from app import views