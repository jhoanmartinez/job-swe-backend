from django.urls import path
from .views import GetAllJobs

urlpatterns = [
    path('jobs/', GetAllJobs.as_view(), name="jobs")
]