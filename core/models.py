from django.db import models

class priority(models.TextChoices):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

class status(models.TextChoices):
    ACTIVE = 'Active'
    COMPLETED ='Completed'


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=priority.choices, default=priority.MEDIUM)
    status = models.CharField(max_length=10, choices=status.choices, default=status.ACTIVE)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.title