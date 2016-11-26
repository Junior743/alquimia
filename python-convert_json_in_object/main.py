import json

class Principal(object):

    def __init__(self):
        
        estrutura = input("Entre com a estrutura JSON: ")
        estrutura = estrutura.replace(" ", "")
        estrutura = json.loads(estrutura)
        
        Conversor.deJson(Conversor, estrutura)

        print(Conversor.__dict__)


class Conversor(object):

    def deJson(self, json):
        '''
        Transforma quaisquer atributos de uma estrutura JSON em objetos de determinada classe
        '''
        try:

            for chave, valor in json.items():
                setattr(self, chave, valor)
                
            return self

        except:
            raise


if __name__ == "__main__":
    Principal()