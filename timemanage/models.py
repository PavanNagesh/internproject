from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_date = models.DateField()
    task_time = models.TimeField()
