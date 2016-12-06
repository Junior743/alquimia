import json

class Principal(object):

    estrutura_padrao = {"produtos":[], "endereco":{"rua":"", "numero":""}}
    
    def __init__(self):
        
        # Entrada de dados
        estrutura = input("Entre com a estrutura JSON: ")

        # Tranformando o JSON
        ponto_movimentacao = PontoMovimentacao()
        saida = ponto_movimentacao.de_json(self.estrutura_padrao, estrutura)

        # Output
        if(saida):
            print(saida.endereco["rua"])
            print('\n')
            print(saida.produtos)
            print('\n')
            print(type(saida))
        else:
            print("ops, deu mal")

    @classmethod
    def de_json(cls, estrutura_padrao, estrutura):
        try:

            if estrutura_padrao and estrutura:
                estrutura = json.loads(estrutura)
                if cls.verifica_estrutura(estrutura_padrao, estrutura):
                    for chave, valor in estrutura.items():
                        setattr(cls, chave, valor)
                    return cls
                else:
                    return False
            else:
                return False

        except:
            raise
            

    @classmethod
    def verifica_estrutura(cls, estrutura_padrao, estrutura):
        try:

            if estrutura_padrao and estrutura:
                # (False for chave in estrutura_padrao if chave not in estrutura)
                for chave in estrutura_padrao:
                    if chave not in estrutura:
                        return False
                    else:
                        if isinstance(estrutura[chave], dict):
                            if cls.verifica_estrutura(estrutura_padrao[chave], estrutura[chave]):
                                return True
                            else:
                                return False
                        else:
                            pass
                        pass

                return True
            else:
                return False

        except:
            raise


class PontoMovimentacao(Principal):

    def __init__(self):
        self.produtos = []
        self.endereco = {"rua":"", "numero":""}


if __name__ == "__main__":

    Principal()
