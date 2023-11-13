import secrets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from ..models import userProfile 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_email_confirmation_token(request):
    user_profile, created = userProfile.objects.get_or_create(user=request.user)
    token = secrets.token_urlsafe(16)
    print('aqui', token)
    user_profile.email_confirmation_token = token
    user_profile.save()

    send_mail(
        'Confirmação de E-mail',
        f'Seu token de confirmação de e-mail é: {token}',
        'noreply@example.com',
        [request.user.email],
        fail_silently=False,
    )
    return Response({'message': 'Token de confirmação enviado com sucesso.'}, status=status.HTTP_200_OK)
