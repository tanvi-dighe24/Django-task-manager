from django.db import models

class Task(models.Model):
    # This creates a 'Title' column in your SQL database
    title = models.CharField(max_length=200)
    
    # This creates a 'Description' column (optional)
    description = models.TextField(null=True, blank=True)
    
    # This creates a 'Status' checkbox (True/False)
    complete = models.BooleanField(default=False)
    
    # This automatically saves the date the task was made
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title