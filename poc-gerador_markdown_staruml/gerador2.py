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
            lista_documentacoes = GeradorDocumentacao.PegarDocumentacoes(self, conteudo_arquivo)

            # Compondo string de documentacao
            documentacao_composta = GeradorDocumentacao.ComporDocumentacao(self, lista_documentacoes)

            # Gravando em arquivo de saida
            arquivo_saida = open(arquivo.split('.')[0] + '.txt', 'w')
            arquivo_saida.write(str(documentacao_composta))
            arquivo_saida.close()
            

    def BuscarDocumentacoes(self, conteudo_arquivo_json):
        
        lista_documentacoes = []

        if conteudo_arquivo_json.get('ownedElements'):
            conteudo_arquivo_json = conteudo_arquivo_json['ownedElements']

            lista_documentacoes += GeradorDocumentacao.BuscarDocumentacoes(self, conteudo_arquivo_json)

            for bloco_json in conteudo_arquivo_json:
                if bloco_json.get('_type'):
                    if bloco_json['_type'] in lista_etiquetas:
                        if bloco_json.get('documentation'):
                            lista_documentacoes.append(bloco_json['documentation'])
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
        else:
            pass

        return lista_documentacoes


    def PegarDocumentacoes(self, conteudo_arquivo_json):
        
        lista_documentacoes = []
        lista_etiquetas = ['Project', 'UMLModel', 'ERDDataModel', 'ERDEntity', 'ERDDiagram', 'UMLEnumeration', 'UMLInterface', 'UMLClass']
        lista_etiquetas_excessao = []
        
        if conteudo_arquivo_json.get('_type'):
            if conteudo_arquivo_json['_type'] in lista_etiquetas:
                if conteudo_arquivo_json.get('documentation'):
                    print('olaaaaaaaaaaaaaa')
                    lista_documentacoes.append(conteudo_arquivo_json['documentation'])
                else:
                    pass

                lista_documentacoes += GeradorDocumentacao.BuscarDocumentacoes(self, conteudo_arquivo_json)
            else:
                pass
        else:
            pass

        return lista_documentacoes
            
    
    def ComporDocumentacao(self, lista_documentacoes):
        
        documentacoes = None

        if lista_documentacoes:
            for documentacao in lista_documentacoes:
                if documentacoes:
                    documentacoes = str(documentacao) + '\n\n\n' + str(documentacoes)
                else:
                    documentacoes = str(documentacao)

        return documentacoes


GeradorDocumentacao()