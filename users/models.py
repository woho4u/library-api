from django.db import models
from books.models import Book

class User(models.Model):
    """
    Simple User model for demonstration purposes.
    In a real project, you would typically use or extend
    Django's built-in User model from django.contrib.auth.
    """
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class ReadingList(models.Model):
    """
    A reading list belongs to one user
    and can contain multiple books (via a ManyToMany relationship).
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reading_lists')
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    books = models.ManyToManyField(Book, through='ReadingListBook', related_name='reading_lists')

class ReadingListBook(models.Model):
    """
    Junction table (through model) for the many-to-many relationship
    between ReadingList and Book. This allows additional fields such as
    'added_at' or 'status' to be stored for each book in a reading list.
    """
    reading_list = models.ForeignKey(ReadingList, on_delete=models.CASCADE, related_name='reading_list_books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reading_list_books')
    added_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        # Ensure each (reading_list, book) pair is unique
        unique_together = ('reading_list', 'book')

    def __str__(self):
        return f"{self.book.title} in {self.reading_list.name}"