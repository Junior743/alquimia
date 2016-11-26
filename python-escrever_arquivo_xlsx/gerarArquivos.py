import pandas as pandas
import os

class GeradorArquivos(object):
    
    def __init__(self):
        dados = {
            'Coluna 1':['Valor 1', 'Valor 2', 'Valor 3', 'Valor 4', 'Valor 5'],
            'Coluna 2':['Maças', 'Laranjas', 'Abacaxis', 'Peras', 'Bananas'],
            'Coluna 3':['Lapis Colorido', 'Apontador', 'Borracha', 'Lapiseira', 'Lapis'],
            'Coluna 4':['Notebook', 'Mesa', 'Mouse', 'Teclado', 'Fones'],
            'Coluna 5':['Onibus', 'Metro', 'Moto', 'Carro', 'Aviao'],
            'Coluna 6':['Empresa', 'Superior', 'Salario', 'Cargo', 'Nome']
        }

        GeradorArquivos.gerarArquivosXLSX(dados, 'arquivos/', 'arquivos_teste', 'Aba Padrão', False)


    def gerarArquivosXLSX(dados, caminho, nome_arquivo, nome_aba, com_indice):
        # Declaração de variaveis
        dict_padrao = {}
        linha = 0
        coluna = 0
        
        # Comparações
        nome_aba = nome_aba if nome_aba else 'Sheet1' 
        caminho = caminho if caminho else ''

        # Iniciando arquivo a ser gravado
        caminho_gravacao = pandas.ExcelWriter(caminho + nome_arquivo + '.xlsx', engine='xlsxwriter')
        
        for indice, valores in dados.items():
            for valor in valores:

                if linha == 0:
                    # Adicionando valores ao data frame
                    data_frame_padrao = pandas.DataFrame.from_dict([{indice:valor}])
                else:
                    # Adicionando valores ao data frame
                    data_frame_padrao = pandas.DataFrame.from_items({indice, valor})

                # Gravando valores em formato XLSX (excel)
                data_frame_padrao.to_excel(caminho_gravacao, sheet_name=nome_aba, index=com_indice, startrow=linha, startcol=coluna)

                linha += 1

            linha = 0
            coluna += 1

        # Gravando arquivo
        caminho_gravacao.save()

GeradorArquivos()