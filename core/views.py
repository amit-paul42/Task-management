from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.tasks import task
from .models import Task


def index(request):
    all_tasks = Task.objects.all()
    return render(request, 'index.html', context={"tasks": all_tasks})


def task_create(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', context={})

    elif request.method == 'POST':
        due_date = request.POST.get('due_date') or None

        _ = Task.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            priority=request.POST.get('priority'),
            due_date=due_date,
            tags=request.POST.get('tags')
        )
        return redirect('/')
    else:
        return HttpResponse("<h1>Method not allowed</h1>")


def delete_task(request, pk):
    # task = Task.objects.filter(pk=pk)

    # if not task.exists():
    #    print("not found")
    #    return redirect('/')

     try:
          task = Task.objects.get(pk=pk)
     except Task.DoesNotExist: 
        print("not found")
        return redirect('/')
    
     task.delete()
     return redirect('/')
        
 