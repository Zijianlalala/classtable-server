import io

from flask import Flask, request, send_file, session, render_template

from urp import URP

app = Flask(__name__)
app.secret_key = 'developer is very cool'
u = URP()


@app.route('/')
def index():
    return render_template('index.html', index='haha')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        ret = u.get_captcha()
        if ret == 'TimeOut':
            return 'Time Out!\n'
        return send_file(
            io.BytesIO(ret),
            mimetype='image/jpg'
        )
    else:
        username = request.form.get('zjh')
        password = request.form.get('mm')
        captcha = request.form.get('v_yzm')
        u.start_time(2018, 3, 5)
        ret = u.get_classtable(username, password, captcha)
        if ret == 'TimeOut':
            return 'Time Out!\n'
        return ret


if __name__ == '__main__':
    app.run()
