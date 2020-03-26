from django.urls import path, include
from myproperty import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('profile-feed', views.UserProfileFeedAPI)
# router.register('BasicProperties', views.BasicPropertiesViewSet)
router.register('features', views.PropertyViewSet)
router.register('gallery', views.PropertyImagesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



