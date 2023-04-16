from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserFollowView, UserFollowingViewSet, UserTokenObtainPairView, UsersViewSet

router = DefaultRouter()

router.register("profile", UsersViewSet)
router.register("subscribe", UserFollowingViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("subs", UserFollowView.as_view()),
    path("login/", UserTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
