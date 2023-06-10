from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    context = {"tasks":tasks,'form':form}
    return render(request,'app/app.html',context)

def delete_task(request,pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')