from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles__api import views


# router creates all the four urls for us
router = DefaultRouter()
# router.register('hello-viewset', views.HelloAPIViewSet, basename='hello-viewset')
# router.register('profile-feed', views.UserProfileFeedAPI)
router.register('', views.UserProfileViewSet)

urlpatterns = [

    path('profile/login/', views.UserLoginAPIView.as_view()),
    path('profile/logout/', views.UserLogoutAPIView.as_view()),
    path('profile/', include(router.urls)),

    # path('hello-apiview/', views.HelloAPIView.as_view()),

]
