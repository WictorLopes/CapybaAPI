from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    data = request.data
    if 'email' in data and 'password' in data:
        try:
            user = User.objects.create_user(username=data['email'], email=data['email'], password=data['password'])
            user.first_name = data.get('first_name', '')
            user.profile_image = data.get('profile_image')
            user.save()
            return Response({'message': 'Usuário registrado com sucesso.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Email e senha são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)
def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(email=email).exists():
            return Response("User with this email already exists", status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(email=email, password=password)
        return Response("User created successfully", status=status.HTTP_201_CREATED)
