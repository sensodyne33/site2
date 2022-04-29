from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    #show snippet of articles instead of whole text body
    #update this on templates
    def snippet(self):
        return self.body[:100] + "..." #cut text to 50 chars
















# NOTES:

########### INTERACTING WITH CODE AND DATABASE USING PYTHON ORM ######################
#to interact with our Articles table, do python manage.py shell
#import Articles into the shell; from (articles)appname.models import (Articles)ClassnameofModel
#to see all queries in our Articles table: Articles.objects.all() --> output: Articles: Article object(1)
    #we want to see actual title of this object so we use def __str__(self): return self.title
#create an instance of an Article to be added: article1 = Articles()
    # add fields to article obj: article1.title = "Hello, world"
#save the changes: article.save()
#retrieve the first object's title: Articles.objects.all()[0].title

