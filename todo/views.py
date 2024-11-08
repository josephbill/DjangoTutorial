# Create your views here.
## a method to list our tasks
## a method to create the tasks
# method to list task
from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
def task_list(request):
    # all records in the db
    # rows : represent the object /columns
    tasks = Task.objects.all()
    return render(request,'todo/task_list.html',{'tasks':tasks})

def task_create(request):
    # cover validity
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html',{'form': form})

