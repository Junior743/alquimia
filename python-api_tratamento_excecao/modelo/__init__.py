import traceback

from sqlalchemy.exc import IntegrityError


class Usuario(object):

    def __init__(self, *args, **kwargs):

        self.codigo = kwargs.get("codigo", None)
        self.nome = kwargs.get("nome", None)
        self.email = kwargs.get("email", None)
        self.senha = kwargs.get("senha", None)
        self.perfis = kwargs.get("perfis", [])

    @classmethod
    def criar(cls):
        '''
        metodo responsavel por criar um novo usuario
        '''
        try:

            raise ValueError("O nome do usuário é um atributo obrigatório")

        except Exception as e:
            traceback.print_exc()
            raise e

    @classmethod
    def atualizar(cls):
        '''
        Metodo responsavel por atualizar um usuario
        '''
        try:

            raise AttributeError("O codigo do usuário não pode ser atualizado")

        except Exception as e:
            traceback.print_exc()
            raise e

    @classmethod
    def excluir(cls):
        '''
        Metodo responsavel por excluir um usuario
        '''
        try:

            raise Exception("Usuário não encontrado!")

        except Exception as e:
            traceback.print_exc()
            raise e
