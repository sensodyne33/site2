from django.urls import path 
from . import views


#name this whole URL page for articles with an appname
#so it doesn't create confusion when we have other apps with names such as list or detail
app_name = 'articles'

urlpatterns = [
    #this URL already refers to homepage so we need to modify the project urls.py to include this app url
    path('', views.article_list, name="list"),
    #create template for users to create new article and if user wants to view, need log in
    path('create/', views.article_create, name="create"),
    #slug is the type of param passed, and second slug is the name of the param (abc,-,etc)
    path('<slug:slug>/', views.article_detail, name="detail"), #we can give this path a name to include it in href of template
    path('<int:id>/delete', views.article_delete, name='delete'),
    path('<int:id>/update', views.article_update, name='update'),
]