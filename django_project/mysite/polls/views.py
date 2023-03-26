from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Question,Choice,QuestionForm,ChoiceForm
from .forms import myform

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"你没有选择",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))
    
def question_input(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = form.save()
            q.save()
            return HttpResponseRedirect(reverse('polls:index'))
    else:
        form = QuestionForm()
        return render(request,'polls/question_input.html',{'form':form})

def get_name(request):
    if request.method == 'POST':
        form = myform(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = myform()

    return render(request,'polls/name.html',{'form':form})

def thanks(request):
    return HttpResponse("你输入的是："+request.POST['user_name'])