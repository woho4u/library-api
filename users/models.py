from django.db import models
from books.models import Book

class User(models.Model):
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class ReadingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reading_lists')
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    books = models.ManyToManyField(Book, through='ReadingListBook', related_name='reading_lists')

class ReadingListBook(models.Model):
    reading_list = models.ForeignKey(ReadingList, on_delete=models.CASCADE, related_name='reading_list_books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reading_list_books')
    added_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('reading_list', 'book')

    def __str__(self):
        return f"{self.book.title} in {self.reading_list.name}"