from django.urls import path
from custom_error import views

urlpatterns = [
    path('403/', views.permission_denied_view)
]
