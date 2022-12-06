from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Channel(models.Model):
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(User, related_name='add_user', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    channel = models.ManyToManyField(Channel, related_name='add_channel', null=True, blank=True)
    message = models.TextField()

    