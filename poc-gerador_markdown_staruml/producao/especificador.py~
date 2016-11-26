#  
# Dsenvolvedor: Junior
# Data: 07/10/2016
# Objetivo: Automatizar a geracao de documentos no formato markdown para o portal de documentacao MKDocs.
#

import os
import json
import argparse
from sqlalchemy.util.langhelpers import classproperty

class ArquiteturaEstrategica(object):
    
    @classmethod
    def mapearArgumentos(cls, interpretador):
        try:
            
            # criando os comandos
            args_arquiteturaestrategica = interpretador.add_parser('arquiE', help='Grupo de comandos para ferramentas uteis em arquitetura estrategica')
            args_arquiteturaestrategica.add_argument('-c', '--caminho', nargs=1, type=str, help='Caminho ate o arquivo mdj')
            args_arquiteturaestrategica.add_argument('-t', '--tipo', nargs=1, type=str, help='Tipo do arquivo (MER ou DER)')
            args_arquiteturaestrategica.add_argument('-n', '--nome', nargs=1, type=str, help='Nome do programa')
            args_arquiteturaestrategica.set_defaults(func = cls.especificador)

        except:
            raise


    def especificador(self, args):
        
        # garantindo informações obrigatorias
        arg_caminho = (args.caminho or input("Caminho do arquivo: "))
        arg_tipo = (args.tipo or input("Tipo da documentacao (MER ou DER): "))
        arg_nome = (args.nome or input("Nome do arquivo: "))

        # convertendo argumentos para string
        arg_caminho = self.converterParaString(self, arg_caminho)
        arg_tipo = self.converterParaString(self, arg_tipo)
        arg_nome = self.converterParaString(self, arg_nome)
                
        # convertendo JSON para Markdown
        if self.converterJsonParaMarkdown(self, arg_caminho, arg_tipo, arg_nome):
            print('\nDocumentacao gerada com sucesso no caminho: \'' + arg_caminho + '\'')
        else:
            print('\nErro ao gerar documentacao.')


    def converterJsonParaMarkdown(self, caminho, tipo, nome):
        
        # variaveis
        lista_documentacoes = []

        # pegando conteudo do arquivo
        conteudo_arquivo = self.ler(self, caminho, nome)

        # tomando decisão de acordo com o tipo do arquivo
        if str(tipo).lower() == 'der':
            lista_documentacoes = self.gerarDocumentacoesDER(self, conteudo_arquivo)
        elif str(tipo).lower() == 'mer':
            lista_documentacoes = self.gerarDocumentacoesMER(self, conteudo_arquivo)
        else:
            print("\nTipo de arquivo não encontrado!")
            exit()
            
        # compondo toda a documentacao em uma unica string
        conteudo_arquivo = self.comporDocumentacao(self, lista_documentacoes)

        # gravando dados em arquivo externo
        self.gravar(self, caminho, conteudo_arquivo)

        return True
        

    def gerarDocumentacoesDER(self, objetos_UML):
        
        # variaveis
        lista_documentacoes = []

        # 1 - verificando se o valor da chave '_type' eh 'Project'
        if objetos_UML['_type'] == 'Project':
            objetos_UML = objetos_UML['ownedElements'][0]
        else:
            pass
        
        # 2 - verificando se o valor da chave '_type' eh 'UMLModel'
        if objetos_UML['_type'] == 'UMLModel':
            objetos_UML = objetos_UML['ownedElements']
            for entidade in objetos_UML:
                if entidade.get('_type'):
                    if entidade['_type'] == 'UMLEnumeration':
                        if entidade.get('documentation'):
                            lista_documentacoes.append(entidade['documentation'])
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            
            for entidade in objetos_UML:
                if entidade.get('_type'):
                    if entidade['_type'] == 'UMLInterface':
                        if entidade.get('documentation'):
                            lista_documentacoes.append(entidade['documentation'])
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            
            for entidade in objetos_UML:
                if entidade.get('_type'):
                    if entidade['_type'] == 'UMLClass':
                        if entidade.get('documentation'):
                            #print(entidade.get('name'))
                            lista_documentacoes.append(entidade['documentation'])
                        else:
                            pass
                    elif entidade['_type'] == 'UMLModel':
                        if entidade.get('ownedElements'):
                            objetos_UML2 = entidade['ownedElements']
                            for entidade in objetos_UML2:
                                if type(entidade) == dict:
                                    if entidade.get('_type'):
                                        if entidade['_type'] == 'UMLClass':
                                            if entidade.get('documentation'):
                                                #print(entidade.get('name'))
                                                lista_documentacoes.append(entidade['documentation'])
                                            else:
                                                pass
                    else:
                        pass
                else:
                    pass
        
        else:
            pass

        return lista_documentacoes


    def gerarDocumentacoesMER(self, objetos_UML):
        
        # variaveis
        lista_documentacoes = []

        # 1 - verificando se o valor da chave '_type' eh 'Project'
        if objetos_UML['_type'] == 'Project':
            objetos_UML = objetos_UML['ownedElements'][0]
        else:
            pass
        
        # 2 - verificando se o valor da chave '_type' eh 'UMLModel'
        if objetos_UML['_type'] == 'UMLModel':
            objetos_UML = objetos_UML['ownedElements'][0]
        else:
            pass

        # 3 - verificando se o valor da chave '_type' eh 'ERDDataModel'
        if objetos_UML['_type'] == 'ERDDataModel':
            objetos_UML = objetos_UML['ownedElements']
            for entidade in objetos_UML:
                if entidade.get('_type'):
                    if entidade['_type'] == 'ERDEntity':
                        if entidade.get('documentation'):
                            lista_documentacoes.append(entidade['documentation'])
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            
            for entidade in objetos_UML:
                if entidade.get('_type'):
                    if entidade['_type'] == 'ERDDiagram':
                        if entidade.get('documentation'):
                            lista_documentacoes.append(entidade['documentation'])
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            
        else:
            pass
            
        return lista_documentacoes


    def comporDocumentacao(self, lista_documentacoes):
        
        # variaveis
        documentacoes = None

        # tranformando a lista de documentacoes em um unica string
        for documentacao in lista_documentacoes:
            if documentacoes:
                documentacoes = str(documentacao) + '\n\n\n' + str(documentacoes)
            else:
                documentacoes = str(documentacao)

        return documentacoes

    
    def gravar(self, caminho, conteudo, nome='documentacao.txt'):
        
        # validando caminho e nome do arquivo
        self.validarDiretorio(self, caminho, nome)

        # gravando toda a string de documentacao em um unico arquivo
        arquivo = open(os.path.join(caminho, nome), 'w')
        arquivo.write(conteudo)
        arquivo.close()

        return True


    def ler(self, caminho, nome):

        # validando caminho e nome do arquivo
        self.validarDiretorio(self, caminho, nome)

        # lendo conteudo do arquivo 'umj'
        arquivo = open(os.path.join(caminho, nome), 'r')
        conteudo_arquivo = json.load(arquivo)
        arquivo.close()

        return conteudo_arquivo

    
    def validarDiretorio(self, caminho, nome):
        
        if os.path.isfile(os.path.join(caminho, nome)):
            pass
        else:
            print('\nCaminho ou nome do arquivo incorretos')
            exit()

        return True


    def converterParaString(self, valor):
        
        # convertendo valor em string
        if type(valor) == str:
            pass
        else:
            if type(valor) == list:
                valor = str(valor[0])
            else:
                valor = str(valor)

        return valor

    
    def verificarArgumentos(self, objeto, atributo):
        if hasattr(objeto, atributo):
            objeto.func(ArquiteturaEstrategica, objeto)
        else:
            print('\nFaltam argumentos! Tente novamente.')
            exit()
            

if __name__ == '__main__':
    
    interpretador_argumentos = argparse.ArgumentParser(description='Ferramentas uteis para uso geral')
    comandos = interpretador_argumentos.add_subparsers()
    
    # mapeando argumentos
    ArquiteturaEstrategica.mapearArgumentos(comandos)
    
    # pegando os argumentos
    args = interpretador_argumentos.parse_args()

    # verificando os argumentos
    ArquiteturaEstrategica.verificarArgumentos(ArquiteturaEstrategica, args, 'func')
