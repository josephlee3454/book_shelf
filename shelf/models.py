from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    # authors = models.ManyToManyField(Author, related_name='books')
    
    def __str__(self):
        return self.title + " " + self.description

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name='authors')

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.notes
