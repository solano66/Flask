from flask import Flask


app = Flask(__name__)

#----------practice start------------
@app.route('/')
def index():
    return '<h1>bad request</h1>', 400, {'key1':100, 'key2':200}
    # F12，Status = 400 , key1,key2 在 response headers

#----------practice end--------------

if __name__ == '__main__':
    app.run(debug=True)
