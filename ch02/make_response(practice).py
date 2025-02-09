#----------practice start------------
from flask import Flask, make_response
#----------practice end--------------

app = Flask(__name__)

#----------practice start------------
@app.route('/')
def index():
    response = make_response('<h1>Check the status code</h1>')
    response.status_code = 404
    print("response.content_length :",response.content_length, "response.content_type :",response.content_type, 
          "len(\"<h1>Check the status code</h1>\"):",len("<h1>Check the status code</h1>"))
    # print 的內容會顯示在小黑窗
    # 要創建 response 物件才能取得這些資訊
    return response

#----------practice end--------------

if __name__ == '__main__':
    app.run(debug=True)
