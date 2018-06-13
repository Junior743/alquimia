from pyramid.response import Response
from pyramid.view import view_config

from json import (
    dumps,
    loads
)


@view_config(name="add_pms", route_name="permissoes/", request_method="POST")
def adicionar(request):
    return dumps({"permission":"created"})

@view_config(name="atu_pms", route_name="permissoes/{codigo}", request_method="PUT")
def atualizar(request):
    return dumps({"permission":"updated"})

@view_config(name="del_pms", route_name="permissoes/{codigo}", request_method="DELETE")
def deletar(request):
    return dumps({"permission":"deleted"})
