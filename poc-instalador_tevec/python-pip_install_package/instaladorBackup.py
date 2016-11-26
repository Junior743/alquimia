import os
import sys
import site
import shutil
from platform import python_version

class Instalador(object):
    # Variaveis
    versao_release = None
    versao_python = None
    nome_cliente = None
    lista_mensagens = []
    nome_programa = sys.argv[0]
    versao_python_strike = '3.4'

    def __init__(self):
        try:
            ####### TODO: 
            # * Testar dependencias de todos os projetos
            # * Pensar na condição de caso o usuário desejar atualizar um pacote
            # * Pensar na condição de caso o usuário desejar excluir o projeto com suas dependencias

            # Variaveis
            lista_parametros = []
            concluido = False
            
            # Pegando paramentros
            lista_parametros = sys.argv
            
            # Carregando mensagens utilizadas no programa em uma lista de mensagens
            Instalador.carregarListaMensagens(self)

            # Atualizar versao do python
            for indice, valor_parametro in enumerate(lista_parametros):
                if valor_parametro == '--atualizar-python':
                    concluido = Instalador.atualizarVersaoPython(self, lista_parametros[indice + 1])
                    exit()

            # Validacoes
            Instalador.validacoes(self, lista_parametros)

            # Exibir ajuda
            for indice, valor_parametro in enumerate(lista_parametros):
                if valor_parametro == '-h':
                    print(Instalador.exibirAjuda(self))
                    exit()
            
            # Exibir lista de ambientes
            for indice, valor_parametro in enumerate(lista_parametros):
                if valor_parametro == '-l':
                    concluido = Instalador.listarAmbientes(self)
                    exit()
                
            # Setando a versão do release
            for indice, valor_parametro in enumerate(lista_parametros):
                if valor_parametro == '-v':
                    # Verifica se o indice existe na lista
                    if len(lista_parametros) > 2 and len(lista_parametros) < 6:
                        self.versao_release = (lista_parametros[indice + 1])
            
            # Instalando o projeto do cliente e suas dependencias no ambiente python
            for indice, valor_parametro in enumerate(lista_parametros):
                if valor_parametro == '-i' or valor_parametro == 'instalar':
                    if len(lista_parametros) > 2 and len(lista_parametros) < 6:
                        self.nome_cliente = lista_parametros[indice + 1]

                        # Instalando o projeto cliente e suas dependencias
                        concluido = Instalador.instalarPacote(self)
                    else:
                        print(self.lista_mensagens[8] + self.lista_mensagens[9])
                        exit()

            # Desinstalando o projeto do cliente e suas dependencias do ambiente python
            for indice, valor_parametro in enumerate(lista_parametros):
                if valor_parametro == '-r' or valor_parametro == 'remover':
                    if len(lista_parametros) > 2 and len(lista_parametros) < 6:
                        self.nome_cliente = lista_parametros[indice + 1]

                        # Desinstalando o projeto cliente e suas dependencias
                        concluido = Instalador.desinstalarPacote(self)
                    else:
                        print(self.lista_mensagens[8] + self.lista_mensagens[9])
                        exit()
            
            if concluido:
                print(self.lista_mensagens[0])
            else:
                print(self.lista_mensagens[1] + self.lista_mensagens[9])
        except:
            raise
        
    def instalarPacote(self):
        if input(self.lista_mensagens[2]) == 'y':

            # Pegando o caminho do ambiente python
            print(self.lista_mensagens[5])
            caminho_ambiente = site.getsitepackages()[0]
            # caminho_ambiente = str(sys.prefix) + '/lib/python' + self.versao_python + '/site-packages/'

            # Validando se o usuário preencheu a versão de release do projeto
            if self.versao_release == None:
                self.versao_release = '@' + str(self.versao_release)
            else:
                self.versao_release = ''
            
            # Verificando se o usuário deseja instalar as dependencias do projeto
            opcao = input(self.lista_mensagens[15] + self.lista_mensagens[14])
            if opcao == 'y':
                comando_pip = 'pip install -e git+https://github.com/TEVEC/' + str(self.nome_cliente) + self.versao_release + '#egg=' + str(self.nome_cliente) + '&subdirectory=aplicacao'
            elif opcao == 'N':
                comando_pip = 'pip install --no-deps -e git+https://github.com/TEVEC/' + str(self.nome_cliente) + self.versao_release + '#egg=' + str(self.nome_cliente) + '&subdirectory=aplicacao'
            else:
                print(self.lista_mensagens[10])
                exit()
            
            # Executando os comandos
            print(self.lista_mensagens[11])
            # os.chdir(caminho_ambiente)
            if os.system('cd ' + caminho_ambiente + ' && ' + comando_pip):
                    exit()
            
            return True
        else:
            print(self.lista_mensagens[6])
            exit()

    def desinstalarPacote(self):
        if input(self.lista_mensagens[3]) == 'y':
            # Pegando o caminho do ambiente python
            print(self.lista_mensagens[5])
            caminho_ambiente = str(sys.prefix) + '/lib/python' + self.versao_python + '/site-packages/'
            
            try:
                # Pegando o caminho do ambiente python
                print(self.lista_mensagens[12])
                # Apagando o diretorio do pacote
                shutil.rmtree(caminho_ambiente + 'src/' + str(self.nome_cliente))
                # os.remove(caminho_ambiente + str(self.nome_cliente) + '.egg-link')
            except:
                print(self.lista_mensagens[13])
                exit()
        
        return True

    def listarAmbientes(self):
        # Listando ambientes python
        if os.system('conda env list'):
            exit()

    def atualizarVersaoPython(self, versao):
        # Atualizando versão do python
        if os.system('conda install python=' + str(versao)):
            exit()
        
    def validacoes(self, lista_parametros):
        
        #   Atente-se quanto a ordem das validacoes. 
        #   É recomendado que a validacao do ambiente python seja a primeira validacao, 
        #  e logo após venha a validacao da versao do python.
        
        # Variaveis
        self.versao_python = str(python_version()).split('.')
        self.versao_python = self.versao_python[0] + '.' + self.versao_python[1]
        
        # Validando se o ambiente está ativo
        if not 'CONDA_PREFIX' in os.environ:
            print(self.lista_mensagens[16])
            exit()

        # Validando versão do python
        if self.versao_python != self.versao_python_strike:
            print(self.lista_mensagens[4])
            exit()
        
        # Validando se falta argumentos
        if len(lista_parametros) < 2:
            print(self.lista_mensagens[7] + self.lista_mensagens[9])
            exit()
        
        # Validando se há excesso de argumentos
        if len(lista_parametros) > 5:
            print(self.lista_mensagens[10] + self.lista_mensagens[9])
            exit()

        return True
    
    def exibirAjuda(self):
        texto_ajuda = '\n'\
                'Programa utilizado para instalação de projetos do github no ambiente python.\n\n'\
                'Como usar:\n'\
                '   python ' + self.nome_programa + ' <comando>\n'\
                '   python ' + self.nome_programa + ' <comando> [valor]\n'\
                '   python ' + self.nome_programa + ' <comando> [valor] <comando> [valor]\n\n'\
                'Comandos:\n'\
                '   -i, instalar          Instala o pacote.\n'\
                '   -r, remover           Remove o pacote.\n'\
                '   -l                    Lista os ambientes python.\n'\
                '   -h                    Ajuda.\n'\
                '   -v                    Indicar a versão do release desejado.\n'\
                '   --atualizar-python    Atualizar a versão do python.\n'\
                '\n'\
                'Exemplos de uso:\n'\
                '   Instalação de pacote:\n'\
                '      python ' + self.nome_programa + ' instalar cliente-wickbold\n\n'\
                '   Instalação de pacote indicando a versão do release desejado:\n'\
                '      python ' + self.nome_programa + ' instalar cliente-wickbold -v 1.0\n\n'\
                '   Desinstalação de pacote:\n'\
                '      python ' + self.nome_programa + ' desinstalar cliente-wickbold\n\n'\
                '   Listar ambientes python:\n'\
                '      python ' + self.nome_programa + ' -l\n\n'\
                '   Atualizar versão do python:\n'\
                '      python ' + self.nome_programa + ' --atualizar-python 3.4'\
                '\n'

        return texto_ajuda

    def carregarListaMensagens(self):
        self.lista_mensagens = ['\nConcluído.', 
                                '\nOcorreu um erro.', 
                                '\nInstalar projeto no ambiente? (y/N): ', 
                                '\nDesinstalar projeto do ambiente? (y/N): ',
                                '\nA versão do python não condiz com a versão utilizada pelo strike (' + self.versao_python_strike + '). '\
                                'Atualize a versão do python em seu ambiente utilizando o comando \'python ' + self.nome_programa + ' --atualizar-python ' + self.versao_python_strike + '\'.',
                                '\nAcessando ambiente python.', 
                                '\nBye tevequiano', 
                                '\nExistem parametros obrigatórios para a execução do programa.', 
                                '\nO nome do projeto do cliente é obrigatório.', 
                                ' Use o comando \'python ' + self.nome_programa + ' -h\' para obter informações de utilização.', 
                                '\nParâmetro incorreto.', 
                                '\nInstalando projeto.', 
                                '\nDesinstalando projeto.', 
                                '\nProjeto não encontrado no ambiente python.', 
                                '\nDeseja instalar as dependências do projeto? (y/N): ', 
                                '\n\033[33mSe você aceitar esta ação, seram instalados novos pacotes e os já existentes seram atualizados!\033[0;0m', 
                                '\nAmbiente python inativo. Utilize o comando \'source activate nome_do_ambiente\' para ativar o ambiente python.'
                                ]

Instalador()