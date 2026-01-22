from django.db import models
from django.contrib.auth.models import User
from projects.models import Project  # upewnij się, że Project istnieje

class Task(models.Model):

    STATUS_CHOICES = [
        ('todo', 'To do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='todo'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

