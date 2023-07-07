
from django.shortcuts import redirect, render,HttpResponse
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from home.models import contact,Signup
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from blog.models import Blog


def entry_not_found(request, exception, template_name='404.html'):
    return render(request, template_name)

def index(request):
    if request.user.is_authenticated:
        post = Blog.objects.all()
        context = {'allposts' : post}
        return render(request, 'blog.html',context)

    return render(request, 'home/index.html')

@login_required
def Contact(request):
    

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        issue = request.POST['content']
        
        if len(name)<2 or len(email)<10 or len(phone)<10 or len(issue)<4:
            messages.error(request, 'Please fill the form Correctly')

        else:
            messages.success(request, 'Your Query is successfully send to admin')
            b = contact(Name = name,Phone = phone, Email = email,Issue = issue)
            b.save()
        # inserting in db
        
    return render(request, 'home/contact.html')

@login_required
def tags(request):
    
    return render(request, 'home/tags.html')


def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        


        # check if enter input is wrong
        if len(username) > 10:
            messages.error(request, 'Please enter username under 10 characters')
            return redirect('/')
        if not username.isalnum():
            messages.error(request, 'username should only contains letter and numbers')
            return redirect('/')
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('/')

        myuser = User.objects.create_user(username,email,password)  
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save() 
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
        return render(request,'home/tags.html')

    else:
        return HttpResponse('404 - Error not found')
    
def login_view(request):
    
    if request.method == 'POST':

        # get post parameter from the user
        loginemail = request.POST['email1']
        loginpassword = request.POST['pass1']
        print('email',loginemail)
        print('pass1',loginpassword)

        # authenticate user
        user = authenticate(username=loginemail,password=loginpassword)
        
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully logged in')
            return redirect('blogHome')
        else:
            messages.error(request,'Invalid username or password,Please try again')
            return redirect('/')
        

def handlelogout(request):
        logout(request)
        messages.success(request,'Logout Successfully')
        return redirect('/')

# make prpoer theme of UI
# unique authentication of unique user
# messages show in current page
# Verfication of email etc.
@login_required
def search(request):
    if request.user.is_authenticated:
        query = request.GET['query']
        if len(query)==0:
            messages.warning(request, 'you are searching nothing')
        if len(query) > 50:
            post = Blog.objects.none()
        else:
            allpost = Blog.objects.filter(Title__icontains=query)
            content = Blog.objects.filter(content__icontains=query)
            
            post = allpost.union(content)
        
        if post.count()==0:
            messages.error(request, 'Try check your spells')
        context = {'allposts' : post , 'query':query}
        return render(request, 'home/search.html', context)
    return HttpResponse('You have to first login again')

