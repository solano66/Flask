from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#----------practice start------------

@app.route('/<x>')
def greet(x):
    return f'<h1>Hello {x}!</h1>'

#----------practice end--------------

if __name__ == '__main__':
    app.run(debug=True)
