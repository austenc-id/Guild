from django.db.models.signals import post_save
from django.dispatch import receiver
from _project.settings import AUTH_USER_MODEL


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_profile(sender, instance, **kwargs):
    from .models import Profile
    user_profile = Profile.objects.create(user=instance)
    user_profile.save()
