from django.db import models
from django.utils import timezone

class Todolist(models.Model):
    name = models.CharField(max_length=50)
    value = models.PositiveSmallIntegerField()
    datetime_field = models.DateTimeField(default=timezone.now)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-value']
