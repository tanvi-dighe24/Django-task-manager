from django.urls import path
from . import views

urlpatterns = [
    # This means the empty path (homepage) will run the 'task_list' logic
    path('', views.task_list, name='task_list'),
]