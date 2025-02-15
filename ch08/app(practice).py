from flask import Flask, render_template, request, url_for
from pathlib import Path
import uuid

# practice start
import recognition.load_model as model
# practice end

app = Flask(__name__)

# practice start
UPLOAD_FOLDER = Path(__file__).resolve().parent/'static/uploaded'
# practice end

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header")

# practice start
@app.route('/file', methods=['GET', 'POST'])
def get_file():
    if request.method == "GET":
        return render_template('file(practice).html', page_header="upload file")
    elif request.method == "POST":
        file = request.files['file101'] # key is the value of name(html attribute) in <input type="file">
        if file:
            filename = str(uuid.uuid4())+"_"+file.filename
            file.save(UPLOAD_FOLDER/filename)
        data = model.recog_digit(filename)
        img_src = url_for('static', filename=f'uploaded/{filename}')
        return render_template('recog_result(practice).html', page_header="review file", data=data, img_src=img_src)

# practice end


if __name__ == "__main__":
    app.run(debug=True)



