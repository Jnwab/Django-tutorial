from django import http
from django import template
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, request, response,HttpResponseRedirect
from django.template import context, loader
from django.http import Http404
from django.urls import reverse
from  django.views import generic
from .models import Choice, Question
from django.utils import timezone


# This is how all that data is visually shown and accsed through request and responses
#Templates are really aiming  the website engaging to the user, seprating how the data is being SHOWN from what the data is actually.
#def index(request): #A request,  which allows you to see the webpages we see today
    #return HttpResponse("Hello, world. You're at the polls index.") #If the response is accepted, well you'll see Hello world.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        
        #Excludes any questions that aren't  actually published yet.
        
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#After writing these, you have to wire them back towards the urls path polls/url.py