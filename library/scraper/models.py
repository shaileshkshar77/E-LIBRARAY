from django.db import models
from django.utils import timezone

from autoslug import AutoSlugField


class Book(models.Model):
    title = models.CharField(max_length=1000, null=True, default='no title found')
    slug = AutoSlugField(populate_from='title', null=True, unique=True)
    author = models.CharField(max_length=500, null=True, default='no author found')
    date = models.CharField(max_length=100, null=True, default='no date found')
    size = models.CharField(max_length=100, null=True, default='size not available')
    download_link = models.CharField(max_length=1000, null=True, default='download link not available')
    category = models.CharField(max_length=1000, null=True, default='Technology')

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def str(self):
        return self.title

