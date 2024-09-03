from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)



class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.intField(max_length=10)
    