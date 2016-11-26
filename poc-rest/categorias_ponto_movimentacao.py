from json import dumps
from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.response import Response
from listas import Listas


@view_defaults(route_name='categorias_ponto_movimentacao')
class CategoriaPontoMovimentacao(object):
    
    def __init__(object, request):

        self.requisicao = request
        self.ponto_movimentacao = PontoMovimentacao

    @view_config(request_method='GET')
    def listar(self):
        try:

            return 0

        except:
            return 'Erro ao consultar categorias'

    @view_config(route_name='ponto_movimentacao', request_method='GET')
    def pegar(self):
        try:
            return 0
        except:
            return 'Erro ao consultar categoria'

    @view_config(request_method='POST')
    def adicionar(self):
        try:
            return 0
        except:
            return 'Erro ao adicionar categoria'

    @view_config(request_method='PUT')
    def atualizar(self):
        try:
            return 0
        except:
            return 'Erro ao atualizar loja categoria'

    # analizar se este metodo eh importante
    @view_config(route_name='ponto_movimentacao', request_method='PATH')
    def modificar(self):
        try:
            return 0
        except:
            return 'Erro ao modificar loja categoria'

    @view_config(route_name='ponto_movimentacao', request_method='DELETE')
    def excluir(self):
        try:
            return 0
        except:
            return 'Erro ao excluir loja categoria'