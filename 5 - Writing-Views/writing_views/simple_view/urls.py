from django.urls import path
from simple_view import views

urlpatterns = [
    path('simple_view/', views.current_datetime)
]
