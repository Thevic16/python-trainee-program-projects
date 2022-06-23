from django.urls import path
from return_error import views

urlpatterns = [
    path('found/', views.found),
    path('not_found/', views.not_found)
]
