from django.db import models


# Create your models here.
class Reading_module(models.Model):
    text = models.TextField()
    questions = models.TextField()
    options = models.JSONField(default=list)
    answer = models.TextField()
