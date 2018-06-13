from pyramid.config import Configurator
from wsgiref.simple_server import make_server
from pyramid.renderers import JSON
from zope.interface.registry import Components
from json import (
    dumps,
    loads
)

from api import VisaoUsuario


class JSON(JSON):
    """ Renderer that returns a JSON-encoded string.

    Configure a custom JSON renderer using the
    :meth:`~pyramid.config.Configurator.add_renderer` API at application
    startup time:

    .. code-block:: python

       from pyramid.config import Configurator

       config = Configurator()
       config.add_renderer('myjson', JSON(indent=4))

    Once this renderer is registered as above, you can use
    ``myjson`` as the ``renderer=`` parameter to ``@view_config`` or
    :meth:`~pyramid.config.Configurator.add_view`:

    .. code-block:: python

       from pyramid.view import view_config

       @view_config(renderer='myjson')
       def myview(request):
           return {'greeting':'Hello world'}

    Custom objects can be serialized using the renderer by either
    implementing the ``__json__`` magic method, or by registering
    adapters with the renderer.  See
    :ref:`json_serializing_custom_objects` for more information.

    .. note::

        The default serializer uses ``json.JSONEncoder``. A different
        serializer can be specified via the ``serializer`` argument.  Custom
        serializers should accept the object, a callback ``default``, and any
        extra ``kw`` keyword arguments passed during renderer construction.
        This feature isn't widely used but it can be used to replace the
        stock JSON serializer with, say, simplejson.  If all you want to
        do, however, is serialize custom objects, you should use the method
        explained in :ref:`json_serializing_custom_objects` instead
        of replacing the serializer.

    .. versionadded:: 1.4
       Prior to this version, there was no public API for supplying options
       to the underlying serializer without defining a custom renderer.
    """

    def __init__(self, serializer=dumps, adapters=(), **kw):
        """ Any keyword arguments will be passed to the ``serializer``
        function."""
        self.serializer = serializer
        self.kw = kw
        self.components = Components()
        for type, adapter in adapters:
            self.add_adapter(type, adapter)

    def __call__(self, info):
        """ Returns a plain JSON-encoded string with content-type
        ``application/json``. The content-type may be overridden by
        setting ``request.response.content_type``."""
        def _render(value, system):
            import pdb; pdb.set_trace()
            
            request = system.get('request')
            if request is not None:
                response = request.response
                ct = response.content_type
                if ct == response.default_content_type:
                    response.content_type = 'application/json'
            default = self._make_default(request)
            return self.serializer(value, default=default, **self.kw)

        return _render

if __name__ == "__main__":
    with Configurator() as config:

        ## adicionando rotas
        config.add_route("usuarios", "/usuarios")

        ## adicionando visoes
        config.add_view(VisaoUsuario.adicionar, request_method="POST", route_name="usuarios", renderer="myjson")
        config.add_view(VisaoUsuario.atualizar, request_method="PUT", route_name="usuarios", renderer="myjson")
        config.add_view(VisaoUsuario.excluir, request_method="DELETE", route_name="usuarios", renderer="myjson")

        ## adicionando renderers
        config.add_renderer("myjson", JSON(indent=4))

        app = config.make_wsgi_app()

    server = make_server("0.0.0.0", 8080, app)
    print("Provendo em: 0.0.0.0:8080")
    server.serve_forever()