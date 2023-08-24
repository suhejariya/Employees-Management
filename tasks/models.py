from django.db import models


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),]
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    completion_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title