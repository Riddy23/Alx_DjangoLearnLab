from django.db import models

class Author(models.Model):
    """
    Author model represents a writer who can have multiple books.
    Fields:
    - name: The author's full name.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a book written by an author.
    Fields:
    - title: The title of the book.
    - publication_year: The year this book was published.
    - author: A ForeignKey linking the book to its Author (One-to-Many).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()                        
                                       
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"


