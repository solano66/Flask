#----------practice start------------
from flask import Flask, abort
#----------practice end--------------

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hi</h1>"

# ----------practice start------------
@app.route('/user/<int:id>')
def get_user(id):
    if id > 100:
        abort(404)
        # 為啥不用 raise (手動丟exception)，因為整個 .py 都會停掉。
    return f'<h1>hello {id}</h1>'

# ----------practice end--------------


if __name__ == '__main__':
    app.run(debug=True)
