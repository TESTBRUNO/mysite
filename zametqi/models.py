from msilib.schema import CheckBox
from turtle import done
from django.db import models

class cloudnotes(models.Model):
    
    text = models.CharField(max_length=100)
    CheckBox = models.BooleanField()

