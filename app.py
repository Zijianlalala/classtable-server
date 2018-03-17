import io

from flask import Flask, request, send_file, session

from classtable import ClassTable

app = Flask(__name__)
app.secret_key = 'developer is very cool'
CLASS_TABLE = ClassTable()


@app.route('/')
def index():
    return 'Index\n'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return send_file(
            io.BytesIO(CLASS_TABLE.get_captcha()),
            mimetype='image/jpg'
        )
    else:
        username = request.form.get('zjh')
        password = request.form.get('mm')
        captcha = request.form.get('v_yzm')
        return CLASS_TABLE.get_json(username, password, captcha)
