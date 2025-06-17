from django.urls import path
from .views import (
    PublicAPIView,
    ProtectedAPIView,
    TriggerEmailView,
    telegram_webhook,
)

urlpatterns = [
    path('public/', PublicAPIView.as_view(), name='public'),
    path('protected/', ProtectedAPIView.as_view(), name='protected'),
    path('send-email/', TriggerEmailView.as_view(), name='send_email'),
    path('telegram-webhook/', telegram_webhook, name='telegram_webhook'),
]
