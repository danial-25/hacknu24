from django.urls import path
from . import views

urlpatterns = [
    path("reading", views.answer_questions),
    path("reading_puzzle", views.reading_puzzle),
]
