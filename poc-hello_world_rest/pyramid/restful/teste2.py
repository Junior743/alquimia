from wsgiref.simple_server import make_server
from pyramid.response import Response
from pyramid.config import Configurator
from pyramid.view import view_defaults
from pyramid.view import view_config

@view_defaults(route_name='user')
class USERView(object):
    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET')
    def get(self):
        return Response('get')

    @view_config(request_method='POST')
    def post(self):
        return Response('post')

    @view_config(request_method='PUT')
    def put(self):
        return Response('put')

    @view_config(request_method='DELETE')
    def delete(self):
        return Response('delete')

if __name__ == '__main__':
    config = Configurator()
    config.add_route('user', '/user')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 8000, app)
    server.serve_forever()