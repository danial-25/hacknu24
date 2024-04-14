from django.urls import path
from . import views

urlpatterns = [
    path("signup", views.sing_up),
    path("login", views.log_in),
    path("history", views.history),
]
