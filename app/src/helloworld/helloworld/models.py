from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    question_recording = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
