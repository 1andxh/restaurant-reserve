from django.urls import path
from users.views import RegisterUser

urlpatterns =[
    path('register/', RegisterUser.as_view())
]