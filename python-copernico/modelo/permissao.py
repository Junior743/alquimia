import traceback


class Permissao(object):

    def __init__(self, *args, **kwargs):

        self.codigo = kwargs.get("codigo", None)
        self.nome = kwargs.get("nome", None)

    @classmethod
    def criar(cls):
        """
        Metodo responsavel por criar uma permissão
        """
        try:

            return Permissao()

        except Exception as e:
            traceback.print_exc()
            raise e

    def atualizar(self):
        """
        Metodo responsavel por atualizar uma permissão
        """
        try:

            return self

        except Exception as e:
            traceback.print_exc()
            raise e

    def excluir(self):
        """
        Metodo responsavel por excluir uma permissão
        """
        try:

            return None

        except Exception as e:
            traceback.print_exc()
            raise e