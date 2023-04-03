from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UsersAPIView, UserTokenObtainPairView

urlpatterns = [
    path('', UsersAPIView.as_view()),
    path('login/', UserTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
