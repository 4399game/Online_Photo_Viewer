from django.http import QueryDict

try:
    from django.utils.deprecation import MiddlewareMixin
except:
    MiddlewareMixin = object

class Method(MiddlewareMixin):
    def process_request(self, request):
        """
        让DELETE & 方法能够获取参数
        :param request: 原生请求
        :return:
        """
        try:
            http_method = request.META['REQUEST_METHOD']
            if http_method.upper() not in ('GET', 'POST'):
                setattr(
                    request, 
                    http_method.upper(), 
                    QueryDict(request.body)
                )
        except Exception:
            pass
        finally:
            return None