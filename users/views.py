from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.filters import SearchFilter

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['username', 'id']  # keep search for text if desired


class AddBookToReadingListView(APIView):
    def post(self, request, *args, **kwargs):
        # Extract book_id and optionally a reading list name from the request
        book_id = request.data.get("book_id")
        list_name = request.data.get("list_name", "Favorites")
        user_id = request.data.get("user_id")

        if not book_id:
            return Response({"error": "book_id is required."},
                            status=status.HTTP_400_BAD_REQUEST)

        user = request.user

        # Get existing reading lists or initialize an empty list
        reading_lists = user.reading_lists if user.reading_lists else []

        # Search for the specified reading list
        for reading_list in reading_lists:
            if reading_list.get("name") == list_name:
                # Add the book_id if not already in the list
                if book_id not in reading_list.get("bookIds", []):
                    reading_list.setdefault("bookIds", []).append(book_id)
                break
        else:
            # If the list doesn't exist, create a new one
            reading_lists.append({
                "name": list_name,
                "bookIds": [book_id]
            })

        # Update and save the user's reading lists
        user.reading_lists = reading_lists
        user.save()

        return Response({
            "message": "Book added successfully",
            "reading_lists": reading_lists
        }, status=status.HTTP_200_OK)