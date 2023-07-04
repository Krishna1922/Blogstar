from django.urls import path,include
from . import views # it import views



urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.Contact,name='contact'),
    path('tags',views.tags,name='tags'),
    path('signup',views.signup,name='signup'),
    path('login',views.login_view,name='login'),
    path('logout',views.handlelogout,name='handlelogout'),
    path('search',views.search,name='search'),
   
    


]

