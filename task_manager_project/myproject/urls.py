from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # This links to the built-in Django Admin site
    path('admin/', admin.site.id),
    
    # This tells the project to look at your 'tasks' folder for addresses
    path('', include('tasks.urls')),
]