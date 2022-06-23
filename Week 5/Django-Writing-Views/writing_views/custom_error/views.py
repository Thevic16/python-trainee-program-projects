from django.core.exceptions import PermissionDenied
from django.http import HttpResponse


# Create your views here.
def response_error_handler(request, exception=None):
    return HttpResponse('Error handler content', status=403)


def permission_denied_view(request):
    raise PermissionDenied

