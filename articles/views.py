from django.http import HttpResponse
from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse

# Create your views here.
def article_list(request):
    articles = Articles.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

#receive slug from the URL and sending it back to browser
def article_detail(request,slug):
    # return HttpResponse(slug)
    #look for article with specific slug and store it in the variable article
    article = Articles.objects.get(slug=slug)
    #we use render to get the request and render it to a template
    #third param is the data we getting from the DB which we want to render to template
    return render(request, 'articles/article_detail.html', {'article': article})