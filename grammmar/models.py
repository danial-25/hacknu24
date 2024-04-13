from django.db import models


class Grammar_find_word(models.Model):
    text = models.TextField()
    answer = models.TextField()
    options = models.JSONField(default=list)
