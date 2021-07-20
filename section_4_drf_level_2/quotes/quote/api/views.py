from rest_framework import (
    generics,
    permissions
)

from quote.models import Quote
from quote.api.serializers import QuoteSerializer
from quote.api.pagination import DefaultSetPagination
# from quote.api.permissions import IsAdminUserOrReadOnly


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by('id')
    serializer_class = QuoteSerializer
    pagination_class = DefaultSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
