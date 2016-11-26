import os

class Principal(object):
    
    def __init__(self, nome_ambiente, versao = None, caminho = './', nome_egg = 'strike'):
        print('Acessando diretorio.')
        os.system('cd ' + caminho)
        print('Acessando ambiente python (' + nome_ambiente + ')')
        os.system('source activate ' + nome_ambiente)
        print('Instalando projeto no ambiente python.')

        if versao:
            os.system("pip install --editable=git+http://github.com/Junior743/poc-pip_install@" + versao + "#" + nome_egg)
        else:
            os.system("pip install --editable=git+http://github.com/Junior743/poc-pip_install#egg=" + nome_egg)

        print('Projeto instalado com sucesso')

Principal()