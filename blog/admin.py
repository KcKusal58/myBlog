from django.contrib import admin
from . import models
from blog.models import Blog, Contact


class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all" : ("css/design.css",)
        }

        js = ("js/blog.js",)

admin.site.register(Blog, BlogAdmin)