from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import json


class Animais(object):
    
    # variaveis
    lista_animais = [
        {
            'nome':'A',
            'tipo':'Cachorro',
            'medidas':{
                'altura':0.5,
                'peso':20
            }
        },
        {
            'nome':'B',
            'tipo':'Gato',
            'medidas':{
                'altura':0.3,
                'peso':10
            }
        },
        {
            'nome':'C',
            'tipo':'Leopardo',
            'medidas':{
                'altura':1,
                'peso':70
            }
        }
    ]

    # metodos
    def mapearRotas(self, configurador):

        # mapeando rotas
        configurador.add_route(name='principal', pattern='/', request_method='GET')
        configurador.add_route(name='listar', pattern='/listar', request_method='GET')
        configurador.add_route(name='pegar', pattern='/pegar/{nome}', request_method='GET', request_param='nome=123')
        configurador.add_route(name='adicionar', pattern='/adicionar/{animal}')
        configurador.add_route(name='atualizar', pattern='/atualizar/{animal}')
        configurador.add_route(name='modificar', pattern='/modificar/{animal}')

        # atribuindo comportamentos as rotas
        configurador.add_view(self.principal, route_name='principal', request_method='GET')
        configurador.add_view(self.listar, route_name='listar', request_method='GET')
        configurador.add_view(self.pegar, route_name='pegar', request_method='GET', request_param='nome=123')
        configurador.add_view(self.adicionar, route_name='adicionar')
        configurador.add_view(self.atualizar, route_name='atualizar')
        configurador.add_view(self.modificar, route_name='modificar')

        return configurador


    #@view_config(name='principal', request_method='GET', context=City, renderer='json')
    @view_config(route_name='principal', request_method='GET')
    def principal(request):
        
        return Response('Olá mundo!')
        
    @view_config(route_name='listar', request_method='GET')
    def listar(request):
        
        return Response(json.dumps(Animais.lista_animais[0]))


    @view_config(route_name='pegar', request_method='GET')
    def pegar(request):
        
        return Response('pegar')


    @view_config(route_name='adicionar', request_method='POST')
    def adicionar(request):

        return Response('adicionar')


    @view_config(route_name='atualizar', request_method='POST')
    def atualizar(request):

        return Response('atualizar')


    @view_config(route_name='modificar', request_method='POST')
    def modificar(request):

        return Response('modificar')


if __name__ == '__main__':
    # instanciando o configurador
    configurador = Configurator()

    # mapeando rotas
    configurador = Animais.mapearRotas(Animais, configurador)

    # configurando WSGI
    app = configurador.make_wsgi_app()

    # servindo
    server = make_server('127.0.0.1', 8000, app)
    server.serve_forever()