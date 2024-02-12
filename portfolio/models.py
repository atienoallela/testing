from django.db import models


# Create your models here.
class Profile(models.Model):
    profilephoto = models.ImageField(upload_to='images/')


class Experience(models.Model):
    logo = models.ImageField(upload_to='images/')
    role = models.CharField(max_length=30)
    role_description = models.TextField()

    def __str__(self):
        return self.role


class Contact(models.Model):
    email = models.EmailField(max_length=250)
    feedback = models.TextField()

