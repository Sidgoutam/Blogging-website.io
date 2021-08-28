from django.contrib import admin
from .models import Stories
from tinymce.widgets import TinyMCE
from django.db import models

class StoriesAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/Date" , {"fields":["title","time_of_publish"]}),
        ("Description" , {"fields":["genre","content"]}),
        ("Links" , {"fields":["url"]})
    ]

    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE()}
        }
    
admin.site.register(Stories,StoriesAdmin)
