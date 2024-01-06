from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from users.views import MyTokenObtainPairView

from . import views

urlpatterns = [
    path("sign-up/", views.UserRegistrationView.as_view(), name="sign-up"),
    path("log-in/", views.UserLoginView.as_view(), name="log-in"), 
    path('email-verification/<str:uidb64>/<str:token>/', views.ActivateView.as_view(), name='email-verification'),
    path('email-verification/<str:uidb64>/<str:token>/', views.ActivateView.as_view(), name='email-verification'),
    path('reset-password/', views.ChangePasswordView.as_view(), name='password-reset'),    
    
    path("jwt/create/", MyTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token-verify"),
]