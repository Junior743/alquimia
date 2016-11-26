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
        tipo_diagrama = None
        conteudo_arquivo = None
        documentacao_composta = None
        lista_documentacoes = []
        lista_arquivos = []

        # Buscando arquivos no diretorio
        lista_arquivos = glob.glob('*.mdj')

        for arquivo in lista_arquivos:
            
            # Pegando o conteudo do arquivo de entrada
            conteudo_arquivo = GeradorDocumentacao.LerArquivo(self, arquivo)

            # Pegando o tipo do diagrama
            tipo_diagrama = GeradorDocumentacao.VerificarTipoDiagrama(arquivo)

            # Pegando as documentacoes das entidades
            if tipo_diagrama == 'DER' or tipo_diagrama == 'der':
                lista_documentacoes = GeradorDocumentacao.PegarDocumentacoesDER(self, conteudo_arquivo)
            if tipo_diagrama == 'MER' or tipo_diagrama == 'mer':
                lista_documentacoes = GeradorDocumentacao.PegarDocumentacoesMER(self, conteudo_arquivo)
            

            # Compondo string de documentacao
            documentacao_composta = GeradorDocumentacao.ComporDocumentacao(self, lista_documentacoes)

            # Gravando em arquivo de saida
            GeradorDocumentacao.GravarArquivo(self, documentacao_composta, tipo_diagrama)
            
        
    def GravarArquivo(self, conteudo, nome_arquivo='output'):
        
        arquivo_saida = open(nome_arquivo + '.txt', 'w')
        arquivo_saida.write(conteudo)
        arquivo_saida.close()

        return True


    def LerArquivo(self, arquivo):

        arquivo_entrada = open(arquivo, 'r')
        conteudo_arquivo = json.load(arquivo_entrada)
        arquivo_entrada.close()

        return conteudo_arquivo


    def VerificarTipoDiagrama(arquivo):
        
        tipo_arquivo = arquivo.split('.')[0]
        tipo_arquivo = tipo_arquivo.split('_')[-1]

        return tipo_arquivo


    def PegarDocumentacoesDER(self, objetos_UML):
        
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


    def PegarDocumentacoesMER(self, objetos_UML):
        
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