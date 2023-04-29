from django.urls import include, path
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserFollowView, UserFollowingViewSet, UserTokenObtainPairView, UsersViewSet, UsersAPIView

router = DefaultRouter()

router.register("profile", UsersViewSet)
router.register("subscribe", UserFollowingViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path('1', UsersAPIView.as_view()),
    path("subs", UserFollowView.as_view()),
    path("login/", UserTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
