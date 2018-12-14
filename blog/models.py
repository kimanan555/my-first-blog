from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class dt(models.Model):
    pH=models.FloatField(max_length=3)
    temp=models.FloatField(max_length=3)
    Ec=models.FloatField(max_length=3)
    Water=models.FloatField(max_length=3)

class dt2(models.Model):
    pH=models.FloatField(max_length=3)
    temp=models.FloatField(max_length=3)
    Ec=models.FloatField(max_length=3)
    Water=models.FloatField(max_length=3)
    # temp=models.IntegerField(default=0)
    # Ec=models.IntegerField(default=0)
    # Water=models.IntegerField(default=0)
