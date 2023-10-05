from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .serializers import SignUpSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser

class Register(APIView):

    def post(self, request):
        data = request.data
        user = SignUpSerializer(data=data)
        if user.is_valid():
            if not User.objects.filter(username=data['email']).exists():
                user = User.objects.create(
                    first_name = data['first_name'],
                    last_name = data['last_name'],
                    username = data['email'],
                    email = data['email'],
                    password = make_password(data['password'])
                )
                return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {
                        'error': 'User already exists'
                    },
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CurrentUser(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = UserSerializer(request.user)
        return Response(user.data, status=status.HTTP_200_OK)

class UpdateUser(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = User.objects.get(username=request.user)
        mutable_data = request.data.copy()
        if 'password' in mutable_data and mutable_data['password'] != '':
            mutable_data['password'] = make_password(mutable_data['password'])
        serializer = UserSerializer(user, data=mutable_data, many=False, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': "Error updated"}, status=status.HTTP_400_BAD_REQUEST)

class UploadResume(APIView):

    parser_classes = [FileUploadParser]

    def patch(self, request, format=None):
        file_obj = request.data['resume']
        return Response(status=status.HTTP_200_OK)
    

