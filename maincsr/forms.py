from django import forms
from django.forms import ModelForm 
from django import forms
from .models import *

class NGOsignUp(ModelForm):
    ngo_name = models.TextInput()
    passwd = models.TextInput(max_length = 32)
    no_of_employees= models.IntegerField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    address = models.TextField()
    description= models.TextField()
