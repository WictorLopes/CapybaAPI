from rest_framework import generics
from django.db.models import Q
from ..models import item
from ..serializers import itemSerializer
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied

class RestrictedItemList(generics.ListAPIView):
    serializer_class = itemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Verifique se o e-mail do usuário foi verificado
        if not user.profile.email_confirmed:
            raise PermissionDenied("Email not verified")

        queryset = item.objects.all()
        page_size = self.request.query_params.get('page_size', 10)
        page = self.request.query_params.get('page', 1)
        search = self.request.query_params.get('search', '')
        is_draft = self.request.query_params.get('is_draft', None)

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )

        if is_draft is not None:
            queryset = queryset.filter(is_draft=is_draft)

        total_items = queryset.count()
        queryset = queryset[(int(page) - 1) * int(page_size):int(page) * int(page_size)]

        return queryset
