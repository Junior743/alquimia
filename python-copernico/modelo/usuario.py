import traceback


class Usuario(object):

    def __init__(self, *args, **kwargs):

        self.codigo = kwargs.get("codigo", None)
        self.nome = kwargs.get("nome", None)
        self.email = kwargs.get("email", None)
        self.senha = kwargs.get("senha", None)
        self.perfis = kwargs.get("perfis", [])

    @classmethod
    def criar(cls):
        """
        criar um usuario
        """
        try:

            return Usuario()

        except Exception as e:
            traceback.print_exc()
            raise e

    def atualizar(self):
        """
        Metodo responsavel por atualizar um usuario
        """
        try:

            return self

        except Exception as e:
            traceback.print_exc()
            raise e

    def excluir(self):
        """
        Metodo responsavel por excluir um usuario
        """
        try:

            return None

        except Exception as e:
            traceback.print_exc()
            raise e
