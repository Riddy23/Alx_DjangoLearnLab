"""
Sample queries (Task 0).
Run from Django shell (python manage.py shell) or import and call functions.
"""

from .models import Author, Book, Library

def books_by_author(author_name):
    """Return a queryset of books written by author_name."""
        try:
                author = Author.objects.get(name=author_name)
                        return Book.objects.filter(author=author)
                            except Author.DoesNotExist:
                                    return Book.objects.none()

                                    def books_in_library(library_name):
                                        """Return a queryset of books in the named library."""
                                            try:
                                                    lib = Library.objects.get(name=library_name)
                                                            return lib.books.all()
                                                                except Library.DoesNotExist:
                                                                        return Book.objects.none()

                                                                        def librarian_of_library(library_name):
                                                                            """Return the Librarian instance for a library, or None."""
                                                                                from .models import Librarian
                                                                                    try:
                                                                                            lib = Library.objects.get(name=library_name)
                                                                                                    return getattr(lib, 'librarian', None)
                                                                                                        except Library.DoesNotExist:
                                                                                                                return None
                                                                                                                