from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import random
# @api_view(['GET'])
# @permission_classes([AllowAny])

# def get_random_words(text):
#     words = text.split()  # Split the string into words
#     random.shuffle(words)  # Shuffle the list of words randomly
#     return words


# def construct_sentence(request):
#     count = Grammar.objects.count()
#     random_index = random.randint(0, count - 1)
#     random_object = Grammar.objects.all()[random_index]
#     return Response({'sentence':random_object.text, 'options':random_object.options})
# def 
