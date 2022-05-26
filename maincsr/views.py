from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): # view for homepage
    return render(request, "home.html")

def login_page(request): # view for loginpage
    return render(request, "loginpage.html")
    
def signup_page(request): # view for sign in page
    return render(request, "signuppage.html")
