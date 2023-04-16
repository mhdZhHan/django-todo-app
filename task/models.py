from django.db import models
from todo.settings import AUTH_USER_MODEL

class Task(models.Model):
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
