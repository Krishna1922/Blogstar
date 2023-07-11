from django.urls import path,include
from . import views # it import views



urlpatterns = [
     path('',views.blogHome,name='blogHome'),
     path('create/',views.Create_Blog,name='create'),
     path('postcomments',views.postComments,name='postcomments'),
     path('<str:user>/<int:pid>',views.blogPost,name='blogPost'),
     path('<str:user>/',views.User_Profile,name='profile'),


]

