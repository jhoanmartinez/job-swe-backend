from rest_framework.views import APIView
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Avg, Min, Max
from .filters import JobFilter

class GetAllJobs(APIView):

    def get(self, request):
        # jobs = Job.objects.all()
        filterset = JobFilter(request.GET, queryset=Job.objects.all().order_by('id'))
        serializer = JobSerializer(filterset.qs, many=True)
        return Response(serializer.data)

class GetJobByID(APIView):

    def get(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
            serializer = JobSerializer(job)
            return Response(serializer.data)
        except Job.DoesNotExist:
            return Response({"message": "El trabajo no existe"}, status=status.HTTP_404_NOT_FOUND)

class PostJob(APIView):

    def post(self, request):
        print(request.data)
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateJob(APIView):

    def patch(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response( {'message': 'Job not exist'}, status=status.HTTP_404_NOT_FOUND )
        serializer = JobSerializer(job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteJob(APIView):

    def delete(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response( {'message': 'Job not exist'}, status=status.HTTP_404_NOT_FOUND )
        job.delete()
        return Response( {'message': 'Job deleted succesfully'}, status=status.HTTP_204_NO_CONTENT )

class StatsPerTopic(APIView):

    def get(self,request, topic):
        args = {'title__icontains': topic}
        jobs = Job.objects.filter(**args)
        if len(jobs) == 0:
            return Response({'message': f'No stats found for topic {topic}'})
        stats = jobs.aggregate(
            total_jobs = Count('title'),
            avg_positions = Avg('positions'),
            avg_salary = Avg('salary'),
            min_salary = Min('salary'),
            max_salary = Max('salary')
        )
        return Response({'stats': stats}, status=status.HTTP_200_OK)