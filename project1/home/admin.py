from django.contrib import admin
from home.models import contact,Signup, User_profile


# Register your models here.
admin.site.register(contact)
admin.site.register(Signup)
admin.site.register(User_profile)