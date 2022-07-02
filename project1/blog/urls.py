from django.urls import path,include
from . import views # it import views



urlpatterns = [
     path('postcomments',views.postComments,name='postcomments'),
     path('<str:slug>',views.blogPost,name='blogPost'),
     path('',views.blogHome,name='blogHome'),
     
     
    
   
    


]

