from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    # context = {'message':'Hello,world!'}
    q = Question.objects.all()
    context = {'new_list':q}
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    q = Question.objects.get(id=question_id)
    context = {'question':q}
    return render(request,'polls/detail.html',context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
