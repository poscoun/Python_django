from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    todos = ToDo.objects.all()
    content = {'todos' : todos}
    return render(request, 'my_to_do_app/index.html', content)

def createTodo(request):
    input = request.POST['todoContent']

    content = ToDo(contents = input)
    content.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse('createTodo page : ' + input)

def doneTodo(request):
    done_id = request.GET['todoNum']
    todo = ToDo.objects.get(id = done_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))













