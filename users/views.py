from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
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
        #if there are any params, return readinglists with a matching user_id value
        if user_param is not None:
            return ReadingList.objects.filter(user_id=user_param)
        return super().get_queryset()

    def perform_create(self, serializer):
        """
        Here it is assumed the user is passed with the fetch request

        it is possible to automatically asign the user of the reading list or other logic

        for example: serializer.save(user=self.request.user)
        """
        serializer.save()


class ReadingListBookViewSet(viewsets.ModelViewSet):
    queryset = ReadingListBook.objects.all()
    serializer_class = ReadingListBookSerializer

    def perform_create(self, serializer):

        reading_list = serializer.validated_data['reading_list']  # The ReadingList instance
        new_book = serializer.validated_data['book']  # The Book instance being added

        # only enforce the genre check if the new book actually has a genre
        if new_book.genre:
            # Fetch any existing books in this reading list. reading_list is an object manager, not directly an object
            existing_books = reading_list.books.all()
            matching_keywords = 0

            # If there is at least one existing book, compare genres
            if existing_books.exists():
                first_book = existing_books[0]
                print(first_book.genre)
                print(new_book.genre)
                if first_book.genre == new_book.genre:
                    raise ValidationError({
                        "detail": (
                            f"Cannot add book with genre '{new_book.genre}' "
                            f"to a reading list containing a book of genre '{first_book.genre}'."
                        )
                    })
                    #print("genre are NOT matching")
                for keyword in new_book.keywords:
                    if keyword in first_book.keywords:
                        matching_keywords = matching_keywords + 1
                if matching_keywords == 0:
                    raise ValidationError({
                        "detail": (
                            f"Keywords do not match. The book to add needs to have at least one matching keyword"
                        )
                    })
                    #print("keywords are not matching")


        # If no books exist in the reading list or if all genres match (or empty), we save
        serializer.save()
