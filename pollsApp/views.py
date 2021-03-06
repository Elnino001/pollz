from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'pollsApp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by('-pub_date')[:]
    
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return render(request, 'pollsApp/index.html', context)

    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'pollsApp/detail.html'
    # question = get_object_or_404(Question, pk = question_id)
    # return render(request, 'pollsApp/detail.html', {'question':question})
   



# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'pollsApp/result.html', {'question': question})
class ResultView(generic.DetailView):
    model = Question
    template_name = 'pollsApp/result.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id) 
    try: 
        selected_choice = question.choice_set.get(pk=request.POST['choice']) 
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form. 
        return render(request, 'pollsApp/detail.html', { 'question': question, 'error_message': "You didn't select a choice.", }) 
    else: 
        selected_choice.votes += 1 
        selected_choice.save() 
        # Always return an HttpResponseRedirect after successfully dealing  with POST data. This prevents data from being posted twice if a user hits the Back button. 
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # return HttpResponse(f"You're voting on question {question_id}")

def name(request, firstName):
    return HttpResponse(f"your name is {firstName}")
