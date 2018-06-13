from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

from pyramid.view import notfound_view_config
from json import dumps

@notfound_view_config()
def notfound(request):
    return Response(dumps({"error":"rota inexistente!!!"}))

def hello_world(request):
    return Response('Hello World!')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    print("Provendo em 0.0.0.0:6543")
    server.serve_forever()