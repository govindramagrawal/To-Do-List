from django.contrib import admin
from . import views
from django.urls import include, path

urlpatterns = [
    path("", views.home, name="home"),
    path("add_task/", views.add_task, name="add_task"),
    path("edit_task/<int:task_id>/", views.edit_task, name="edit_task"),
    path("toggle_done/<int:task_id>/", views.toggle_done, name="toggle_done"),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
]