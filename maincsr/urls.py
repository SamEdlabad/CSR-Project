from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    #above two lines of code take yyou to the same page, the second path is added to facilitate logout redirect
    #path('login-page/', views.login_page),
    path('sign-up-page/', views.signup_page),
    path('Company-sign-up-page/', views.company_signup_page),
    path('NGO-sign-up-page/', views.ngo_signup_page),
]
