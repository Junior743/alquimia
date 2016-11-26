from json import dumps
from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.response import Response
from listas import Listas


@view_defaults(route_name='produtos')
class Produto(object):

    def __init__(object, request):
        
        self.requisicao = request
        # produto também pode se autoadicionar em produtos indutores
        self.receita = Receita

    @view_config(request_method='GET')
    def listar(self):
        try:

            return 0

        except:
            return 'Erro ao consultar produtos'

    @view_config(route_name='ponto_movimentacao', request_method='GET')
    def pegar(self):
        try:
            return 0
        except:
            return 'Erro ao consultar produto'

    @view_config(request_method='POST')
    def adicionar(self):
        try:
            return 0
        except:
            return 'Erro ao adicionar produto'

    @view_config(request_method='PUT')
    def atualizar(self):
        try:
            return 0
        except:
            return 'Erro ao atualizar produto'

    # analizar se este metodo eh importante
    @view_config(route_name='ponto_movimentacao', request_method='PATH')
    def modificar(self):
        try:
            return 0
        except:
            return 'Erro ao modificar produto'

    @view_config(route_name='ponto_movimentacao', request_method='DELETE')
    def excluir(self):
        try:
            return 0
        except:
            return 'Erro ao excluir produto'