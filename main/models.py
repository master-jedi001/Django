from django.db import models


class Task(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description', max_length=256)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Text', max_length=2000)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

