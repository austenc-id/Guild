from django.db.models.signals import post_save
from django.dispatch import receiver
from project.settings import AUTH_USER_MODEL


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_profile(sender, instance, **kwargs):
    from .models import Profile
    first_name_id = getattr(instance, '_first_name', None)
    user_profile = Profile.objects.create(user=instance)
    user_profile.save()
