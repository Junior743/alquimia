"""

Cópernico

    Pois foi um dos primeiros a analisar e documentar suas descobertas na astronomia. 
Neste caso a documentar a estrela Sirius.
    Futuramente pode-se automatizar a geração da documentação de outras estrelas.

"""

import traceback

import markdown
from especificacoes import API

from modelo.perfil import Perfil
from modelo.usuario import Usuario
from modelo.permissao import Permissao
from api import (
    perfil,
    usuario,
    permissao
)


REGEX = "\[[A-Z]+ - .+\]"

def listar_arquivos_md():
    """
    Metodo responsavel por listar todos os arquivos md dentro de determinado diretorio
    """
    try:

        return ["/home/bode743/Documents/projetos/alquimia/python-escritor/markdown/seguranca.md"]

    except Exception as e:
        traceback.print_exc()
        raise e

def buscar_primeira_rota(file):
    """
    Metodo responsavel por buscar primeira ocorrencia de padrão de uma URI em um dado arquivo fornecido
    """
    try:

        ## REGEX: REGEX variable
        _rota = "[POST - api/0.0/usuarios]"
        _rota = _rota.replace("[", "").replace("]", "")

        return _rota

    except Exception as e:
        traceback.print_exc()
        raise e

def substituir_md_por_uri(file, markdown, uri):
    """
    Metodo responsavel por fazer a substituição da URI no arquivo fornecido pelo contéudo markdown gerado
    """
    try:

        ## REGEX: REGEX variable
        return True

    except Exception as e:
        traceback.print_exc()
        raise e

def desmembrar_rota(rota):
    """
    Metodo responsavel por pegar metodo http e uri a partir da rota
    """
    ## separando metodo e uri
    _metodo_http, _uri = rota.split("-")
    ## removendo espacos
    _metodo_http = _metodo_http.strip()
    _uri = _uri.strip()

    return _metodo_http, _uri

def documentar(args):
    """
    Metodo responsavel por gerar a documentação da API Sirius.
    """
    _arquivos = listar_arquivos_md()

    for _arquivo in _arquivos:

        with open(_arquivo) as _file:

            _rota = buscar_primeira_rota(_file)

            ## enquando encontrar o padrao de URI no documento markdown
            while _rota:
                ## pegando primeira ocorrencia de URI no documento markdown
                _rota = buscar_primeira_rota(_file)
                ## pegando metodo HTTP e URI a partir da rota
                _metodo_http, _uri = desmembrar_rota(_rota)
                ## documentando a partir do objeto
                _markdown = API(_metodo_http, _uri).documentar()
                ## substituindo URI pelo o markdown
                substituir_md_por_uri(_file, _markdown, _rota)

def capturar_argumentos():
    """
    Metodo responsavel por declarar e capturar os argumentos desejados
    """
    ## declarando parametros de entrada
    parser = ArgumentParser(description="Cópernico - Sistema responsavel pela geração automatica da documentação da estrela Sirius.")
    parser.add_argument("metodo", help="Metodo HTTP para acesso a rota da API")
    parser.add_argument("uri", help="URI para acesso a rota na API")
    parser.add_argument("-a", "--arquivo", help="Arquivo a ser carregado", action="append")

    ## pegando perametros inseridos
    return parser.parse_args()

def executar():
	try:

        args = capturar_argumentos()

		print("Executando...")
		documentar(args)
		print("\n\nConcluido")

	except Exception as ex:
		print("\n\nErro: " + str(ex))


if __name__ == "__main__":
	executar()
