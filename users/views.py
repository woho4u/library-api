from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.filters import SearchFilter

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['username', 'id']  # keep search for text if desired
