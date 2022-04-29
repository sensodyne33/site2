from django.contrib import admin
#we want Articles model to show in our admin page
from .models import Articles

#tell admin page to register Articles model
admin.site.register(Articles)