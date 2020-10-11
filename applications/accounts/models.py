from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    first_name      = models.CharField(max_length=50, blank=True, null=True)
    last_name       = models.CharField(max_length=50, blank=True, null=True)
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar          = models.ImageField(upload_to='users/avatars', height_field=None, width_field=None, max_length=None)
    nationality     = models.CharField(max_length=50)
    job_title       = models.CharField(max_length=50)
    phone           = models.IntegerField()
    bio             = models.TextField()

    def __str__(self):
        return f'{ self.user.username }\'s profile'
