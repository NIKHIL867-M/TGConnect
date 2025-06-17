from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),               # ✅ API routes from your app
    path('api/token/', obtain_auth_token, name='api_token'),  # ✅ DRF Token Auth
    path('login/', auth_views.LoginView.as_view(), name='login'),    # ✅ Optional Login View
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # ✅ Optional Logout View
]
