from django.urls import path
from .views import GetAllJobs, GetJobByID, PostJob, UpdateJob, DeleteJob, StatsPerTopic

urlpatterns = [
    path('all/', GetAllJobs.as_view(), name="jobs"),
    path('<int:job_id>/', GetJobByID.as_view(), name='job-detail'),
    path('new/', PostJob.as_view(), name='new-job'),
    path('update/<int:job_id>/', UpdateJob.as_view(), name='update-job'),
    path('delete/<int:job_id>/', DeleteJob.as_view(), name='delete-job'),
    path('stats/<str:topic>/', StatsPerTopic.as_view(), name='stats')
]