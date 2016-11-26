# 
# Objetivo: Automatizar a geracao de textos no formato markdown para documentacao no github. 
# Dsenvolvedor: Junior
# Data: 07/10/2016
#

import sys
import json

class GerarDocumentacao(object):

    def __init__(self):

        # Variaveis
        lista_documentacoes = []

        # Pegando paramentros
        lista_parametros = sys.argv

        # Lendo arquivo
        #arquivo = open(lista_parametros[1])
        arquivo = open('input.js', 'r')

        # Pegando o conteudo do arquivo
        conteudo_arquivo = json.load(arquivo)

        # Pegando as documentacoes das entidades
        lista_documentacoes = GerarDocumentacao.PegarElementos(self, conteudo_arquivo)

        # Formatando a documentacao
        #lista_documentacoes = GerarDocumentacao.TratarDados(self, lista_documentacoes)

        # Fechando arquivo
        arquivo.close()

        # Gravando em arquivo
        arquivo = open('output.txt', 'w')
        print(lista_documentacoes[0])
        arquivo.write(lista_documentacoes[0])
        arquivo.close()
        
    def PegarElementos(self, objetos_UML):
        
        lista_documentacoes = []

        if objetos_UML['_type'] == 'Project':
            objetos_UML = objetos_UML['ownedElements'][0]
            return self.PegarElementos(objetos_UML)
        elif objetos_UML['_type'] == 'UMLModel':
            objetos_UML = objetos_UML['ownedElements']
            
            for entidade in objetos_UML:
                if entidade.get('_type'):
                    if entidade['_type'] == 'UMLClass' or entidade['_type'] == 'UMLEnumeration' or entidade['_type'] == 'UMLInterface':
                        if entidade.get('documentation'):
                            lista_documentacoes.append(entidade['documentation'])
                        else:
                            pass
                    else:
                        pass
                else:
                    pass

            return lista_documentacoes


    def TratarDados(self, lista_documentacoes):
        
        lista_documentacoes_formatada = []

        for documentacao in lista_documentacoes:
            documentacao = documentacao.replace('##', '')
            lista_documentacoes_formatada.append(documentacao)

        return lista_documentacoes_formatada


GerarDocumentacao()