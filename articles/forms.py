from django import forms
from . import models

#create a model form
class CreateArticle(forms.ModelForm):
    class Meta:
        #get form data from Articles model
        model = models.Articles
        fields=['title', 'body', 'thumb']


class EditArticles(forms.ModelForm):
    class Meta:
        #get form data from Articles model
        model = models.Articles
        fields=['title', 'body', 'thumb']