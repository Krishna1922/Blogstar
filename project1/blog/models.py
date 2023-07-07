
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.utils.timezone import now, datetime
from ckeditor.fields import RichTextField
from django import forms
# Create your models here.

#class Tag(models.Model):
    #tag = models.CharField(max_length=20)


class Blog(models.Model):
    TAGS_CHOICES = (
        ('Film & Animation', 'Film & Animation'),
        ('Autos & Vehicles','Autos & Vehicles'),
        ('Music','Music'),
        ('Pets & Animals','Pets & Animals'),
        ('Sports','Sports'),
        ('Travel & Events','Travel & Events'),
        ('Gaming','Gaming'),
        ('People & Blogs','People & Blogs'),
        ('Comedy','Comedy'),
        ('Entertainment','Entertainment'),
        ('News & Politics','News & Politics'),
        ('Howto & Style','Howto & Style'),
        ('Education','Education'),
        ('Science & Technology','Science & Technology'),
        ('Nonprofits & Activism','Nonprofits & Activism')
    )
    sno = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50, blank=True)
    Title = models.CharField(max_length=50)
    content = RichTextField(blank=True, null=True)
    Time = models.DateTimeField(default=datetime.now)
    Tag = models.CharField(max_length=50, choices=TAGS_CHOICES, default='Web_Development')
    
    def __str__(self):
        return self.Title

class Comment(models.Model):
    Commentpost = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment =  models.TextField()
    Timestamp = models.DateTimeField(default=now)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='+')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-Timestamp']

    def __str__(self):
        return str(self.author) + ' comment ' + str(self.comment)
    

    #children filters all the replies of the comments
    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()


    # is_parent categorizes whether a comment is parent or reply of comment.
    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False





