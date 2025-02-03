import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    # We'll allow ?id_in=1,2,3 for multiple IDs
    id_in = django_filters.BaseInFilter(field_name='id', lookup_expr='in')

    class Meta:
        model = Book
        fields = ['id_in', 'author', 'title']
