from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from api.tasks import send_welcome_email
from .models import TelegramUser

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import requests

BOT_TOKEN = '7906497727:AAHIPvMv8s9gzBnS51K7O32YHqc74xbB76A'

class PublicAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"message": "This is a public endpoint. No authentication required."})

class ProtectedAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}. This is a protected endpoint."})

class TriggerEmailView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('username')
        if not email or not username:
            return Response({'error': 'Email and username are required.'}, status=status.HTTP_400_BAD_REQUEST)
        send_welcome_email.delay(email, username)
        return Response({'message': f'✅ Welcome email scheduled for {email}'}, status=status.HTTP_200_OK)

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            message = data.get('message', {})
            text = message.get('text', '').strip()  # ✨ Clean input
            chat = message.get('chat', {})
            username = chat.get('username', 'friend')  # ✨ Default to "friend"
            chat_id = chat.get('id')

            if not chat_id:
                return JsonResponse({"error": "Invalid chat ID"}, status=400)

            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

            # ✨ RICHER RESPONSES (NEW)
            if text == '/start':
                user, created = TelegramUser.objects.get_or_create(
                    chat_id=chat_id,
                    defaults={'username': username}
                )
                response = (
                    f"🎉 *Welcome, {username}!* \n\n"
                    "You're now registered with MyShopBot! "
                    "Use /help to see what I can do. 😊"
                ) if created else (
                    f"👋 *Hey there, {username}!* \n\n"
                    "You're already registered! "
                    "Try /info to see your details."
                )
                requests.post(url, json={'chat_id': chat_id, 'text': response, 'parse_mode': 'Markdown'})

            elif text == '/help':
                requests.post(url, json={
                    'chat_id': chat_id,
                    'text': (
                        "📜 *Help Menu* 📜\n\n"
                        "Here’s what I can do:\n\n"
                        "➡️ */start* - Register with me\n"
                        "➡️ */info* - View your profile\n"
                        "➡️ */shop* - See products 🛒\n"  # ✨ New command example
                        "➡️ */about* - Learn about me\n"
                        "➡️ */help* - Show this menu\n\n"
                        "Just type a command and I’ll help! 😃"
                    ),
                    'parse_mode': 'Markdown'
                })

            elif text == '/about':
                requests.post(url, json={
                    'chat_id': chat_id,
                    'text': (
                        "🤖 *About MyShopBot* 🤖\n\n"
                        "I’m your friendly shopping assistant!\n\n"
                        "✨ *Features:*\n"
                        "- Track orders\n"
                        "- Browse products\n"
                        "- Get support\n\n"
                        "Version: 1.0\n"
                        "Made with ❤️ using Django + Python"
                    ),
                    'parse_mode': 'Markdown'
                })

            elif text == '/info':
                try:
                    user = TelegramUser.objects.get(chat_id=chat_id)
                    requests.post(url, json={
                        'chat_id': chat_id,
                        'text': (
                            f"📋 *Your Profile* 📋\n\n"
                            f"👤 *Username:* {user.username}\n"
                            f"🆔 *Chat ID:* `{user.chat_id}`\n"
                            f"📅 *Joined:* {user.created_at.strftime('%d %b %Y')}\n\n"
                            f"Thanks for using MyShopBot! ❤️"
                        ),
                        'parse_mode': 'Markdown'
                    })
                except TelegramUser.DoesNotExist:
                    requests.post(url, json={
                        'chat_id': chat_id,
                        'text': "❌ You’re not registered yet! Use /start first."
                    })

            # ✨ NEW COMMAND EXAMPLE (optional)
            elif text == '/shop':
                requests.post(url, json={
                    'chat_id': chat_id,
                    'text': (
                        "🛍️ *Shop Menu* 🛍️\n\n"
                        "What are you looking for?\n\n"
                        "1. Electronics 📱\n"
                        "2. Clothes 👕\n"
                        "3. Books 📚\n\n"
                        "Reply with a number!"
                    ),
                    'parse_mode': 'Markdown'
                })

            # ✨ DEFAULT RESPONSE (if unknown command)
            else:
                requests.post(url, json={
                    'chat_id': chat_id,
                    'text': (
                        f"🤔 *Hmm, I didn’t get that!*\n\n"
                        f"Try one of these commands:\n\n"
                        f"- /start\n"
                        f"- /help\n"
                        f"- /about\n\n"
                        f"I’m here to help! 😊"
                    ),
                    'parse_mode': 'Markdown'
                })

            return JsonResponse({"ok": True})

        except Exception as e:
            return JsonResponse({"error": "Oops! Something went wrong."}, status=500)

    return JsonResponse({"error": "Only POST requests allowed"}, status=400)