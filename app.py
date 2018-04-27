import io

from flask import Flask, render_template, request, send_file, session

from registrar import factory

app = Flask(__name__)
app.secret_key = 'developer is very cool'


@app.route('/')
def index():
    return render_template('index.html', index='Ya')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # 存在验证码使用GET请求获取验证码
    if request.method == 'GET':
        school = request.values.get('school')
        if school==None:
            return 'No School'
        u = factory.Factory().get_object(school)
        ret = u.get_captcha_base64()
        session['state'] = u.get_state()
        return render_template('login.html', captcha_base64=ret,school=school)
        # 返回base64形式字符串
        #return ret

    # 不存在验证码直接发送POST请求
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        school = request.form.get('school')
        u = factory.Factory().get_object(school)
        u.set_state(session['state'])
        captcha_text = request.form.get('captcha_text')
        u.start_time(2018, 3, 5)
        ret = u.get_classtable(username, password, captcha_text)
        return ret


if __name__ == '__main__':
    app.run()
