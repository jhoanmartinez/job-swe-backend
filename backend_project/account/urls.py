from django.urls import path
from .views import Register, CurrentUser

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('me/', CurrentUser.as_view(), name='current-user'),
]