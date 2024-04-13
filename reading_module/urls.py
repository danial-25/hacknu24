from django.urls import path
from . import views

urlpatterns = [
    path("reading/<int:level>", views.answer_questions),
    path("reading_puzzle", views.reading_puzzle),
]
