from django.urls import path
from . import views

urlpatterns = [
    path("grammar/find_word", views.find_word),
    path("grammar/choose_correct", views.choose_correct),
]
