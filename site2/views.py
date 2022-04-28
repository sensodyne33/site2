#this returns a HttpResponse back
from django.http import HttpResponse
#render allow us to send back template response from views function
from django.shortcuts import render

#if views.about get accessed, we send back a string to web page
def about(request):
    # return HttpResponse("this is about page")

    #render takes in 2 params; the request and response=template
    return render(request, 'about.html')

#if views.home get accessed, we send back a string to web page
def home(request):
    # return HttpResponse("this is about homepage")

    return render(request, 'homepage.html')