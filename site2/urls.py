from django.contrib import admin
from django.urls import path, include #include help us include URLs from our apps
from . import views # helps us reference URLs from web to views' functions related to the URL
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #let django handle static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls), #if we get URL request that ends in admin go to admin site
    path('about/', views.about), # if we get URL request with about/ we go to views.py>about function
    path('', views.home), #if we get URL request with nothing, go to views.py and home function
    path('articles/', include('articles.urls')) #goes to articles.py and runs those URLS; URLs with /articles
]

 #function to server our static files using django
urlpatterns += staticfiles_urlpatterns()

#function to save media
#takes in 2 params: media url and root of those media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)