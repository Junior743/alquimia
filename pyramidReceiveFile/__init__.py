from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from views import ViewProduct


#region [__init__]
if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('products', '/products')
        config.add_route('product', '/products/{code_process}')

        config.add_view(ViewProduct.view_process, route_name='products', request_method="POST")
        config.add_view(ViewProduct.view_get_result, route_name='product', request_method="GET")
        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 8580, app)
    print("Servindo em 0.0.0.0:8580")
    server.serve_forever()
#endregion
