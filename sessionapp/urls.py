from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('', Home.as_view(),name="Home"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('my_cookies',my_cookies,name="my_cookies"),
    path('get_cookies',get_cookies,name="get_cookies"),
    path('delete_cookies',delete_cookies,name="delete_cookies"),
]