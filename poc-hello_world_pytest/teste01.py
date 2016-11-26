class Principal():
    
    def main(self):
        try:
            
            self.calcular(self, 1)
            self.teste_calcular(self)

        except:
            raise


    def calcular(self, x):
        return x + 1


    def teste_calcular(self):
        assert self.calcular(self, 1) == 3


if __name__ == "__main__":
    Principal.main(Principal)