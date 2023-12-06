from django.db import models
from django.utils import timezone

class Todolist(models.Model):
    name = models.CharField(max_length=50,  default='default_name')
    value = models.PositiveSmallIntegerField(null=True, default='default_value')
    datetime_field = models.DateTimeField(default=timezone.now, null=True)
    comments = models.TextField(blank=True, null=True, default='default_comments')
    username = models.CharField(max_length=50, null=True, default='default_username')
    email = models.EmailField(max_length=254, null=True, blank=True, default='default_email')
    password = models.CharField(max_length=500, default='default_password')


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-value']
