from json import dumps
from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.response import Response
from listas import Listas
from categorias_ponto_movimentacao import CategoriaPontoMovimentacao
from produtos import Produto
from receitas import Receita
from itens_receitas import ItemReceita
from cadernos import Caderno
from planogramas import Planograma


@view_defaults(route_name='pontos_movimentacao')
class PontoMovimentacao(object):

    def __init__(self, request):
        
        self.requisicao = request
        self.categoria_ponto_movimentacao = CategoriaPontoMovimentacao
        self.produto = Produto
        self.receita = Receita
        self.item_receita = ItemReceita
        self.caderno = Caderno
        self.planograma = Planograma

    @view_config(route_name='pontos_movimentacao', request_method='GET')
    def listar(self):
        try:
            
            return Response(dumps(Listas.lista_pdm))

        except:
            return Response('Erro ao consultar lojas')

    @view_config(route_name='ponto_movimentacao', request_method='GET')
    def pegar(self):
        try:
            
            pdm = None
            lista_pdm = Listas.lista_pdm
            id_pdm = self.requisicao.matchdict['id']
            
            for _pdm in lista_pdm:
                if str(_pdm['id']) == str(id_pdm):
                    pdm = _pdm
                else:
                    pass

            if pdm:
                return Response(dumps(pdm))
            else:
                return Response('Loja não encontrada')

        except:
            return Response('Erro ao consultar loja')

    @view_config(request_method='POST')
    def adicionar(self):
        try:
            
            lista_pdm = Listas.lista_pdm
            novo_pdm = self.requisicao.json_body
            
            if novo_pdm:
                for _pdm in lista_pdm:
                    if 'id' in _pdm.keys():
                        if str(_pdm['id']) == str(novo_pdm['id']):
                            return Response('Loja já existente')
                        else:
                            pass
                    else:
                        return Response('Estrutura JSon informada não coincide com a estrutura do contrato')
            else:
                return Response('Informe a estrutura JSon de loja conforme o contrato')

            Listas.lista_pdm.append(novo_pdm)
            return Response(dumps(novo_pdm))
            
        except:
            return Response('Erro ao adicionar loja')

    @view_config(request_method='PUT')
    def atualizar(self):
        try:
            
            indice = None
            lista_pdm = Listas.lista_pdm
            novo_pdm = self.requisicao.json_body
            id_pdm = self.requisicao.matchdict['id']

            if novo_pdm and id_pdm:
                for _indice, _pdm in enumerate(lista_pdm):
                    if str(_pdm['id']) == str(id_pdm):
                        indice = _indice
                        break
                    else:
                        pass
            else:
                return Response('Informe o id de uma receita e suas novas configurações')

            if indice or indice == 0:
                Listas.lista_pdm[indice] = novo_pdm
                return Response(dumps(novo_pdm))
            else:
                return Response('Receita não encontrada')
            
        except:
            return Response('Erro ao atualizar receita')

    # analizar se este metodo eh importante
    @view_config(route_name='ponto_movimentacao', request_method='PATCH')
    def modificar(self):
        try:
            return 0
        except:
            return Response('Erro ao modificar loja')

    @view_config(route_name='ponto_movimentacao', request_method='DELETE')
    def excluir(self):
        try:
            
            indice = None
            lista_pdm = Listas.lista_pdm
            id_pdm = self.requisicao.matchdict['id']

            if id_pdm:
                for _indice, _pdm in enumerate(lista_pdm):
                    if str(_pdm['id']) == str(id_pdm):
                        indice = _indice
                        print(indice)
                        break
                    else:
                        pass
            else:
                return Response('Informe o id de uma loja e suas novas configurações')
                
            
            if indice or indice == 0:
                Response(dumps(Listas.lista_pdm.pop(int(indice))))
                return Response('Loja excluida com sucesso')
            else:
                return Response('Loja não encontrada')
            
        except:
            raise
            return Response('Erro ao excluir loja')

    @view_config(route_name='ponto_movimentacao_receita', request_method='GET')
    def listarReceitas(self):
        try:

            lista_receitas_encontradas = []
            lista_receitas = Listas.lista_receitas
            lista_pdm = Listas.lista_pdm
            id_pdm = self.requisicao.matchdict['id']
            
            for _pdm in lista_pdm:
                if str(_pdm['id']) == str(id_pdm):
                    lista_receitas_no_pdm = _pdm['receitas']
                    for _receita_no_pdm in lista_receitas_no_pdm:
                        for _receita in lista_receitas:
                            if _receita_no_pdm['id'] == _receita['id']:
                                lista_receitas_encontradas.append(_receita)
                            else:
                                pass
                else:
                    pass

            if lista_receitas_encontradas:
                return Response(dumps(lista_receitas_encontradas))
            else:
                return Response('Não há receitas nesta loja')
                
        except:
            return Response('Erro ao consultar receitas na loja')