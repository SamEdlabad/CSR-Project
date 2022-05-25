from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): # view for homepage
    return render(request, "home.html")
    