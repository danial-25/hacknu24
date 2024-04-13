from django.urls import path
from . import views

urlpatterns = [
    path("grammar/find_word", views.find_word),
]
