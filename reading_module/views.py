from django.shortcuts import render
import os
from .models import Reading_module, Reading_puzzle
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Create your views here.


@api_view(["GET"])
@permission_classes([AllowAny])
def answer_questions(request, level):
    # question = request.GET.get("id")
    all_obj = Reading_module.objects.filter(level=level)

    response_data = []
    for obj in all_obj:
        response_data.append(
            {
                "text": obj.text,
                "questions": obj.questions,
                "options": obj.options,
                "answer": obj.answer,
                "level": obj.level,
            }
        )

    return Response(response_data)


@api_view(["GET"])
@permission_classes([AllowAny])
def reading_puzzle(request):
    # question = request.GET.get("id")
    all_obj = Reading_puzzle.objects.all()

    response_data = []
    for obj in all_obj:
        response_data.append(
            {
                "rus_word": obj.rus_word,
                "kaz_word": obj.kaz_word,
                "shuffled_kaz_word": obj.shuffled_kaz_word,
            }
        )

    return Response(response_data)
