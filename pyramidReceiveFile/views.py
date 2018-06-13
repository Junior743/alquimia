from controllers import ControllerProduct


class ViewProduct(object):

    @classmethod
    def view_process(cls, request):
        return ControllerProduct.controller_process(request)

    @classmethod
    def view_get_result(cls, request):
        return ControllerProduct.controller_get_result(request)
