from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Todo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class TodoItem(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

# signals
@receiver(post_save, sender=User)
def todoSignal(sender, instance, created, **kwargs):
    if created:
        Todo.objects.create(user=instance)