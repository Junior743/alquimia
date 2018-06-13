from pyramid.response import Response
from pyramid.view import view_config

from json import (
    dumps,
    loads
)


@view_config(name="add_usr", route_name="usuarios/", request_method="POST")
def adicionar(request):
    return dumps({"user":"created"})

@view_config(name="atu_usr", route_name="usuarios/{codigo}", request_method="PUT")
def atualizar(request):
    return dumps({"user":"updated"})

@view_config(name="del_usr", route_name="usuarios/{codigo}", request_method="DELETE")
def deletar(request):
    return dumps({"user":"deleted"})