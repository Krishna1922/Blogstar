
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required
from blog.models import Blog,Comment
from django.contrib import messages
from blog.templatetags import extras


@login_required
def blogHome(request):

    allPosts = Blog.objects.all()
    context = {'allposts': allPosts}
    
    
    return render(request,'blog/blog.html',context)
@login_required
def blogPost(request, slug): 
    post = Blog.objects.filter(slug=slug).first()
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

    return render(request, 'blog/blogPost.html',context1)

# def postcomments(request):
#     if request.method=='POST':
#         comment = request.POST.get("comment")
#         user = request.user
#         postsno = request.POST.get("postsno") #serial no.
#         post = Post.objects.get(sno = postsno)
#         parentsno = request.POST.get("parentsno")

#         if parentsno == "":
#             commentx = Post_comment(comment=comment, user=user, post=post)
#             commentx.save()
#             messages.success(request, "Your comment has been posted successfully")
#         else:
#             parent= Post_comment.objects.get(sno=parentsno)
#             commentx = Post_comment(comment=comment, user=user, post=post,parent = parent)
#             commentx.save()
#             messages.success(request, "Your reply has been posted successfully")
        


#     return redirect(f"/bloghome{post.slug}")

   # return render(request, 'blog/blogPost.html')

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
        

    return redirect(f"/bloghome{post.slug}")



