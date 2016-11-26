class ObjetoSelf(object):
    
    lista = []

    def __init__(self):
        self.lista = []

    def adicionar(self, dados):
        self.lista.append(dados)
        print('adicionado\n')

    def pegar(self, indice):
        print(self.lista[indice])

    def listar(self):
        for item in self.lista:
            print(item)