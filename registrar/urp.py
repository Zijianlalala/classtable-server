import json
import re
import base64
import requests
from bs4 import BeautifulSoup
from . import registrar
from abc import abstractclassmethod


class URP(registrar.Registrar):

    def __init__(self):
        self.session = requests.session()
        self.captcha_url = ''
        self.login_url = ''
        self.classtable_url = ''
        self.html_head = ''
        self.headers = ''

    @abstractclassmethod
    def base_url(self):
        return ''

    def generate(self):
        self.captcha_url = self.base_url()+'validateCodeAction.do'
        self.login_url = self.base_url()+'loginAction.do'
        self.classtable_url = self.base_url()+'xkAction.do?actionType=6'

        self.html_head = '<!DOCTYPE html><html><head><meta charset="utf-8"></head>'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }

    def get_state(self):
        return self.session.cookies.get_dict().get('JSESSIONID')

    def set_state(self, state):
        self.session.cookies.set('JSESSIONID', state)

    def get_captcha_base64(self):
        self.generate()
        captcha_pic = self.session.get(self.captcha_url).content
        return str(base64.b64encode(captcha_pic), encoding='utf-8')

    def start_time(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_classtable(self, username, password, captcha):
        self.generate()
        user_info = {"zjh": username, "mm": password, "v_yzm": captcha}

        response = self.session.post(
            self.login_url, headers=self.headers, data=user_info)

        if str(response.text).find(u'<title>学分制综合教务</title>') < 0:
            return 'Error'

        text = self.html_head + self.session.get(self.classtable_url).text

        self.session.close()

        soup = BeautifulSoup(text, 'lxml')

        objs = []
        start = {"year": self.year, "month": self.month, "day": self.day}
        map = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
               "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}

        for items in BeautifulSoup(str(soup.find_all('table')[7]), 'lxml').find_all('tr', {'class': 'odd'}):
            item = items.find_all('td')
            if len(item) < 10:
                week_num_str = item[0].get_text().strip().replace(
                    '周', '').replace('上', '').split('-')
                week_num = list(range(int(week_num_str[0]), int(
                    week_num_str[len(week_num_str)-1])+1))
                day_of_week = int(item[1].get_text().strip())
                class_of_day = map[item[2].get_text().strip()]
                duration = int(item[3].get_text().strip())
                place = item[5].get_text().strip()+item[6].get_text().strip()
            else:
                name = item[2].get_text().strip()
                week_num_str = item[11].get_text().strip().replace(
                    '周', '').replace('上', '').split('-')
                week_num = list(range(int(week_num_str[0]), int(
                    week_num_str[len(week_num_str)-1])+1))
                day_of_week = int(item[12].get_text().strip())
                class_of_day = map[item[13].get_text().strip()]
                duration = int(item[14].get_text().strip())
                place = item[16].get_text().strip()+item[17].get_text().strip()

            obj = {"name": name, "place": place, "day_of_week": day_of_week,
                   "class_of_day": class_of_day, "duration": duration, "week_num": week_num}

            objs.append(obj)

        ret = {"classtable": objs, "start": start}
        return json.dumps(ret, ensure_ascii=False)

    def test(self):
        print("URP")
