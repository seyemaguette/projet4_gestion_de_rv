from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LogoutView
from .views import UserLoginView,UserRegistrationView,SerializerCreatePatient
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)

urlpatterns = [
    #---------------------api-------------------
    # ---------------token-----------
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('patient/',SerializerCreatePatient.as_view()),
    path('registation/',UserRegistrationView.as_view()),
    path('login/',UserLoginView.as_view()),
    
    # ---------------token-----------
]