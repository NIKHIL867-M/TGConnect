# 🤖 Django Telegram Bot Gateway

A Telegram-integrated Django project that receives bot commands via webhooks, authenticates users, and performs background tasks using Celery and Redis.

---

## 🚀 Features

- 🔐 Token-authenticated REST APIs (public + protected)
- 💬 Telegram Bot webhook integration
- 🧠 Background task queue using Celery + Redis
- 📨 Welcome email task demo
- 🌐 Minimal HTML login page using Django templates
- 📦 Environment variable support via `.env`

---

## 🛠 Tech Stack

- **Backend:** Python 3.12, Django 5.2.3, Django REST Framework
- **Bot:** Telegram Bot API
- **Async Tasks:** Celery + Redis
- **Frontend:** Django Templates (for login)
- **Deployment Tools:** ngrok (for testing), python-decouple

---

## 🔧 Setup & Installation

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/django-telegram-bot.git
cd django-telegram-bot
```

### 2. Create & Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
# OR manually:
pip install django djangorestframework python-decouple celery redis
```

---

### 4. Redis Installation

Make sure Redis is running locally:

- **Windows:** Use Redis installer (`Redis-x64-3.0.504`)
- **macOS:** `brew install redis`
- **Linux:** `sudo apt install redis`

Start Redis:
```bash
redis-server
```

---

### 5. Configure Environment Variables

Create a `.env` file in the root directory:
```ini
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
BOT_TOKEN=your-telegram-bot-token
```

---

### 6. Run Django Server

```bash
python manage.py migrate
python manage.py runserver
```

---

### 7. Start Celery Worker

In a new terminal (venv activated):

```bash
celery -A myproject worker --loglevel=info
```

---

### 8. Use ngrok to Expose Localhost

```bash
ngrok http 8000
```

Copy the HTTPS URL and set your bot webhook:

```bash
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://<ngrok-url>/api/telegram-webhook/
```

---

## 📂 Project Structure

```
myproject/
├── api/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tasks.py
├── templates/
│   └── registration/login.html
├── myproject/
│   └── celery.py
├── .env
├── manage.py
└── requirements.txt
```

---

## ✅ Usage

- Start Django server → `/api/public/`, `/api/protected/`
- Use Postman or Curl with token to test protected API
- Send `/start` to bot → webhook triggered → user saved → greeting sent
- Register user → triggers background Celery task to send email

---

## 📌 Optional Enhancements (Future Scope)

- `/help` and `/about` command handlers
- Admin dashboard for registered Telegram users
- UI improvements
- Docker support
- Production deployment (Render, Railway, etc.)

---

## 📄 License

MIT License © 2025
