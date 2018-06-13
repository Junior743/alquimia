from pyramid.response import Response
from pyramid.httpexceptions import (
    HTTPAccepted, 
    HTTPNotFound, 
    HTTPNoContent, 
    HTTPCreated
)
from models import ModelProduct


class ControllerProduct(object):

    @classmethod
    def add(cls, request):
        return HTTPCreated()

    @classmethod
    def process(cls, request):
        _file_storage = request.POST["products"]
        _products = ModelProduct.process(_file_storage)

        return Response(status="202 Accepted", headerlist=[("id_process", _file_storage.filename)])

    @classmethod
    def get_result(cls, request):
        _code_process = request.matchdict.get("code_process")

        _result_process = ModelProduct.get_result(_code_process)
        if _result_process:
            return HTTPNoContent()
        else:
            return HTTPNotFound()
