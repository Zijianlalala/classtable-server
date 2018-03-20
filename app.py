
import io

from flask import Flask, render_template, request, send_file, session

from urp import URP

app = Flask(__name__)
app.secret_key = 'developer is very cool'
u = URP()


@app.route('/')
def index():
    return render_template('index.html', index='Ya')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        ret = u.get_captcha_base64()
        return render_template('login.html', captcha_base64=ret)

        '''
        return send_file(
            io.BytesIO(ret),
            mimetype='image/jpg'
        )
        '''
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        captcha_text = request.form.get('captcha_text')
        u.start_time(2018, 3, 5)
        ret = u.get_classtable(username, password, captcha_text)
        return ret


if __name__ == '__main__':
    app.run()
