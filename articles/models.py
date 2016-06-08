from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    """
    Model to hold data about articles
    """
    title = models.CharField(max_length=40)
    headline = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk':self.id})
