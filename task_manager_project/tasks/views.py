from django.shortcuts import render
from .models import Task

# This function tells Django: 
# 1. Go to the SQL database.
# 2. Grab all the Task objects.
# 3. Send them to the 'index.html' page.

def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)