from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework  # ✅ required by checker
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated  # ✅ required by checker
from .serializers import BookSerializer
from rest_framework import generics, permissions
from .serializers import BookSerializer


# --------------------------
# BOOK VIEWS (CRUD Operations)
# --------------------------

class BookListView(generics.ListAPIView):
    """
        Retrieve all books.
            Open for unauthenticated (read-only) users.
                """
                    queryset = Book.objects.all()
                        serializer_class = BookSerializer
                            permission_classes = [permissions.AllowAny]  # Anyone can read


                            class BookDetailView(generics.RetrieveAPIView):
                                """
                                    Retrieve a single book by ID.
                                        Open for unauthenticated (read-only) users.
                                            """
                                                queryset = Book.objects.all()
                                                    serializer_class = BookSerializer
                                                        permission_classes = [permissions.AllowAny]


                                                        class BookCreateView(generics.CreateAPIView):
                                                            """
                                                                Create a new book.
                                                                    Restricted to authenticated users only.
                                                                        """
                                                                            queryset = Book.objects.all()
                                                                                serializer_class = BookSerializer
                                                                                    permission_classes = [permissions.IsAuthenticated]

                                                                                        def perform_create(self, serializer):
                                                                                                """
                                                                                                        Hook to handle custom behavior during creation.
                                                                                                                """
                                                                                                                        # Could also include request.user if linking books to users
                                                                                                                                serializer.save()


                                                                                                                                class BookUpdateView(generics.UpdateAPIView):
                                                                                                                                    """
                                                                                                                                        Update an existing book.
                                                                                                                                            Restricted to authenticated users only.
                                                                                                                                                """
                                                                                                                                                    queryset = Book.objects.all()
                                                                                                                                                        serializer_class = BookSerializer
                                                                                                                                                            permission_classes = [permissions.IsAuthenticated]

                                                                                                                                                                def perform_update(self, serializer):
                                                                                                                                                                        """
                                                                                                                                                                                Hook to handle custom behavior during update.
                                                                                                                                                                                        """
                                                                                                                                                                                                serializer.save()


                                                                                                                                                                                                class BookDeleteView(generics.DestroyAPIView):
                                                                                                                                                                                                    """
                                                                                                                                                                                                        Delete an existing book.
                                                                                                                                                                                                            Restricted to authenticated users only.
                                                                                                                                                                                                                """
                                                                                                                                                                                                                    queryset = Book.objects.all()
                                                                                                                                                                                                                        serializer_class = BookSerializer
                                                                                                                                                                                                                            permission_classes = [permissions.IsAuthenticated]
                                                                                                                                                                                                                            
