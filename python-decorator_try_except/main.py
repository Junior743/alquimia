from decorator import Decorator 

class ClassePrincipal(object):
    
    # tentar()
    # @Decorator.tentar("Erro", False)
    # def __init__():
    #     valor = 12 / 0
    #     print(valor)


    # tentarCondicional() ##### PRECISA TESTAR MELHOR DESTA MANEIRA
    # @Decorator.tentarCondicional("Erro", False, ['ZeroDivisionError', 'TypeError'])
    # @Decorator.tentarCondicional("Erro de divisao por zero", False, ['ZeroDivisionError'])
    # @Decorator.tentarCondicional("Erro", False, ['TypeError'])
    # def __init__():
    #     valor = 12 / 0
    #     print(valor)


    # tentarCondicionalReverso() ##### PRECISA TESTAR MELHOR
    # @Decorator.tentarCondicionalReverso("Erro", False, ['ZeroDivisionError', 'TypeError'])
    # def __init__(self):
    #     valor = 12 / 0
    #     print(valor)


    # tentarDetalhado()
    # @Decorator.tentarDetalhado("Erro", False, ['ZeroDivisionError', 'TypeError'], 'Projeto', 'Arquivo', 'Classe', 'Metodo')
    # def __init__():
    #     valor = 12 / 0
    #     print(valor)

    # tentarDetalhadoDinamico()
    @Decorator.tentarDetalhadoDinamico("Erro", False, ['ZeroDivisionError', 'TypeError'])
    def __init__():
        valor = 12 / 0
        print(valor)

ClassePrincipal()
