from django.urls import path
from .views import (
  # LoginView, 
  MyTokenObtainPairView,
  RegisterView,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



urlpatterns = [
  # path("login/", LoginView.as_view()),
  path('register/', RegisterView.as_view(), name='register'),
  path('login/', MyTokenObtainPairView.as_view(), name='login'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]