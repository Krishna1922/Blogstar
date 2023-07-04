
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

#class Tag(models.Model):
    #tag = models.CharField(max_length=20)


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=13)
    slug = models.CharField(max_length=200)
    Time = models.DateTimeField(blank=True)
    
    def __str__(self):
        return self.Title + ' by ' + self.author

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




