from django.db import models

# Create your models here.

class TelegramUser(models.Model):
    username = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
