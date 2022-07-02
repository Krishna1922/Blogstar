from django.core.checks import messages
from django.http import HttpResponse, request
from django.shortcuts import render
from django.contrib.auth.models import User

def handleSignup():
    if request.method == 'POST':
        Fname = request.POST('First-name')
        Lname = request.POST('last-name')
        email = request.POST('autoSizingInputGroup')
        username = request.POST('exampleInputtext')
        password = request.POST('exampleInputPassword1')


        myuser = User.objects.create_user(username, email, password)  
        myuser.first_name = Fname
        myuser.last_name = Lname
        myuser.save()
        messages.success(request, "Your Blogstar account has been successfully created")  
        

    else:
        return HttpResponse('404-Error not found')









    