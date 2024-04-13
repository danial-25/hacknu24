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


@api_view(["POST"])
@permission_classes([AllowAny])
def log_in(requests):
    data = json.loads(requests.body)
    print(data)
    email = data.get("email")
    password = data.get("password")
    user = User_data.objects.get(email=email)
    if user.password == password:
        return Response({"message": "nice"}, status=200)
    return Response(status=202)

