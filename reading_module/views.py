from django.shortcuts import render
import os
from .models import Reading_module
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Create your views here.


@api_view(["GET"])
@permission_classes([AllowAny])
def answer_questions(request):
    # question = request.GET.get("id")
    all_obj = Reading_module.objects.all()

    response_data = []
    for obj in all_obj:
        response_data.append(
            {
                "text": obj.text,
                "questions": obj.questions,
                "options": obj.options,
                "answer": obj.answer,
            }
        )

    return Response(response_data)



# @api_view(["GET"])
# @permission_classes([AllowAny])
# def translate_sentence(request):
