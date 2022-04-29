from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import User


@receiver(pre_save, sender=User)
def pre_save_phone_number(sender, instance, **kwargs):
    if instance.phone:
        instance.phone = ''.join(x for x in instance.phone if x.isdigit())
        return instance.phone
