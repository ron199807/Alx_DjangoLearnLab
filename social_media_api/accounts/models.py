from django.db import models

class User(models.Model):
    bio = TextField()
    profile_picture = ImageField()
    followers = 
