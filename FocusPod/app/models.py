from django.db import models
from django.conf import settings
# Create your models here.

class Task(models.Model):
    task_content = models.CharField(max_length=200)

    def __str__(self):
        return self.task_content
    
