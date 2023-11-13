from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def validate_email_confirmation_token(request):
    token = request.data.get('token')
    user = request.user
    if user.profile.email_confirmation_token == token:
        user.profile.email_confirmed = True
        user.profile.email_confirmation_token = None
        user.save()
        return Response({'message': 'E-mail confirmado com sucesso.'}, status=status.HTTP_200_OK)
    return Response({'error': 'Token de confirmação inválido.'}, status=status.HTTP_400_BAD_REQUEST)
