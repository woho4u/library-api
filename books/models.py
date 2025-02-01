from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.CharField(default='This is a great book!', max_length=400)
    genre = models.CharField(max_length=100)
    keywords = models.JSONField(default=list, help_text='A list of keywords')
    coverImage = models.URLField(null=True, help_text='Cover image link')
    published_date = models.DateField()

    def __str__(self):
        return self.title
