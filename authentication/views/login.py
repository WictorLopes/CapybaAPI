from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def login_user(request):
    data = request.data
    if 'email' in data and 'password' in data:
        user = authenticate(request, username=data['email'], password=data['password'])
        if user:
            login(request, user)
            #token, created = Token.objects.get_or_create(user=user)
            return Response(status=status.HTTP_200_OK)
    return Response({'error': 'Credenciais inválidas.'}, status=status.HTTP_400_BAD_REQUEST)
