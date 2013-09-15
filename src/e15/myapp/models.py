from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=16)
    company = models.CharField(max_length=30)

class Book(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    author = models.ForeignKey(Author)
