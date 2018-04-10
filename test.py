from registrar import factory


def test():
    try:
        reg = factory.Factory().get_object('urp')
        reg.test()
    except NameError:
        print('学校名字未定义，请查看 __init__.py 是否已修改')
    except BaseException:
        print('未知异常')


if __name__ == '__main__':
    test()
