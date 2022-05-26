from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('login-page/', views.login_page),
    path('sign-up-page/', views.signup_page),
]
