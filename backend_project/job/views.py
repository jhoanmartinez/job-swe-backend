from rest_framework import views
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response

class GetAllJobs(views.APIView):

    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)