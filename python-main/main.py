#
# tentando entender a diferenca entre if __name__ == '__main__' e __init__()
#

class Principal(object):

    def __init__(self):

        print('__init__')


if __name__ == '__main__':

    print('__name__ == \'__main__\'')


Principal()