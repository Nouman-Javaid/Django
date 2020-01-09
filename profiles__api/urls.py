from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles__api import views


# router creates all the four urls for us
router = DefaultRouter()
router.register('hello-viewset', views.HelloAPIViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
# router.register('profile-feed', views.UserProfileFeedAPI)

urlpatterns = [
    path('', include(router.urls)),

    path('hello-apiview/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path('logout/', views.UserLogoutAPIView.as_view()),



]
