from django.urls import path

from . import views # the '.' means from ALL accesable directories, you're looking into it

urlpatterns = [
    path('',views.index, name='index'), # You're url is a list of path functions, kinda wild.
    path('<int:question_id>/', views.detail,name="detail"), # Polls path that allows you to view the question  NUMBER
    path('<int:question_id>/results/',views.results, name="results"), # Polls path allowing u to view the results of the question you answered
    path('<int:question_id>/resuts/',views.vote, name="vote") #polls path letting you see/choices and choosing one.

]

#make sure all urls are going/pointed in the correct area
