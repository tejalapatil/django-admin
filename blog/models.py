from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title
