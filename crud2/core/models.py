from django.db import models

# Create your models here.

class Marvel(models.Model):
    name=models.CharField(max_length=50)
    mail=models.EmailField(max_length=50)
