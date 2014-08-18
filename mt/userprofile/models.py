from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.userprofile

def create_user_profile(sender, instance, **kwargs):
    p = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User, dispatch_uid="Userprofile created")

