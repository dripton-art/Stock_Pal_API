from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializer import UserRegistrationSerializer

User = get_user_model()

'''
views
- handle user registration
- expect email and password - required
- validate email and password
- save the data
'''

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = User_serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Registration successfull'})
