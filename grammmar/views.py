from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Grammar_find_word, Grammar_choose_correct
from users.models import User_data
import random


@api_view(["GET"])
@permission_classes([AllowAny])
def find_word(request):

    email = request.GET.get("email")
    if email is not None:
        all_obj = Grammar_find_word.objects.all()
        for obj in all_obj:
            if User_data.objects.get(email=email) is not None:
                a = User_data.objects.get(email=email)
                if obj not in a.grammar_find_word:
                    response = {
                        "text": obj.text,
                        "answer": obj.answer,
                        "options": obj.options,
                    }
                a.grammar_find_word.append(
                    {
                        "text": obj.text,
                        "answer": obj.answer,
                        "options": obj.options,
                    }
                )
                a.save()
    else:
        all_obj = Grammar_find_word.objects.all()
        random_obj = all_obj.order_by("?").first()
        response = {
            "text": random_obj.text,
            "answer": random_obj.answer,
            "options": random_obj.options,
        }
    return Response(response)


@api_view(["GET"])
@permission_classes([AllowAny])
def choose_correct(request):
    response_data = []
    email = request.GET.get("email")
    if email is not None:
        all_obj = Grammar_choose_correct.objects.all()
        for obj in all_obj:
            if User_data.objects.get(email=email) is not None:
                a = User_data.objects.get(email=email)
                if obj not in a.grammar_choose_correct:
                    response = {
                        "question": obj.question,
                        "answer": obj.answer,
                        "options": obj.options,
                        "word_to_replace": obj.word_to_replace,
                    }
                a.grammar_choose_correct.append(
                    {
                        "question": obj.question,
                        "answer": obj.answer,
                        "options": obj.options,
                        "word_to_replace": obj.word_to_replace,
                    }
                )
                a.save()

        else:
            all_obj = Grammar_choose_correct.objects.all()
            random_obj = all_obj.order_by("?").first()
            response = {
                "question": random_obj.question,
                "answer": random_obj.answer,
                "options": random_obj.options,
                "word_to_replace": random_obj.word_to_replace,
            }
    return Response(response)


# @api_view(["GET"])
# @permission_classes([AllowAny])
# def choose_correct(requests):
#     response_data = []
#     all_obj = Grammar_choose_correct.objects.all()
#     for obj in all_obj:
#         response_data.append(
#             {
#                 "question": obj.question,
#                 "answer": obj.answer,
#                 "options": obj.options,
#                 "word_to_replace": obj.word_to_replace,
#             }
#         )

#     return Response(response_data)

# response_data.append(
#             {
#                 "question": obj.question,
#                 "answer": obj.answer,
#                 "options": obj.options,
#                 "word_to_replace": obj.word_to_replace,
#             }
