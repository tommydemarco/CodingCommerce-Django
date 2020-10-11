from django.db.models.signals import post_save 
from django.contrib.auth.models import User
from django.dispatch import receiver 
from .models import UserProfile

#creating a UserProfile whenever a new User is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

#saving the user profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    instance.UserProfile.save()