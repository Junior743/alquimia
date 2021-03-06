from wsgiref.simple_server import make_server
from pyramid.config import Configurator


if __name__ == "__main__":
    with Configurator() as config:
        config.scan()
        app = config.make_wsgi_app()
    server = make_server("0.0.0.0", 8080, app)
    server.serve_forever()
