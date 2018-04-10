from . import urp


class SDAU(urp.URP):
    def base_url(self):
        return 'http://jw.sdau.edu.cn/'

    def test(self):
        print('SDAU')
