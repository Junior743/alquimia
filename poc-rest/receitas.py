from json import dumps
from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.response import Response
from listas import Listas
from itens_receitas import ItemReceita


@view_defaults(route_name='receitas')
class Receita(object):

    def __init__(self, request):
        
        self.requisicao = request
        self.item_receita = ItemReceita

    @view_config(request_method='GET')
    def listar(self):
        try:
            
            return Response(dumps(Listas.lista_receitas))

        except:
            return Response('Erro ao consultar receitas')

    @view_config(route_name='ponto_movimentacao', request_method='GET')
    def pegar(self):
        try:
            
            receita = None
            lista_receitas = Listas.lista_receitas
            id_receita = self.requisicao.matchdict['id']
            
            for _receita in lista_receitas:
                if str(_receita['id']) == str(id_receita):
                    receita = _receita
                else:
                    pass

            if receita:
                return Response(dumps(receita))
            else:
                return Response('Receita não encontrada')
            
        except:
            return Response('Erro ao consultar receita')

    @view_config(request_method='POST')
    def adicionar(self):
        try:
            
            lista_receitas = Listas.lista_receitas
            nova_receita = self.requisicao.json_body
            
            if nova_receita:
                for _receita in lista_receitas:
                    if 'id' in _receita.keys():
                        if str(_receita['id']) == str(nova_receita['id']):
                            return Response('Receita já existente')
                        else:
                            pass
                    else:
                        return Response('Estrutura JSon informada não coincide com a estrutura do contrato')
            else:
                return Response('Informe a estrutura JSon de receita conforme o contrato')

            Listas.lista_receitas.append(nova_receita)
            return Response(dumps(nova_receita))

        except:
            raise
            return Response('Erro ao adicionar receita')

    @view_config(request_method='PUT')
    def atualizar(self):
        try:
            
            indice = None
            lista_receitas = Listas.lista_receitas
            nova_receita = self.requisicao.json_body
            id_receita = self.requisicao.matchdict['id']

            if nova_receita and id_receita:
                for _indice, _receita in enumerate(lista_receitas):
                    if str(_receita['id']) == str(id_receita):
                        indice = _indice
                        break
                    else:
                        pass
            else:
                return Response('Informe o id de uma receita e suas novas configurações')

            if indice or indice == 0:
                Listas.lista_receitas[indice] = nova_receita
                return Response(dumps(nova_receita))
            else:
                return Response('Receita não encontrada')
            
        except:
            return Response('Erro ao atualizar receita')

    # analizar se este metodo eh importante
    @view_config(route_name='ponto_movimentacao', request_method='PATH')
    def modificar(self):
        try:
            return 0
        except:
            return Response('Erro ao modificar receita')

    @view_config(route_name='ponto_movimentacao', request_method='DELETE')
    def excluir(self):
        try:

            indice = None
            lista_receitas = Listas.lista_receitas
            id_receita = self.requisicao.matchdict['id']

            if id_receita:
                for _indice, _receita in enumerate(lista_receitas):
                    if str(_receita['id']) == str(id_receita):
                        indice = _indice
                        print(indice)
                        break
                    else:
                        pass
            else:
                return Response('Informe o id de uma receita e suas novas configurações')
                
            
            if indice or indice == 0:
                Response(dumps(Listas.lista_receitas.pop(int(indice))))
                return Response('Receita excluida com sucesso')
            else:
                return Response('Receita não encontrada')
            
        except:
            return Response('Erro ao excluir receita')

    def incluirProdutoIndutor():
        try:
            return 0
        except:
            return Response('Erro ao incluir produto indutor')