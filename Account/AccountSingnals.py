from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from Account.models import NormalProfile, ServiceProviderProfile, DistributorProfile


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        NormalProfile.objects.create(user=instance,
                                     name=instance.first_name,
                                     profile_pick="/Default/1Free-Nature-image.jpg",
                                     profile_Background_pic="/Default/2Free-Nature-imgae.jpg")
        ServiceProviderProfile.objects.create(user=instance,
                                              SerV_name=instance.first_name,
                                              SerV_Profile_pick="/Default/SeviceProfile.png")
        DistributorProfile.objects.create(user=instance,
                                          DisB_name=instance.first_name,
                                          DisB_Profile_pick="/Default/DistProfile.png")

