import os
import platform

class Principal(object):

    def __init__(self):
        try:
            # Variaveis e validacoes
            nome_ambiente = input('Nome do ambiente python*: ')
            if nome_ambiente == '':
                print('Nome do ambiente é obrigatório')
                exit()
            
            versao = input('Versão do release: ')

            caminho = input('Caminho do diretorio de instalacao: ')
            if caminho == '':
                if platform.system() == 'Windows':
                    caminho = '.\\'
                else:
                    caminho = './'

            nome_egg = input('Nome do egg: ')
            if nome_egg == '':
                nome_egg = 'poc-pip_install'

            iniciar = input('\n\nInstalar pacote (y/N): ')

            # Validacoes e instalacao
            if iniciar == 'y':
                print('\nAcessando diretorio.')
                if os.system('cd ' + caminho):
                    exit()

                print('\nAcessando ambiente python (' + nome_ambiente + ')')
                if os.system('source activate ' + nome_ambiente):
                    exit()
                
                print('\nInstalando projeto no ambiente python.')

                if versao == '':
                    if os.system("pip install --editable=git+http://github.com/Junior743/poc-pip_install#egg=" + nome_egg):
                        exit()
                else:
                    if os.system("pip install --editable=git+http://github.com/Junior743/poc-pip_install@" + versao + "#egg=" + nome_egg):
                        exit()

                print('\n\nProjeto instalado com sucesso')

            else:
                print('\n\nBye')
        
        except:
            raise

Principal()
