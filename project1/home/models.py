from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

# Create your models here.
class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Issue = models.TextField()
    Phone = models.CharField(max_length=13)
    Email = models.CharField(max_length=100)
    Time = models.TimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return  'Message from ' + self.Name

class Signup(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    Time = models.TimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'signup of' + self.fname


    """def clean_email(self,request):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email).exists():
            messages.error(request, "This username is already taken")
        return email"""
#default user model of signup and login