#----------practice start------------
from flask import Flask
app123 = Flask(__name__)

@app123.route('/')
def index():
    return '<h1>hello world!</h1>'
#----------practice end--------------
