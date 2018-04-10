from abc import abstractclassmethod


class Registrar:
    @abstractclassmethod
    def get_state(self):
        pass

    @abstractclassmethod
    def set_state(self, state):
        pass

    @abstractclassmethod
    def get_captcha_base64(self):
        pass

    @abstractclassmethod
    def start_time(self, year, month, day):
        pass

    @abstractclassmethod
    def get_classtable(self, username, password, captcha):
        pass

    def test(self):
        print('Registrar')
