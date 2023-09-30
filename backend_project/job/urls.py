from django.urls import path
from .views import GetAllJobs, GetJobByID, PostJob, UpdateJob, DeleteJob

urlpatterns = [
    path('all/', GetAllJobs.as_view(), name="jobs"),
    path('<int:job_id>/', GetJobByID.as_view(), name='job-detail'),
    path('new/', PostJob.as_view(), name='new-job'),
    path('update/<job_id>/', UpdateJob.as_view(), name='update-job'),
    path('delete/<job_id>/', DeleteJob.as_view(), name='delete-job')
]