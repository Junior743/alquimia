def imprimir(cls_objeto):
    return cls_objeto.numero_instancias

class Principal(object):
    numero_instancias = 0

    def __init__(self):
        Principal.numero_instancias = Principal.numero_instancias + 1

principal1 = Principal()
principal2 = Principal()

print(imprimir(principal1))
