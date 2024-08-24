from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib import admin




class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageFiled(upload_to='profile_photo/', null=True blank=True)

    objects = CustomeUserManager()

class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')
            email = self.normalize_email(email)
            user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
            user.save(using=self.db)
            return user

    def create_superuser(self, username, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, date_of_birth, password, **extra_fields)








