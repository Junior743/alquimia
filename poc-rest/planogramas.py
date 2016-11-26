from json import dumps
from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.response import Response
from listas import Listas


@view_defaults(route_name='planogramas')
class Planograma(object):
    
    def __init__(object, request):
        
        self.requisicao = request
        # planograma pode consultar seus PDMs
        self.ponto_movimentacao = PontoMovimentacao

    @view_config(request_method='GET')
    def listar(self):
        try:
            return 0
        except:
            return 'Erro ao consultar planogramas'

    @view_config(route_name='ponto_movimentacao', request_method='GET')
    def pegar(self):
        try:
            return 0
        except:
            return 'Erro ao consultar planograma'

    @view_config(request_method='POST')
    def adicionar(self):
        try:
            return 0
        except:
            return 'Erro ao adicionar planograma'

    @view_config(request_method='PUT')
    def atualizar(self):
        try:
            return 0
        except:
            return 'Erro ao atualizar planograma'

    # analizar se este metodo eh importante
    @view_config(route_name='ponto_movimentacao', request_method='PATH')
    def modificar(self):
        try:
            return 0
        except:
            return 'Erro ao modificar planograma'

    @view_config(route_name='ponto_movimentacao', request_method='DELETE')
    def excluir(self):
        try:
            return 0
        except:
            return 'Erro ao excluir planograma'