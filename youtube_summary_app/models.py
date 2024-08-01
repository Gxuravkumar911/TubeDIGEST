from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    summary = models.TextField(blank=True)
# Create your models here.
