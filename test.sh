#/bin/sh

echo "首页GET请求"
curl "http://127.0.0.1:5000/"

echo "登录页面GET请求"
curl -c cookie.txt -o 'captcha.jpg' "http://127.0.0.1:5000/login"

echo "登录页POST请求"
curl -b cookie.txt -d "zjh=20151234&mm=123456&v_yzm=0000" "http://127.0.0.1:5000/login"
