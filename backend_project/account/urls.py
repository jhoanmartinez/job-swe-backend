from django.urls import path
from .views import Register, CurrentUser, UpdateUser

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('me/', CurrentUser.as_view(), name='current-user'),
    path('me/update/', UpdateUser.as_view(), name='update-user'),
]