from xml.etree.ElementTree import Comment
from django.contrib import admin
from blog.models import Blog,Comment

admin.site.register(Comment)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)

