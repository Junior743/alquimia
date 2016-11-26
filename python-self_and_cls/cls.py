class ObjetoCls(object):

    lista = []

    def __init__(self):
        self.lista = []

    @classmethod
    def adicionar(cls, dados):
        cls.lista.append(dados)
        print('adicionado\n')

    @classmethod
    def pegar(cls, indice):
        print(cls.lista[indice])

    @classmethod
    def listar(cls):
        for item in cls.lista:
            print(item)