from json import dumps
from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.response import Response
from pyramid.config import Configurator
from wsgiref.simple_server import make_server
import pontos_movimentacao
import produtos
import receitas
import itens_receitas
import planogramas
import cadernos


class Aplicacao(object):
    
    def mapearRotas(self, configurador):
    
        # mapeando rotas
        configurador.add_route(name='pontos_movimentacao', pattern='/ponto_movimentacao')
        configurador.add_route(name='ponto_movimentacao', pattern='/ponto_movimentacao/{id}')
        configurador.add_route(name='ponto_movimentacao_receita', pattern='/ponto_movimentacao/receita/{id}')
        configurador.add_route(name='categorias_ponto_movimentacao', pattern='/categoria_ponto_movimentacao')
        configurador.add_route(name='categoria_ponto_movimentacao', pattern='/categoria_ponto_movimentacao/{id}')
        configurador.add_route(name='produtos', pattern='/produto')
        configurador.add_route(name='produto', pattern='/produto/{id}')
        configurador.add_route(name='receitas', pattern='/receita')
        configurador.add_route(name='receita', pattern='/receita/{id}')
        configurador.add_route(name='itens_receitas', pattern='/item_receita')
        configurador.add_route(name='item_receita', pattern='/item_receita/{id}')
        configurador.add_route(name='cadernos', pattern='/caderno')
        configurador.add_route(name='caderno', pattern='/caderno/{id}')
        configurador.add_route(name='planogramas', pattern='/planograma')
        configurador.add_route(name='planograma', pattern='/planograma/{id}')

        # mapeando views
        configurador.add_view(pontos_movimentacao.PontoMovimentacao, attr='listar', request_method='GET')
        configurador.add_view(pontos_movimentacao.PontoMovimentacao, attr='pegar', route_name='ponto_movimentacao', request_method='GET')
        configurador.add_view(pontos_movimentacao.PontoMovimentacao, attr='adicionar', request_method='POST')
        configurador.add_view(pontos_movimentacao.PontoMovimentacao, attr='modificar', route_name='ponto_movimentacao', request_method='PATH')
        configurador.add_view(pontos_movimentacao.PontoMovimentacao, attr='atualizar', route_name='ponto_movimentacao', request_method='PUT')
        configurador.add_view(pontos_movimentacao.PontoMovimentacao, attr='excluir', route_name='ponto_movimentacao', request_method='DELETE')
        configurador.add_view(pontos_movimentacao.PontoMovimentacao, attr='listarReceitas', route_name='ponto_movimentacao_receita', request_method='GET')

        configurador.add_view(produtos.Produto, attr='listar', request_method='GET')
        configurador.add_view(produtos.Produto, attr='pegar', route_name='produto', request_method='GET')
        configurador.add_view(produtos.Produto, attr='adicionar', request_method='POST')
        configurador.add_view(produtos.Produto, attr='modificar', route_name='produto', request_method='PATH')
        configurador.add_view(produtos.Produto, attr='atualizar', route_name='produto', request_method='PUT')
        configurador.add_view(produtos.Produto, attr='excluir', route_name='produto', request_method='DELETE')

        configurador.add_view(receitas.Receita, attr='listar', request_method='GET')
        configurador.add_view(receitas.Receita, attr='pegar', route_name='receita', request_method='GET')
        configurador.add_view(receitas.Receita, attr='adicionar', request_method='POST')
        configurador.add_view(receitas.Receita, attr='modificar', route_name='receita', request_method='PATH')
        configurador.add_view(receitas.Receita, attr='atualizar', route_name='receita', request_method='PUT')
        configurador.add_view(receitas.Receita, attr='excluir', route_name='receita', request_method='DELETE')

        configurador.add_view(itens_receitas.ItemReceita, attr='listar', request_method='GET')
        configurador.add_view(itens_receitas.ItemReceita, attr='pegar', route_name='item_receita', request_method='GET')
        configurador.add_view(itens_receitas.ItemReceita, attr='adicionar', request_method='POST')
        configurador.add_view(itens_receitas.ItemReceita, attr='modificar', route_name='item_receita', request_method='PATH')
        configurador.add_view(itens_receitas.ItemReceita, attr='atualizar', route_name='item_receita', request_method='PUT')
        configurador.add_view(itens_receitas.ItemReceita, attr='excluir', route_name='item_receita', request_method='DELETE')

        configurador.add_view(planogramas.Planograma, attr='listar', request_method='GET')
        configurador.add_view(planogramas.Planograma, attr='pegar', route_name='planograma', request_method='GET')
        configurador.add_view(planogramas.Planograma, attr='adicionar', request_method='POST')
        configurador.add_view(planogramas.Planograma, attr='modificar', route_name='planograma', request_method='PATH')
        configurador.add_view(planogramas.Planograma, attr='atualizar', route_name='planograma', request_method='PUT')
        configurador.add_view(planogramas.Planograma, attr='excluir', route_name='planograma', request_method='DELETE')

        configurador.add_view(cadernos.Caderno, attr='listar', request_method='GET')
        configurador.add_view(cadernos.Caderno, attr='pegar', route_name='caderno', request_method='GET')
        configurador.add_view(cadernos.Caderno, attr='adicionar', request_method='POST')
        configurador.add_view(cadernos.Caderno, attr='modificar', route_name='caderno', request_method='PATH')
        configurador.add_view(cadernos.Caderno, attr='atualizar', route_name='caderno', request_method='PUT')
        configurador.add_view(cadernos.Caderno, attr='excluir', route_name='caderno', request_method='DELETE')

        return configurador
        
    
if __name__ == '__main__':
    
    # instanciando o configurador
    configurador = Configurator()

    # mapeando rotas
    configurador = Aplicacao.mapearRotas(Aplicacao, configurador)

    # escaneando rotas
    configurador.scan()

    # configurando WSGI
    app = configurador.make_wsgi_app()

    # servindo
    server = make_server('127.0.0.1', 8000, app)
    server.serve_forever()