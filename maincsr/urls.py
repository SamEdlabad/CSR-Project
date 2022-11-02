from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    #above two lines of code take you to the same page, the second path is added to facilitate logout redirect
    path('login/', views.login, name= "login"),
    path('logout/', views.logout, name= "logout"),
    path('sign-up-page/', views.signup_page),
    path('Company-sign-up-page/', views.company_signup_page),
    path('NGO-sign-up-page/', views.ngo_signup_page),
    path('dashboard/<str:username>/', views.dashboard),
    path('search/', views.search),
    path('search/results', views.search),
    path('connect/', views.connect),
]

if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
      #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  