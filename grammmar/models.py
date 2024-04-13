from django.db import models


class Grammar_find_word(models.Model):
    text = models.TextField()
    answer = models.TextField()
    options = models.JSONField(default=list)

class Grammar_choose_correct(models.Model):
    question = models.TextField()
    answer = models.TextField()
    word_to_replace = models.TextField()
    options = models.JSONField(default=list)