from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email, username):
    subject = "🎉 Welcome to Our Platform!"
    message = f"Hi {username},\n\nThanks for registering. We're glad to have you!"
    from_email = "msantosh63226@gmail.com"  # ✅ Your real Gmail address

    send_mail(subject, message, from_email, [email])
    return f"✅ Welcome email sent to {email}"
