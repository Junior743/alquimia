import traceback

from json import (
    dumps,
    loads
)
from pyramid.view import (
    view_config,
    view_defaults
)
from pyramid.response import Response

from modelo import Usuario
from util import Excecao


class VisaoUsuario(object):

    def adicionar(request):
        try:

            return ControladorUsuario.adicionar()
        
        except Exception as ex:
            Excecao.compor(ex)

    def atualizar(request):
        try:

            return ControladorUsuario.atualizar()
        
        except Exception as ex:
            Excecao.compor(ex)

    def excluir(request):
        try:

            return ControladorUsuario.excluir()

        except Exception as ex:
            Excecao.compor(ex)


class ControladorUsuario(object):

    @classmethod
    def adicionar(cls):
        try:

            _usuario = Usuario.criar()
            
            return dumps({"user":"created"})

        except Exception as ex:
            traceback.print_exc()
            raise ex

    @classmethod
    def atualizar(cls):
        try:

            _usuario = Usuario.atualizar()

            return dumps({"user":"updated"})

        except Exception as ex:
            traceback.print_exc()
            raise ex

    @classmethod
    def excluir(cls):
        try:

            _usuario = Usuario.excluir()

            return dumps({"user":"deleted"})

        except Exception as ex:
            traceback.print_exc()
            raise ex
