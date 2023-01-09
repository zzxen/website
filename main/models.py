from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class News(models.Model):
    body = models.TextField()

class PricePanel(models.Model):
    title = models.CharField(max_length = 50 , blank = False , default = "")
    months = models.CharField(max_length = 50 , blank = False , default = "")
    users = models.CharField(max_length = 50 , blank = False , default = "")
    speed = models.CharField(max_length = 50 , blank = False , default = "")
    encryption = models.CharField(max_length = 50 , blank = False , default = "")
    link = models.CharField(max_length = 250 , blank = False , default = "")