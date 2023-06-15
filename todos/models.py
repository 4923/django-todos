from django.db import models
from django.conf import settings 

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)            # 제목
    body = models.TextField(null=True,default='')       # 상세내용
    completed = models.BooleanField(default=False)      # 완성여부
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
    )                                                   # 작성자
    
    def __str__(self):
        return f'{self.title} - {self.completed}'