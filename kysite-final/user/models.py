from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
 #blank= True, null=True

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length= 100,null=True)
    college_name = models.CharField(max_length=200,null=True)
    phone_number = models.IntegerField(null=True)
    fb_profile_link = models.CharField(blank=True,max_length=200,null=True)

    REQUIRED_FIELDS = ['full_name', 'college_name', 'phone_number']
    def __str__(self):
        return self.user.username

    '''@receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()'''

    @staticmethod
    def post_save_create(sender, instance, created, **kwargs):
        if created:
            profile, created = Profile.objects.get_or_create(user=instance)


post_save.connect(Profile.post_save_create, sender=User)
