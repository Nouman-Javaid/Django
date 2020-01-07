from django.urls import path, include
from profiles__api import views
from rest_framework.routers import DefaultRouter

# router creates all the four urls for us
router = DefaultRouter()
router.register('hello-viewset', views.HelloAPIViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('profile-feed', views.UserProfileFeedAPI)

urlpatterns = [
    path('', include(router.urls)),

    path('hello-apiview/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),

]
