from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student

@receiver(post_save, sender=Student)
def save_profile(sender, instance=None, created=False, dispatch_uid="test", **kwargs):
    post_save.disconnect(save_profile, sender=sender)
    Student.update_all_instances()
    post_save.connect(save_profile, sender=sender)