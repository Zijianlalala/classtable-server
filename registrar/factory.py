from registrar import *


class Factory:
    @staticmethod
    def get_object(name):
        # 根据反射生成对象
        return eval('{}.{}()'.format(str(name).lower(), str(name).upper()))
