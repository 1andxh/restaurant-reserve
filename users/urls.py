from django.urls import path
from users.views import RegisterUser
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns =[
    path('register/', RegisterUser.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]