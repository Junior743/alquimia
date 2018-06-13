from pyramid.httpexceptions import HTTPNotImplemented
from controllers import ControllerProduct
from utils import enContentType


class ViewProduct(object):

    @classmethod
    def process(cls, request):
        if request.content_type == enContentType.application_json.value:
            return ControllerProduct.add(request)
        elif request.content_type == enContentType.multipart_formdata.value:
            return ControllerProduct.process(request)
        else:
            return HTTPNotImplemented()

    @classmethod
    def get_result(cls, request):
        return ControllerProduct.get_result(request)
