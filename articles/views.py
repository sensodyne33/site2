from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Articles
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.utils.text import slugify
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from django.contrib import messages


@login_required(login_url="/accounts/login/")
def article_list(request):
    articles = Articles.objects.all().filter(author=request.user)
    return render(request, 'articles/article_list.html', {'articles': articles})

#receive slug from the URL and sending it back to browser
def article_detail(request,slug):
    # return HttpResponse(slug)
    #look for article with specific slug and store it in the variable article
    article = Articles.objects.get(slug=slug)
    #we use render to get the request and render it to a template
    #third param is the data we getting from the DB which we want to render to template
    return render(request, 'articles/article_detail.html', {'article': article})


#need to make create page require user login using a decorator
#if user is trying to access create and not logged in use decorator to block access
#then redirect them to login url
@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            #save article to db; but don't save it yet
            instance = form.save(commit=False)
            #attach author first; attach request from user to author
            instance.author = request.user
            instance.slug = slugify(instance.title)
            # instance.slug = slugify(instance)
            #finally save
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})

def article_delete(request, id):
    article = Articles.objects.filter(id=id)
    article.delete()
    return redirect('articles:list')


@login_required
def article_update(request, id):
        obj= get_object_or_404(Articles, id=id)
        form = forms.CreateArticle(request.POST or None, instance= obj)
        context= {'form': form}
        if form.is_valid():
                obj= form.save(commit= False)
                obj.save()
                messages.success(request, "You successfully updated the post")
                context= {'form': form}
                return render(request, 'articles/article_edit.html', context)
        else:
                context= {'form': form,
                           'error': 'The form was not updated successfully. Please enter in a title and content'}
                return render(request,'articles/article_edit.html' , context)
