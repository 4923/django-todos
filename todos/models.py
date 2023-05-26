from django.db import models
from django.conf import settings 

# Create your models here.
class Todo(models.Model):
    title = models.TextField()
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
    )
    
    def __str__(self):
        return f'{self.title} - {self.completed}'