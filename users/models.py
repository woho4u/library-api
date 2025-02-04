from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    readingLists = models.JSONField(default=list, help_text='A list of the booklists, each booklist containing book ids')

    def __str__(self):
        return self.username
