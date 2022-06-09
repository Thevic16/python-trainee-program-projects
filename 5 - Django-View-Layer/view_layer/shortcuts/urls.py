from django.urls import path
from . import views


urlpatterns = [
    path('render/', views.my_view),
]
