import traceback

from pyramid.httpexceptions import (
    HTTPError, 
    HTTPForbidden, 
    HTTPClientError,
    HTTPBadRequest,
    HTTPNotImplemented, 
    HTTPPreconditionFailed, 
    HTTPInternalServerError, 
    HTTPRequestRangeNotSatisfiable
)
from json import (
    dumps,
    loads
)


class HTTPBadRequest(HTTPBadRequest):
    """
    subclass of :class:`~HTTPClientError`

    This indicates that the server did not find anything matching the
    Request-URI.

    code: 404, title: Not Found

    Raise this exception within :term:`view` code to immediately
    return the :term:`Not Found View` to the invoking user.  Usually
    this is a basic ``404`` page, but the Not Found View can be
    customized as necessary.  See :ref:`changing_the_notfound_view`.

    This exception's constructor accepts a ``detail`` argument
    (the first argument), which should be a string.  The value of this
    string will be available as the ``message`` attribute of this exception,
    for availability to the :term:`Not Found View`.
    """
    code = 404
    title = 'Not Found'
    explanation = ('The resource could not be found.')

class Excecao(object):
    
    @classmethod
    def compor(cls, excecao, mensagem=None):
        '''
        Metodo responsavel por compor a exceção em formato de resposta para a API
        '''
        try:

            mensagem = mensagem if mensagem else str(excecao)

            if type(excecao) is Exception or\
                type(excecao) is TypeError or\
                type(excecao) is ValueError:
                excecao = HTTPBadRequest(mensagem)
            else:
                excecao = HTTPInternalServerError(mensagem)

            _json = cls.construir_json_excecao(excecao, mensagem)
            return _json

        except Exception as e:
            traceback.print_exc()
            raise e

    @staticmethod
    def construir_json_excecao(excecao, mensagem):
        """
        Metodo responsavel por construir a estrutura JSON para a exceção
        """
        try:

            return {
                "Erro":mensagem
            }

        except Exception as ex:
            traceback.print_exc()
            raise ex
