# ----------practice start------------
from flask import Flask
from markupsafe import escape
# ----------practice end--------------

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# ----------practice start------------
@app.route('/escape')
def with_escape():
    return escape('<h1>Hello World!</h1>')

# ----------practice end--------------

if __name__ == '__main__':
    app.run(debug=True)