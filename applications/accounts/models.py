from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class UserProfile(models.Model):
    first_name      = models.CharField(max_length=50, blank=True, null=True)
    last_name       = models.CharField(max_length=50, blank=True, null=True)
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar          = models.ImageField(upload_to='users/avatars', max_length=None)
    nationality     = models.CharField(max_length=50)
    job_title       = models.CharField(max_length=50)
    phone           = models.IntegerField()
    bio             = models.TextField()

    def __str__(self):
        return f'{ self.user.username }\'s profile'

    # #resizing the profile pic upon saving the instance of the profile 
    # def save(self):
    #     super().save()
    #     img = Image.open(self.avatar.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.avatar.path)

