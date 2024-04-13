from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Grammar_find_word
import random


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def construct_sentence(request):
#     count = Grammar.objects.count()
#     random_index = random.randint(0, count - 1)
#     random_object = Grammar.objects.all()[random_index]
#     return Response({'sentence':random_object.text, 'options':random_object.options})


@api_view(["GET"])
@permission_classes([AllowAny])
def find_word(requests):
    response_data = []
    all_obj = Grammar_find_word.objects.all()
    for obj in all_obj:
        response_data.append(
            {
                "text": obj.text,
                "answer": obj.answer,
                "options": obj.options,
            }
        )

    return Response(response_data)
