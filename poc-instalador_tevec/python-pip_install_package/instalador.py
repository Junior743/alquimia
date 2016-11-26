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
    lista_mensagens_erros = []
    lista_mensagens_avisos = []
    lista_mensagens_informacoes = []
    lista_mensagens_confirmacoes = []
    nome_programa = sys.argv[0]
    versao_python_strike = '3.4'

    def __init__(self):
        try:
            ####### TODO: 
            # * Testar dependencias de todos os projetos
            # * Pensar na condição de caso o usuário desejar atualizar um pacote
            # * Pensar na condição de caso o usuário desejar excluir o projeto com suas dependencias
	    # * Atualizar python nao esta funcionando, pois na hora de atualizar o python o programa critica a versao incorreta do mesmo novamente.
            # * Dividir as mensagens em categorias, ex: lista_mensagens_erros, lista_mensagens_alerta, lista_mensagem_confirmacao...
            #
            # DOCUMENTACAO:
            # * Verifica se o usuário deseja instalar dependencias

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
                
                break

            # Validacoes
            Instalador.validacoes(self, lista_parametros)

            for indice, valor_parametro in enumerate(lista_parametros):
                # Exibir ajuda
                if valor_parametro == '-h':
                    print(Instalador.exibirAjuda(self))
                    concluido = True
                    break
                    
                # Exibir lista de ambientes
                if valor_parametro == '-l':
                    concluido = Instalador.listarAmbientes(self)
                    break
            
                # Instalando o projeto do cliente e suas dependencias no ambiente python
                if valor_parametro == '-i' or valor_parametro == 'instalar':
                    if len(lista_parametros) > 2 and len(lista_parametros) < 6:
                        self.nome_cliente = lista_parametros[indice + 1]

                        # Pegando a versão do release
                        for indice, valor_parametro in enumerate(lista_parametros):
                            if valor_parametro == '-v':
                                self.versao_release = '@' + (lista_parametros[indice + 1])
                        if self.versao_release == None:
                            self.versao_release = ''

                        # Instalando o projeto cliente e suas dependencias
                        concluido = Instalador.instalarPacote(self)
                    else:
                        print(self.lista_mensagens_erros[1] + self.lista_mensagens_avisos[2])
                        concluido = False
                    
                    break
                
                # Desinstalando o projeto do cliente
                if valor_parametro == '-r' or valor_parametro == 'remover':
                    if len(lista_parametros) > 2 and len(lista_parametros) < 6:
                        self.nome_cliente = lista_parametros[indice + 1]

                        # Desinstalando o projeto cliente e suas dependencias
                        concluido = Instalador.desinstalarPacote(self)
                    else:
                        print(self.lista_mensagens_erros[1] + self.lista_mensagens_avisos[2])
                        concluido = False
                    
                    break
            
            if not concluido:
                print(self.lista_mensagens_erros[0] + self.lista_mensagens_avisos[2])

            exit()
        except:
            raise
        
    def instalarPacote(self):
        if input(self.lista_mensagens_confirmacoes[0]) == 'y':

            # Pegando o caminho do ambiente python
            caminho_ambiente = str(site.getsitepackages()[0])
            
            # Verificando se o usuário deseja instalar as dependencias do projeto
            opcao = input(self.lista_mensagens_avisos[3] + self.lista_mensagens_confirmacoes[2])
            if opcao == 'y':
                comando_pip = 'pip install --upgrade -e git+https://github.com/TEVEC/' + str(self.nome_cliente) + '.git' + str(self.versao_release) + '#egg=' + str(self.nome_cliente) + '&subdirectory=aplicacao'
            elif opcao == 'N':
                # --no-deps
                comando_pip = 'pip install -e git+https://github.com/TEVEC/' + str(self.nome_cliente) + '.git' + str(self.versao_release) + '#egg=' + str(self.nome_cliente) + '&subdirectory=aplicacao'
            else:
                return False

            print(self.lista_mensagens_informacoes[3])
            if os.system('cd ' + caminho_ambiente + ' && ' + comando_pip):
                return False
            
        else:
            print(self.lista_mensagens_informacoes[2])
        
        return True

    def desinstalarPacote(self):
        if input(self.lista_mensagens_confirmacoes[1]) == 'y':
            
            # Pegando o caminho do ambiente python
            caminho_ambiente = str(site.getsitepackages()[0])
            
            try:
                # Pegando o caminho do ambiente python
                print(self.lista_mensagens_informacoes[4])
                # Apagando o diretorio do pacote
                shutil.rmtree(caminho_ambiente + 'src/' + str(self.nome_cliente))
            except:
                print(self.lista_mensagens_erros[3])
                return False

        else:
            print(self.lista_mensagens_informacoes[2])
        
        return True

    def listarAmbientes(self):
        # Listando ambientes python
        if os.system('conda env list'):
            return False
            
        return True

    def atualizarVersaoPython(self, versao):
        # Atualizando versão do python
        if os.system('conda install python=' + str(versao)):
            return False

        return True
        
    def validacoes(self, lista_parametros):
        
        #  Atente-se quanto a ordem das validacoes. 
        #  É recomendado que a validacao do ambiente python seja a primeira validacao, 
        # e logo após venha a validacao da versao do python.
        
        # Variaveis
        self.versao_python = str(python_version()).split('.')
        self.versao_python = self.versao_python[0] + '.' + self.versao_python[1]
        
        # Validando se o ambiente está ativo
        if not 'CONDA_PREFIX' in os.environ:
            print(self.lista_mensagens_erros[4])
            exit()

        # Validando versão do python
        if self.versao_python != self.versao_python_strike:
            print(self.lista_mensagens_avisos[0])
            exit()
        
        # Validando se falta argumentos
        if len(lista_parametros) < 2:
            print(self.lista_mensagens_avisos[1] + self.lista_mensagens_avisos[2])
            exit()
        
        # Validando se há excesso de argumentos
        if len(lista_parametros) > 5:
            print(self.lista_mensagens_erros[2] + self.lista_mensagens_avisos[2])
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
                                
        self.lista_mensagens_erros = [
                                        '\nOcorreu um erro.',
                                        '\nO nome do projeto do cliente é obrigatório.',
                                        '\nParâmetro incorreto.',
                                        '\nProjeto não encontrado no ambiente python.',
                                        '\nAmbiente python inativo. Utilize o comando \'source activate nome_do_ambiente\' para ativar o ambiente python.'
                                     ]
        self.lista_mensagens_avisos = [
                                        '\nA versão do python não condiz com a versão utilizada pelo strike (' + self.versao_python_strike + '). '\
                                        'Atualize a versão do python em seu ambiente utilizando o comando \'python ' + self.nome_programa + ' --atualizar-python ' + self.versao_python_strike + '\'.',

                                        '\nExistem parametros obrigatórios para a execução do programa.',
                                        ' Use o comando \'python ' + self.nome_programa + ' -h\' para obter informações de utilização.',
                                        '\n\033[33mSe você aceitar esta ação os pacotes já existentes em seu ambiente seram atualizados!\033[0;0m'
                                      ]
        self.lista_mensagens_informacoes = [
                                            '\nConcluído.',
                                            '\nAcessando ambiente python.',
                                            '\nBye tevequiano',
                                            '\nInstalando projeto.',
                                            '\nDesinstalando projeto.'
                                           ]
        self.lista_mensagens_confirmacoes = [
                                            '\nInstalar projeto no ambiente? (y/N): ',
                                            '\nDesinstalar projeto do ambiente? (y/N): ',
                                            '\nDeseja atualizar as dependências do projeto? (y/N): '
                                            ]

Instalador()
