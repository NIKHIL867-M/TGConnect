# Telegram-Django-Bot-Integration

A complete integration of Telegram Bot API with Django REST Framework backend and Celery for async tasks.

## 🚀 Tech Stack
- Python 3.12
- Django 5.2.3
- Django REST Framework 3.16.0
- Redis (Celery Broker)
- Celery
- Telegram Bot API

## ✅ Features

- Token-based Auth (DRF)
- Public & Protected REST Endpoints
- Telegram Bot Webhook Integration
- User Registration via Telegram
- Celery Task Queue for async tasks
- Welcome Email on Telegram Join
- Login Page with CSRF Security
- .env Config & .gitignore for secrets

## 🔧 Setup Instructions

1. Clone the repo & create virtualenv
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate for Windows
pip install -r requirements.txt
```

2. Setup environment variables
```
DEBUG=True
SECRET_KEY=your_secret
BOT_TOKEN=your_telegram_token
```

3. Run Redis locally
```
redis-server
```

4. Start services
```
python manage.py runserver
celery -A myproject worker --loglevel=info
```

5. Expose via Ngrok for webhook
```
ngrok http 8000
```

6. Register Webhook using Telegram API

## 📂 Folder Structure
- `myproject/` – Django project
- `api/` – App with API views and Telegram logic
- `templates/` – HTML login template


---

© 2025 | Built for learning & real-world integration.
