from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def found(request):
    # ...
    return HttpResponse('<h1>Page was found</h1>')


def not_found(request):
    # ...
    return HttpResponseNotFound('<h1>Page not found</h1>')


