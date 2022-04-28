from django.contrib import admin
from django.urls import path #helps us access requested URL from the web
from . import views # helps us reference URLs from web to views' functions related to the URL


urlpatterns = [
    path('admin/', admin.site.urls), #if we get URL request that ends in admin go to admin site
    path('about/', views.about), # if we get URL request with about/ we go to views.py>about function
    path('', views.home), #if we get URL request with nothing, go to views.py and home function
]
