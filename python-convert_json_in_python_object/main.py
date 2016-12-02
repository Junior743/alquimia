import json

class Principal(object):

    def __init__(self):

        estrutura = input("Entre com a estrutura JSON: ")
        
        dict_estrutura = self.de_json(estrutura)

        print(dict_estrutura)
        print('\n')
        print(type(dict_estrutura))

    def de_json(self, estrutura):
        try:

            if estrutura:
                return json.loads(estrutura)
            else:
                return False

        except:
            raise


if __name__ == "__main__":

    Principal()