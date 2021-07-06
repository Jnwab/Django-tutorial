from django.urls import path

from . import views # the '.' means from ALL accesable directories, you're looking into it
app_name = "polls"
urlpatterns = [
    #Example: /polls/
    path('',views.IndexView.as_view(), name='index'), # You're url is a list of path functions, kinda wild.
    #Example: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # Polls path that allows you to view the question  NUMBER
    #Example polls/5/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), # Polls path allowing u to view the results of the question you answered
    #Example polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'), #polls path letting you see/choices and choosing one.
    
]

#make sure all urls are going/pointed in the correct area
