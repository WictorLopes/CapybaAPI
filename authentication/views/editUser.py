from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from ..serializers import userSerializer

class EditUserProfile(generics.RetrieveUpdateAPIView):
    serializer_class = userSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
