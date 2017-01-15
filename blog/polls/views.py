from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Question, Choice

# Create your views here.
def index(request):
    latest = Question.objects.order_by('-pub_date')
    template = 'polls/index.html'

    context = {
            'latest': latest,
            }
    print "request", request
    return render(request, template, context )

def details(request, question_id):
    template = 'polls/details.html'

    question = get_object_or_404(Question, pk=question_id)

    context = {
            'question': question,
            }

    return render(request, template, context)


def vote(request, question_id):
    template = "polls/details.html"
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.filter(pk=request.POST['choice'])

    if selected_choice:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    else:
        return render(
                request, template,
                {
                    'question': question,
                    'error_message': "Please select a choice"
                }
            )

def results(request, question_id):
    template = "polls/results.html"
    question = get_object_or_404(Question, pk=question_id)

    context = {
            'question': question,
            }

    return render(request, template, context)

















