import os
import sys
from platform import python_version

class Principal(object):
    
    def __init__(self):
        try:
            # Nome do projeto
            nome_projeto = 'poc-pip_install'
            versao_python = str(python_version()).split('.')
            versao_python = versao_python[0] + '.' + versao_python[1]
            
            if versao_python != '3.4':
                print('\nA versão do python não condiz com a versão utilizada no strike.\nPor favor, atualize a versão do python em seu ambiente para a versão: \'3.4\'')
                exit()
            
            # Pegando nome do ambiente python
            nome_ambiente = input('Nome do ambiente python*: ')
            if nome_ambiente == '':
                print('Nome do ambiente é obrigatório')
                exit()

            # Entrando na pasta do ambiente python
            # caminho_ambiente = str(sys.prefix) + '/envs/' + nome_ambiente + '/lib/python' + versao_python + '/site-packages/'
            caminho_ambiente = str(sys.prefix) + '/lib/python' + versao_python + '/site-packages/'

            # Pegando versao (tag) do commit no github
            versao_release = input('Versão do release: ')
            if versao_release == '':
                comando_pip = 'pip install --editable=git+http://github.com/Junior743/' + str(nome_projeto) + '#egg=' + str(nome_projeto)
                
            else:
                comando_pip = 'pip install --editable=git+http://github.com/Junior743/' + str(nome_projeto) + '@' + str(versao_release) + '#egg=' + str(nome_projeto)
            
            # Deseja instalar o projeto no ambiente python?
            if input('\n\nInstalar pacote (y/N)?: ') == 'y':
                
                # Instalando projeto no ambiente python
                print('\nInstalando projeto no ambiente python.')
                if os.system('cd ' + caminho_ambiente + ' && source activate ' + nome_ambiente + ' && ' + comando_pip):
                    exit()

                print('\n\nProjeto instalado com sucesso')
            else:
                print('\n\nBye')
        
        except:
            raise

Principal()