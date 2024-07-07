from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', views.RegisterView.as_view({'get': 'list'})),
    path('user/', views.UserView.as_view({'get': 'list'})),
    path('login/', views.LoginView.as_view({'get': 'list'})),
]
