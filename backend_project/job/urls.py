from django.urls import path
from .views import GetAllJobs, GetJobByID, PostJob, UpdateJob, DeleteJob, StatsPerTopic\
                    , AppliedToJob


urlpatterns = [
    path('jobs/', GetAllJobs.as_view(), name="jobs"),
    path('jobs/new/', PostJob.as_view(), name='new-job'),
    path('jobs/<int:job_id>/', GetJobByID.as_view(), name='job-detail'),
    path('jobs/<int:job_id>/update/', UpdateJob.as_view(), name='update-job'),
    path('jobs/<int:job_id>/delete/', DeleteJob.as_view(), name='delete-job'),
    path('stats/<str:topic>/', StatsPerTopic.as_view(), name='stats'),
    path('jobs/<int:id>/apply/', AppliedToJob.as_view(), name='apply-to-job')
]