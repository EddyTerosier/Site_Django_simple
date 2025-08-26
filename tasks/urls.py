from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),

    path("tasks/", views.task_list, name="list"),
    path("tasks/active/", views.task_active, name="active"),
    path("tasks/<int:pk>/", views.task_detail, name="detail"),

    path("tasks/<int:pk>/toggle/", views.task_toggle, name="toggle"),
    path("tasks/add/", views.task_add, name="add"),
]