from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .tasks import send_welcome_email  # This is your celery task

@receiver(post_save, sender=User)
def trigger_welcome_email(sender, instance, created, **kwargs):
    if created:
        # Call Celery task
        send_welcome_email.delay(instance.email, instance.username)
