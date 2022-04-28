#this returns a HttpResponse back
from django.http import HttpResponse

#if views.about get accessed, we send back a string to web page
def about(request):
    return HttpResponse("this is about page")

#if views.home get accessed, we send back a string to web page
def home(request):
    return HttpResponse("this is about homepage")