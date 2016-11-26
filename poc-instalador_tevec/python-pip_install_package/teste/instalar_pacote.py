import os
import platform

class Principal(object):
    
    def __init__(self):
        try:
            # Nome do projeto
            nome_projeto = 'tevec-corporativo'
            
            # Pegando nome do ambiente python
            nome_ambiente = input('Nome do ambiente python*: ')
            if nome_ambiente == '':
                print('Nome do ambiente é obrigatório')
                exit()

            # Pegando caminho do ambiente python
            caminho_ambiente = input('Caminho do diretorio de instalacao: ')
            if caminho_ambiente == '':
                if platform.system() == 'Windows':
                    caminho_ambiente = '.\\'
                else:
                    caminho_ambiente = './'
            
            # Pegando versao (tag) do commit no github
            versao = input('Versão do release: ')
            if versao == '':
                comando_pip = 'pip install --editable=git+http://github.com/TEVEC/' + str(nome_projeto) + '#egg=' + str(nome_projeto)
                
            else:
                comando_pip = 'pip install --editable=git+http://github.com/TEVEC/' + str(nome_projeto) + '@' + str(versao) + '#egg=' + str(nome_projeto)
            
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
