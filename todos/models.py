from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ProLicense(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_pro = models.BooleanField(default=False)

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='todo_images/', blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
