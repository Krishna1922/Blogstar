from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from blog.models import Blog,Comment
from home.models import User_profile
from django.contrib import messages
from .forms import CreateForm


@login_required
def blogHome(request):

    allPosts = Blog.objects.all()
    context = {'allposts': allPosts}
    
    
    return render(request,'blog.html',context)
@login_required
def blogPost(request, user, pid): 
    post = Blog.objects.filter(user=user, sno=pid).first()
    comment = Comment.objects.filter(Commentpost=post, parent=None)
    replies = Comment.objects.filter(Commentpost=post).exclude(parent=None) #here we got whole replies whose parent 
    # is any user but we not get replies for a particular comment so we apply a for a loop for getting a replies of a particular comment

    replyDict = {}
    for rep in replies:
        if rep.parent.pk not in replyDict.keys():
            replyDict[rep.parent.pk] = [rep]
        else:
            replyDict[rep.parent.pk].append(rep)

    print(replyDict)
    context1 = {'post':post, 'comments':comment, 'replyDict':replyDict}

    return render(request, 'blogPost.html',context1)


def postComments(request):
    if request.method=='POST':
        comment = request.POST.get("content")
        user = request.user
        postsno = request.POST.get("postsno")
        post = Blog.objects.get(sno=postsno)
        parentsno = request.POST.get("parentsno")

        if parentsno == "":
            comment = Comment(comment = comment, author = user, Commentpost = post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = Comment.objects.get(pk=parentsno)
            comment = Comment(comment = comment, author = user, Commentpost = post,parent = parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        

    return redirect(f"/bloghome/{post.user}/{post.sno}")

def Create_Blog(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            user = request.user
            Title = form['Title'].value()
            content = form['content'].value()
            Tag = form['Tag'].value()
            if(len(content) < 50):
                messages.success(request,'content should be atleast 50 char')
                return redirect('/')
            BlogDetail = Blog(user = user, Title = Title, content = content, Tag = Tag)
            BlogDetail.save()
            messages.success(request,'Your Blog has been successfully posted!')
            return redirect('/')
        messages.error(request,'Fill the data correctly :(')
        return redirect(request, '/')
    else:
        form = CreateForm() 
    return render(request, "create.html", {"form": form})

@login_required
def User_Profile(request, user):
    Blog_count = Blog.objects.filter(user = user).count()
    U = User_profile.objects.filter(user = request.user)
    if request.method == 'POST':
        if not U:
            img = request.POST.get('user_profile')
            f = User_profile(user = request.user, profile = img)
            f.save()
        else:
            # U.profile = img
            pass
    context = {
        'cnt' : Blog_count,
        'user' : user
    }
    
    return render(request, 'profile.html', context)

