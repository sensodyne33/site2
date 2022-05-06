from django.contrib import admin
#we want Articles model to show in our admin page
from .models import Articles
# from django_summernote.admin import SummernoteModelAdmin

@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    # displaying posts with title slug and created time
    list_display = ('title', 'slug', 'date')
    # list_filter = ("status", )
    search_fields = ['title', 'body']
    # prepopulating slug from title
    prepopulated_fields = {'slug': ('title', )}




