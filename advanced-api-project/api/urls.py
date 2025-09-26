from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

    urlpatterns = [
        path("books/", BookListView.as_view(), name="book-list"),
        path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
        path("books/create/", BookCreateView.as_view(), name="book-create"),
        path("books/<int:pk>/update/", BookUpdateView.as_view(), name="book-update"),
        path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
        path('books/', BookListView.as_view(), name='book-list'),
        path("books/", BookListView.as_view(), name="book-list"),                     # List & Create (if ListCreateAPIView used)
        path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),       # Retrieve
        path("books/create/", BookCreateView.as_view(), name="book-create"),         # Create (if separate)
        path("books/<int:pk>/update/", BookUpdateView.as_view(), name="book-update"), # Update
        path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"), # Delete
                        
    ]
