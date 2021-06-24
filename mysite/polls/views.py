from django import http
from django.shortcuts import render
from django.http import HttpResponse, response

# This is how all that data is visually shown and accsed through request and responses
#Templates are really aiming  the website engaging to the user, seprating how the data is being SHOWN from what the data is actually.
def index(request): #A request,  which allows you to see the webpages we see today
    return HttpResponse("Hello, world. You're at the polls index.") #If the response is accepted, well you'll see Hello world.

# Create your views here.
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of of question %s."
    return HttpResponse(response%question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
#After writing these, you have to wire them back towards the urls path polls/url.py