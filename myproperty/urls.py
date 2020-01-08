from django.urls import path, include
from myproperty import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile-feed', views.UserProfileFeedAPI)

urlpatterns = [
    path('', include(router.urls)),
]
