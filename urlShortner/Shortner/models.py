from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=10000, primary_key=True)
    uuid = models.CharField(max_length=10)