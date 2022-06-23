from django.http import HttpResponse, HttpResponseRedirect


# sample URLconf --------------------------------------------------------------
from django.urls import reverse


def special_case_2003(request):
    html = "<html><body>Special case 2003</body></html>"
    return HttpResponse(html)


def year_archive(request, year, foo=None):
    if foo:
        html = f"<html><body>year_archive: {year} foo: {foo} </body></html>"
    else:
        html = f"<html><body>year_archive: {year} </body></html>"
    return HttpResponse(html)


def month_archive(request, year, month):
    html = f"<html><body>year_archive: {year}" \
           f" month_archive: {month} </body></html>"
    return HttpResponse(html)


def article_detail(request, year, month, slug):
    html = f"<html><body>year_archive: {year}" \
           f" month_archive: {month} " \
           f"article_detail: {slug} </body></html>"
    return HttpResponse(html)


# Nested arguments
def blog_articles(request, page, page_number):
    html = f"<html><h1>page:{page} </h1> <h1>page_number:{page_number}</h1>" \
           f"</html>"
    return HttpResponse(html)


def comments(request, page_number):
    html = f"<html><h1>page_number:{page_number}</h1>" \
           f"</html>"
    return HttpResponse(html)


# Specifying defaults for view arguments --------------------------------------
def page(request, num=1):
    html = f"<html><h1>num:{num}</h1>" \
           f"</html>"
    return HttpResponse(html)


# Reverse resolution of URLs --------------------------------------------------
def redirect_to_year(request):
    # ...
    year = 2006
    # ...
    return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))
