from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserMnager


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title


class CustomeUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageFiled(upload_to='profile_photo/', null=True blank=True)




