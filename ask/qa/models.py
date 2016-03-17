from __future__ import unicode_literals

from django.db import models
#from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
class Likes(models.Model):
    added_ad = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)

    class META:
        db_table = "likes"


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(User, null=True)
    likes = models.ForeignKey(Likes, null=True)

    def get_url(self):
        return self.title

    class META:
        db_table = "question"


class Answer(models.Model):
    text = models.TextField()
    added_ad = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True)
    question = models.ForeignKey(Question, null=True)

    class META:
        db_table = "answer"

