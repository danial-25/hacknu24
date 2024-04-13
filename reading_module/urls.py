from django.urls import path
from . import views

urlpatterns = [
    path("reading", views.answer_questions),
]
