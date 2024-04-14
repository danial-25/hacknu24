from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json
from .models import User_data


# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def sing_up(requests):
    data = json.loads(requests.body)
    print(data)
    email = data.get("email")
    password = data.get("password")
    user_data, created = User_data.objects.get_or_create(
        email=email,
        defaults={
            "password": password
        },  # Only provide default values if a new object is created
    )

    if created:
        return Response({"message": "User created successfully"}, status=201)
    else:
        return Response({"message": "User with this email already exists"}, status=400)


# @api_view(["POST"])
# @permission_classes([AllowAny])
# def log_in(request):
#     data = request.data  # Retrieve data from request body
#     print(data)
#     email = data.get("email")
#     password = data.get("password")
#     try:
#         user = User_data.objects.get(email=email)
#         if user.password == password:
#             return Response({"first": user.grammar_find_word})
#         return Response(status=202)
#     except User_data.DoesNotExist:
#         return Response(status=404)


@api_view(["POST"])
@permission_classes([AllowAny])
def log_in(requests):
    data = json.loads(requests.body)
    print(data)
    email = data.get("email")
    password = data.get("password")
    user = User_data.objects.get(email=email)
    if user.password == password:
        return Response(status=200)
    return Response(status=202)


@api_view(["GET"])
@permission_classes([AllowAny])
def history(request):
    email = request.GET.get("email")
    if email is not None:
        try:
            u = User_data.objects.get(email=email)
            email_exists = True
        except User_data.DoesNotExist:
            return Response({"error": "User doesn't exist"}, status=403)
        return Response(
            {
                "reading_texts": u.reading_texts,
                "reading_puzzles": u.reading_puzzles,
                "choose_correct": u.grammar_choose_correct,
                "find_word": u.grammar_find_word,
            }
        )
    else:
        return Response({"error": "Email parameter is missing"}, status=400)
