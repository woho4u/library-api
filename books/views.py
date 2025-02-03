from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter
from rest_framework.filters import SearchFilter

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author']  # keep search for text if desired
