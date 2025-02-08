from rest_framework import viewsets
from .models import User, ReadingList, ReadingListBook
from .serializers import (
    UserSerializer,
    ReadingListSerializer,
    ReadingListBookSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReadingListViewSet(viewsets.ModelViewSet):
    queryset = ReadingList.objects.all()
    serializer_class = ReadingListSerializer

#return reading lists belonging to the user in the pasams
    def get_queryset(self):
        #get the query params
        user_param = self.request.query_params.get('user')
        #if there are any params, return readinglists with a
        #user id matching the user_params
        if user_param is not None:
            return ReadingList.objects.filter(user_id=user_param)
        return super().get_queryset()

    def perform_create(self, serializer):
        """
        Example of customizing create behavior:
        - If you want to automatically assign the current user, for instance:

        serializer.save(user=self.request.user)

        Here, we assume the user is passed in the request body or handled
        by the `ReadingListSerializer`'s user_id field.
        """
        serializer.save()


class ReadingListBookViewSet(viewsets.ModelViewSet):
    queryset = ReadingListBook.objects.all()
    serializer_class = ReadingListBookSerializer

    def perform_create(self, serializer):
        """
        When creating a new reading_list_books entry, 
        you can do custom logic here if needed.
        """

        serializer.save()
