from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request, "home.html", {"tasks": tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        done = request.POST.get("done") == "on"
        task = Task(title=title, description=description, done=done)
        task.save()
        return redirect("home")
    return render(request, "add.html")


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        done = request.POST.get("done") == "on"
        if title:
            task.title = title
            task.description = description
            task.done = done
            task.save()
        return redirect("home")
    return render(request, "edit.html", {"edit_task": task})


def toggle_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done = request.POST.get("done") == "on"
    task.save()
    return redirect("home")


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("home")