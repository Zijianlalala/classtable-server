# 微信课程表server端

## /

测试,返回固定字符串

## /login?school=school_name [GET]

school_name为学校缩写,返回base64形式验证码图片

## /login [POST]
参数 | 解释 | 样例
:-: | :-: | :-: 
school|学校缩写|tsmc
username|账号|123
password|密码|456
captcha_text|验证码|789

## 更新
服务端版本随客户端同时放弃更新.
