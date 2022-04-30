from django.urls import path 
from . import views

urlpatterns = [
    #this URL already refers to homepage so we need to modify the project urls.py to include this app url
    path('', views.article_list),
    #slug is the type of param passed, and second slug is the name of the param (abc,-,etc)
    path('<slug:slug>/', views.article_detail),
]