import traceback


class Perfil(object):

    def __init__(self, *args, **kwargs):

        self.codigo = kwargs.get("codigo", None)
        self.nome = kwargs.get("nome", None)
        self.permissoes = kwargs.get("permissoes", [])

    @classmethod
    def criar(cls):
        """
        Metodo responsavel por criar um perfil
        """
        try:

            return Perfil()

        except Exception as e:
            traceback.print_exc()
            raise e

    def atualizar(self):
        """
        Metodo responsavel por atualizar um perfil
        """
        try:

            return self

        except Exception as e:
            traceback.print_exc()
            raise e

    def excluir(self):
        """
        Metodo responsavel por excluir um perfil
        """
        try:

            return None

        except Exception as e:
            traceback.print_exc()
            raise e