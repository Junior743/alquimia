from json_listas import Listas
from json import dumps
from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.response import Response
from pyramid.config import Configurator
from wsgiref.simple_server import make_server


class Aplicacao(object):

    def mapearRotas(self, configurador):
        
        # mapeando rotas
        configurador.add_route(name='animais', pattern='/animais')
        configurador.add_route(name='animal', pattern='/animais/{id}')
        
        return configurador


@view_defaults(route_name='animais', renderer='json')
class Animais(object):

    def __init__(self, request):
        self.requisicao = request
        self.animais = Listas.lista_animais['animais']
        
    @view_config(request_method='GET')
    def listar(self):
        try:

            return Response(dumps(self.animais))

        except:
            return 'Erro ao consultar animais'

    @view_config(route_name='animal', request_method='GET')
    def pegar(self):
        try:
            
            # variaveis
            animal = None

            # pegando id do animal
            id_animal = self.requisicao.matchdict['id']
            
            # procurando animal na lista de animais
            #animal = (animal for animal in self.animais if str(animal['id']) == str(id_animal))
            for _animal in self.animais:
                if str(_animal['id']) == str(id_animal):
                    animal = _animal
                else:
                    pass
            
            if animal:
                return Response(dumps(animal))
            else:
                return 'Animal não encontrado'
                
        except:
            return 'Erro ao consultar animal'

    @view_config(request_method='POST')
    def adicionar(self):
        try:

            # pegando o objeto animal
            animal = self.requisicao.json_body

            # adicionar o objeto animal a listas de animais
            self.animais.append(animal)

            return animal

        except:
            return 'Erro ao adicionar animal'

    @view_config(request_method='PUT')
    def atualizar(self):
        try:
            
            # pegando o animal
            novo_animal = self.requisicao.json_body
            
            # procurando animal na lista de animais
            #animal = (animal for animal in self.animais if str(id_animal) == str(animal['id']))
            for indice, _animal in enumerate(self.animais):
                    if str(_animal['id']) == str(novo_animal['id']):
                        self.animais[indice] = novo_animal
                        return Response(dumps(novo_animal))
                    else:
                        pass

            return 'Animal não encontrado'
        
        except:
            return 'Erro ao atualizar animal'

    @view_config(route_name='animal', request_method='DELETE')
    def deletar(self):
        try:
            
            # pegando o animal
            id_animal = self.requisicao.matchdict['id']
            
            # procurando animal na lista de animais
            #animal = (animal for animal in self.animais if str(id_animal) == str(animal['id']))
            for indice, _animal in enumerate(self.animais):
                    if str(_animal['id']) == str(id_animal):
                        self.animais.pop(indice)
                        return Response('Animal deletado')
                    else:
                        pass

            return 'Animal não encontrado'
            
        except:
            return 'Erro ao deletar animal'


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