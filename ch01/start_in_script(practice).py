from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#----------practice start------------
if __name__ == '__main__':
    app.run(debug=True)    
    # app.run()    
#----------practice end--------------
