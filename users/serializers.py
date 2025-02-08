from rest_framework import serializers
from .models import User, ReadingList, ReadingListBook, Book
from books.serializers import BookSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ReadingListBookSerializer(serializers.ModelSerializer):

    book = BookSerializer(read_only=True)

    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        source='book',
        write_only=True
    )
    class Meta:
        model = ReadingListBook
        fields = '__all__'


class ReadingListSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user',
        write_only=True
    )

    reading_list_books = ReadingListBookSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = ReadingList
        fields = '__all__'



