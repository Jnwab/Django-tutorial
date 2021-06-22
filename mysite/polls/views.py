from django.shortcuts import render
from django.http import HttpResponse


def index(request): #A request,  which allows you to see the webpages we see today
    return HttpResponse("Hello, world. You're at the polls index.") #If the response is accepted, well you'll see Hello world.

# Create your views here.
