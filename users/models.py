from django.db import models


# Create your models here.
class User_data(models.Model):
    email = models.EmailField()
    password = models.TextField()
    reading_texts = models.JSONField(default=list)
    reading_puzzles = models.JSONField(default=list)
    grammar_choose_correct = models.JSONField(default=list)
    grammar_find_word = models.JSONField(default=list)
