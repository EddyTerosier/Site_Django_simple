from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.views.decorators.http import require_POST
from django.urls import reverse

def today_str():
    return datetime.now().strftime('%d/%m/%Y')

def home(request):
    return render(request, 'home.html', {'today': today_str()})

def about(request):
    return render(request, 'about.html', {'today': today_str()})

def task_list(request):
    qs = Task.objects.all()
    total = qs.count()
    active = qs.filter(completed=False).count()
    done = qs.filter(completed=True).count()
    ctx = {
        "today": today_str(),
        "tasks": qs,
        "total": total,
        "active": active,
        "done": done,
        "title": "Toutes les tâches",
    }
    return render(request, "tasks/list.html", ctx)

def task_active(request):
    qs = Task.objects.filter(completed=False).order_by("-created_at")
    ctx = {
        "today": today_str(),
        "tasks": qs,
        "total": Task.objects.count(),
        "active": qs.count(),
        "done": Task.objects.filter(completed=True).count(),
        "title": "Tâches actives",
    }
    return render(request, "tasks/list.html", ctx)

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    ctx = {"today": today_str(), "task": task}
    return render(request, "tasks/detail.html", ctx)

def task_add(request):
    if request.method == "POST":
        title = (request.POST.get("title") or "").strip()
        if title:
            Task.objects.create(title=title)
        return redirect("tasks:list")
    return redirect("tasks:list")

@require_POST
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    next_url = request.POST.get("next") or reverse("tasks:detail", args=[task.pk])
    task.completed = not task.completed
    task.save(update_fields=["completed"])
    return redirect(next_url)