from django.urls import path

from . import views # the '.' means from ALL accesable directories, you're looking into it

urlpatterns = [
    path('',views.index, name='index') # You're url is a list of path functions, kinda wild.
]

#make sure all urls are going/pointed in the correct area
