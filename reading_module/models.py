from django.db import models


# Create your models here.
class Reading_module(models.Model):
    text = models.TextField()
    questions = models.TextField()
    options = models.JSONField(default=list)
    answer = models.TextField()
    level = models.IntegerField(default=1)


class Reading_puzzle(models.Model):
    rus_word = models.TextField()
    kaz_word = models.TextField()
    shuffled_kaz_word = models.TextField()
