from cls import ObjetoCls
from self import ObjetoSelf

class Principal(ObjetoCls, ObjetoSelf):

    #lista = []

    def __init__(self):
        print('obtendo informacoes do ObjetoCls...')
        ObjetoCls.adicionar('1')
        ObjetoCls.adicionar('2')
        ObjetoCls.adicionar('3')
        ObjetoCls.listar()
        
        print('\n\nobtendo informacoes do ObjetoSelf...')
        ObjetoSelf.adicionar(self, 'um')
        ObjetoSelf.adicionar(self, 'dois')
        ObjetoSelf.adicionar(self, 'tres')
        ObjetoSelf.listar(self)

if __name__ == "__main__":
    Principal()