from pyramid.response import Response
from pyramid.view import view_config

from json import (
    dumps,
    loads
)


@view_config(name="add_per", route_name="perfis/", request_method="POST")
def adicionar(request):
    return dumps({"profile":"created"})

@view_config(name="atu_per", route_name="perfis/{codigo}", request_method="PUT")
def atualizar(request):
    return dumps({"profile":"updated"})

@view_config(name="del_per", route_name="perfis/{codigo}", request_method="DELETE")
def deletar(request):
    return dumps({"profile":"deleted"})