# Reference: https://stackoverflow.com/questions/10991460/django-get-current-user-in-model-save
from threading import current_thread

from django.utils.deprecation import MiddlewareMixin


_requests = {}


def current_request():
    try:
        return _requests.get(current_thread().ident, None)
    except Exception as e:
        print("Probably no session here!")
        raise


class RequestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        _requests[current_thread().ident] = request

    def process_response(self, request, response):
        # when response is ready, request should be flushed
        _requests.pop(current_thread().ident, None)
        return response

    def process_exception(self, request, exception):
        # if an exception has happened, request should be flushed too
        _requests.pop(current_thread().ident, None)
