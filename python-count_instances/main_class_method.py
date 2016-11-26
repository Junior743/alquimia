class Principal(object):
    numero_instancias = 0

    def __init__(self):
        Principal.numero_instancias = Principal.numero_instancias + 1

    @classmethod
    def imprimir(cls_objeto):
        return cls_objeto.numero_instancias

principal1 = Principal()
principal2 = Principal()

print(principal1.imprimir())
print(principal2.imprimir())
