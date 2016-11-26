# 
# Objetivo: Automatizar a geracao de documentos no formato markdown para o portal de documentacao MKDocs. 
# Dsenvolvedor: Junior
# Data: 07/10/2016
#

import sys
import json
import glob

#
# TODOS:
# - Criar gatilho para o github.
# - O programa devera ler arquivos em determinado diretorio, gerar a documentacao para todos os .mdj's do diretorio e por fim salvar a saida em um outro diretorio.
#

class GeradorDocumentacao(object):

    def __init__(self):

        # Variaveis
        documentacao_composta = None
        lista_documentacoes = []
        lista_arquivos = []

        # Buscando arquivos no diretorio
        lista_arquivos = glob.glob('*.mdj')

        for arquivo in lista_arquivos:
            
            # Lendo arquivo de entrada
            arquivo_entrada = open(arquivo, 'r')

            # Pegando o conteudo do arquivo de entrada
            conteudo_arquivo = json.load(arquivo_entrada)

            # Fechando arquivo de entrada
            arquivo_entrada.close()

            # Pegando as documentacoes das entidades
            #lista_documentacoes = GeradorDocumentacao.PegarDocumentacoes(self, conteudo_arquivo)
            lista_documentacoes = GeradorDocumentacao.PegarDocumentacoesDER(self, conteudo_arquivo)

            # Compondo string de documentacao
            documentacao_composta = GeradorDocumentacao.ComporDocumentacao(self, lista_documentacoes)

            # Gravando em arquivo de saida
            arquivo_saida = open(arquivo.split('.')[0], 'w')
            arquivo_saida.write(documentacao_composta)
            arquivo_saida.close()
        

    def PegarDocumentacoes(self, objetos_UML):
        
        lista_documentacoes = []

        # 1
        if objetos_UML['_type'] == 'Project':
            objetos_UML = objetos_UML['ownedElements'][0]
        else:
            pass
        
        # 2
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


    def PegarDocumentacoesDER(self, objetos_UML):
        
        lista_documentacoes = []

        # 1
        if objetos_UML['_type'] == 'Project':
            objetos_UML = objetos_UML['ownedElements'][0]
        else:
            pass
        
        # 2
        if objetos_UML['_type'] == 'UMLModel':
            objetos_UML = objetos_UML['ownedElements'][0]
        else:
            pass

        # 3
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
        
        
    def ComporDocumentacao(self, lista_documentacoes):
        
        documentacoes = None

        for documentacao in lista_documentacoes:
            if documentacoes:
                documentacoes = str(documentacao) + '\n\n\n' + str(documentacoes)
            else:
                documentacoes = str(documentacao)

        return documentacoes


GeradorDocumentacao()