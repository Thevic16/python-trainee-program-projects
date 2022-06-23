from django.urls import path, re_path, register_converter

from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

# Captured parameters ---------------------------------------------------------


urlpatterns = [
    # sample URLconf ----------------------------------------------------------
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/',
         views.year_archive,
         name='news-year-archive'), # Reverse resolution of URLs --------------
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),

    # Registering custom path converters --------------------------------------
    path('converters/articles/<yyyy:year>/', views.year_archive),

    # Using regular expressions -----------------------------------------------
    re_path(r'^regex/articles/(?P<year>[0-9]{4})/$', views.year_archive),
    re_path(r'^regex/articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',
            views.month_archive),
    re_path(r'^regex/articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/'
            r'(?P<slug>[\w-]+)/$',
            views.article_detail),

    # Nested arguments
    re_path(r'^blog/(page-(\d+)/)?$', views.blog_articles),  # bad
    re_path(r'^comments/(?:page-(?P<page_number>\d+)/)?$', views.comments),
    # good

    # Specifying defaults for view arguments
    path('default/blog/', views.page),
    path('default/blog/page<int:num>/', views.page),

    # Passing extra options to view functions
    path('blog/<int:year>/', views.year_archive, {'foo': 'bar'}),
]
